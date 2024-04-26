import logging
import os

logger = logging.getLogger()


class HideSensitiveData(logging.Filter):

    def filter(self, record):
        record.msg = str(record.msg).replace(os.getenv("ADMIN_PASSWORD"), "****")
        return True


logger.addFilter(HideSensitiveData())
