# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler

LOGFILE = "pyromarc-template.log"
# Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Formatteur
formatter = logging.Formatter('%(asctime)s : %(levelname)s :: %(message)s')
# File handler
file_handler = RotatingFileHandler(LOGFILE, 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# Stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
