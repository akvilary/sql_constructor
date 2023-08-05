# coding=utf-8
"""
Module of SqlFilters class.
"""

__author__ = 'https://github.com/akvilary'

from typing import Optional


from .constants import AND_MODE, OR_MODE
from .sql_filter import SqlFilter
from .utils.classes.string_convertible import StringConvertible


class SqlFilters(StringConvertible):
    """
    SqlFilters class is invented to build sql filters faster.
    """

    def __init__(self, filters: Optional[dict] = None, mode: str = AND_MODE, /, **kwargs):
        self.filters = {}
        if filters:
            self.filters.update(filters)
        if kwargs:
            self.filters.update(kwargs)
        self.mode = mode

    def __str__(self):
        converted = ''
        if self.filters:
            method = (
                '__rand__'
                if self.mode.upper() == AND_MODE
                else '__ror__'
                if self.mode.upper() == OR_MODE
                else None
            )
            if method:
                for key, value in self.filters.items():
                    current_filter = SqlFilter({key: value})
                    converted = getattr(current_filter, method)(converted)
        return converted
