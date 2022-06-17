#!/usr/bin/env python3
""" Main file """
from typing import List
import re
import logging

PII_FIELDS = ["name", "email", "ssn", "password", "ip"]


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        It takes a list of fields, a redaction string, a log message, and a
        separator, and returns a filtered log message

        :param record: The record to be formatted
        :type record: logging.LogRecord
        :return: A string.
        """
        return self.filter_datum(list(self.fields), self.REDACTION,
                                 logging.Formatter(self.FORMAT).format(record),
                                 self.SEPARATOR)

    def filter_datum(self, fields: List[str], redaction: str,
                     message: str, separator: str) -> str:
        """
        It takes a list of fields, a redaction string, a message,
        and a separator, and returns a redacted version of the message

        :param fields: A list of strings that represent the fields to be
        redacted
        :type fields: List[str]
        :param redaction: The string to replace the data with
        :type redaction: str
        :param message: the message to be filtered
        :type message: str
        :param separator: The separator between fields in the message
        :type separator: str
        :return: A string with the fields redacted.
        """
        for field in fields:
            message = re.sub(f'{field}=.*?{separator}',
                             f'{field}={redaction}{separator}', message)
        return message


def get_logger() -> logging.Logger:
    """
    It creates a logger that will log to the console,
    and will redact any fields in the log message that
    are in the list of PII_FIELDS
    :return: A logger object.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger
