#!/usr/bin/env python3
""" Main file """
from typing import List
from re import sub


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    It takes a list of fields, a redaction string, a message,
    and a separator, and returns a redacted message

    :param fields: a list of fields to redact
    :type fields: List[str]
    :param redaction: The string to replace the field with
    :type redaction: str
    :param message: the message to be filtered
    :type message: str
    :param separator: The separator between fields in the message
    :type separator: str
    :return: A string with the redacted fields.
    """

    for field in fields:
        message = sub(f'{field}=.*?{separator}',
                      f'{field}={redaction}{separator}', message)
    return message
