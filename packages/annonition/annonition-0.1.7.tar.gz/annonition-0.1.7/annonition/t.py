from logger import CustomLogger
import numpy as np
import random
import string
import time

def random_string(length=5):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase 
    return ''.join(random.choice(letters) for i in range(length))

logger = CustomLogger(level="DEBUG", ignore=["/health", "Press CTRL+C to quit"], include_level=False)

logger.spam("This is a spam message.")
logger.debug("This is a debug message.")

logger.verbose("This is a verbose message.")
logger.info("This is an info message.")
logger.notice("This is a notice message.")
logger.warning("This is a warning message.")
logger.success("This is a success message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

x = [np.random.randint(1, 10) for i in range(5)]
y = {i: random_string(5) for i in range(5)}
logger.info(x)
logger.error(y)

# with logger.spinner("Doing something...") as progress:
#     time.sleep(1)
#     progress.change("Still doing something...")
#     time.sleep(1)
#     progress.log("Did something, but not done yet.")
#     progress.revert() # Changes back to the original message.
#     time.sleep(1)
#     progress.fail("Couldnt do everything.") # Message is optional.


# with logger.timer("Doing something...") as timer:
#     time.sleep(1)
#     logger.info("Still working...")
#     time.sleep(1)
#     logger.info("Almost done...")
#     time_taken = timer.get_time()
#     print(f"Time taken: {time_taken:.2f} seconds.")
#     time.sleep(1)
#     logger.success("Done.")

def add(a, b):
    return a + b

with logger.spinner("Doing heavy math...") as spinner:
    time.sleep(1)
    total = add(2, 2)
    if total == 4:
        spinner.success(f"Breakthrough in math achieved!")
    spinner.fail("Math is hard.")
    time.sleep(10)