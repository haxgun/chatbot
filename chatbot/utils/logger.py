import logging
import os

log_dir = os.path.join(os.path.dirname(__file__), "logs")
ch = logging.StreamHandler()
logger = logging.getLogger(__name__)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, "error.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

ch.setLevel(logging.DEBUG)
logger.addHandler(ch)