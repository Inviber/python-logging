import logging

# Least to most critical
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")