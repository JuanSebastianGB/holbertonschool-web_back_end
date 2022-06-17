#!/usr/bin/env python3
""" Main file """
from typing import List
from re import sub


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ returns a redacted message """
    for field in fields:
        message = sub(f'{field}=.*?{separator}',
                      f'{field}={redaction}{separator}', message)
    return message
