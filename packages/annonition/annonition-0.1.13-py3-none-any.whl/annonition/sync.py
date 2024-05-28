import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from google.cloud import storage
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google.api_core.exceptions import GoogleAPIError
from requests.exceptions import ConnectionError, SSLError
from urllib3.exceptions import MaxRetryError
from google.auth.exceptions import TransportError
from logger import CustomLogger
from google.cloud.storage.blob import Blob

logger = CustomLogger()


bucket_name = "annobackup"

def get_storage_client():
    """Creates a storage client with retry mechanism for reconnection."""
    @retry(
        retry=retry_if_exception_type((GoogleAPIError, SSLError, ConnectionError, MaxRetryError, TransportError)), 
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, max=10)
    )
    def connect():
        return storage.Client()

    return connect()

storage_client = get_storage_client()
bucket = storage_client.bucket(bucket_name)

def reconnect_bucket():
    global storage_client, bucket
    storage_client = get_storage_client()
    bucket = storage_client.bucket(bucket_name)

class Watcher:
    DIRECTORY_TO_WATCH = "W:/"
    interrupted = False

    def __init__(self):
        self.observer = Observer()

    def run(self):
        self.initial_sync()
        if Watcher.interrupted:
            return
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        if self.observer.is_alive():
            self.observer.stop()
            logger.warning("Observer Stopped")
            self.observer.join()

    def initial_sync(self):
        for subdir, dirs, files in os.walk(self.DIRECTORY_TO_WATCH):
            for file in files:
                file_path = os.path.join(subdir, file)
                try:
                    checkAndUpload(file_path)
                except KeyboardInterrupt:
                    logger.warning("Initial sync interrupted by user")
                    Watcher.interrupted = True
                    self.stop()
                    return

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory or event.event_type != 'created':
            return None
        try:
            checkAndUpload(event.src_path)
        except KeyboardInterrupt:
            logger.warning("Event handler interrupted by user")
            Watcher().stop()
            Watcher.interrupted = True

def checkAndUpload(file_path):
    with logger.spinner(f"Checking {file_path}...") as spinner:
        if not file_in_cloud(file_path):
            spinner.change(f"File not present in cloud - {file_path}, checking if stable...")
            # TODO: Instead, check if file is corrupted or not
            if is_file_stable(file_path):
                spinner.change(f"File is stable - {file_path}")
                upload_to_gcs(file_path, spinner)
        else:
            spinner.change(f"File already present in cloud - {file_path}")


def is_file_stable(path, interval=1, retries=5):
    initial_size = os.path.getsize(path)
    for _ in range(retries):
        time.sleep(interval)
        if os.path.getsize(path) != initial_size:
            return False
    return True

@retry(
    retry=retry_if_exception_type((GoogleAPIError, SSLError, ConnectionError, MaxRetryError, TransportError)), 
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, max=10)
)
def file_in_cloud(path):
    try:
        relative_path = os.path.relpath(path, start=Watcher.DIRECTORY_TO_WATCH)
        destination_blob_name = relative_path.replace("\\", "/")

        blob = bucket.blob(destination_blob_name)

        if blob.exists():
            cloud_blob = bucket.get_blob(destination_blob_name)
            local_file_size = os.path.getsize(path)

            if cloud_blob.size == local_file_size:
                return True
        return False
    except (GoogleAPIError, SSLError, ConnectionError, MaxRetryError, TransportError) as e:
        reconnect_bucket()
        raise e

# @retry(
#     retry=retry_if_exception_type((GoogleAPIError, SSLError, ConnectionError, MaxRetryError, TransportError)), 
#     stop=stop_after_attempt(5),
#     wait=wait_exponential(multiplier=1, max=10)
# )
def upload_to_gcs(path, spinner):
    spinner.change(f"Uploading {path} to cloud...")
    relative_path = os.path.relpath(path, start=Watcher.DIRECTORY_TO_WATCH)
    destination_blob_name = relative_path.replace("\\", "/")

    blob = bucket.blob(destination_blob_name)

    try:
        spinner.change(f"Uploading {path} to {destination_blob_name}...")
        blob.upload_from_filename(path)
        spinner.change(f'File {path} uploaded to {destination_blob_name}.')
    except (GoogleAPIError, SSLError, ConnectionError, MaxRetryError, TransportError) as e:
        reconnect_bucket()
        spinner.fail(f"Failed to upload {path}. Error: {str(e)}")
        raise

if __name__ == '__main__':
    try:
        w = Watcher()
        w.run()
    except KeyboardInterrupt:
        logger.warning("Program interrupted by user. Exiting...")
        w.stop()

