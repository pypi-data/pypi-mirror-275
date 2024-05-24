import os 
import sys 
import logging
from rich.logging import RichHandler

# # setup the loggins string format 
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# logging.basicConfig(
#     # level=logging.INFO,
#     level="NOTSET",
#     format=logging_str,
#     handlers=[
#         RichHandler(),
#         logging.FileHandler(log_filepath),
#         # logging.StreamHandler(sys.stdout),

#     ]
# )

# log = logging.getLogger('IVM6311')
# # log = logging.getLogger(__name__)

logging.basicConfig(
    level="NOTSET", format=logging_str, datefmt="[%X]", handlers=[
        RichHandler(),
        logging.FileHandler(log_filepath),
                                                                  ]
)  # set level=20 or logging.INFO to turn off debug
log = logging.getLogger(__name__)

# logger.debug("debug...")
# logger.info("info...")
# logger.warning("warning...")
# logger.error("error...")
# logger.fatal("fatal...")