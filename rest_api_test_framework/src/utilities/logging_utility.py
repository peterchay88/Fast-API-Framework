import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger()
load_dotenv("/Users/peter/Desktop/python/udemy/Rest_API_Project/secrets.env")


class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(os.getenv("ADMIN_PASSWORD"), "****")
        return True


logger.addFilter(HideSensitiveData())
