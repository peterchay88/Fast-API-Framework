import logging
import os
from dotenv import load_dotenv

LOGGER = logging.getLogger()
load_dotenv("../../secrets.env")


class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(os.getenv("ADMIN_PASSWORD"), "****")
        return True


LOGGER.addFilter(HideSensitiveData())