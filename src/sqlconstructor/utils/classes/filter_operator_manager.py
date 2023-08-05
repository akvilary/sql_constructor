# coding=utf-8
"""
Module of FilterOperatorManager class.
"""

__author__ = 'https://github.com/akvilary'

from sqlconstructor.constants import AND_MODE, OR_MODE
from .string_convertible import StringConvertible


class FilterOperatorManager(StringConvertible):
    """
    The class is invented to provide __and__, __rand__, __or__, __ror__ methods.
    It requires subclasses to have __str__ method.
    """
    def __and__(self, other):
        return gather_filters(self, other, AND_MODE)

    def __rand__(self, other):
        return gather_filters(other, self, AND_MODE)

    def __or__(self, other):
        return gather_filters(self, other, OR_MODE)

    def __ror__(self, other):
        return gather_filters(other, self, OR_MODE)


def gather_filters(one: StringConvertible, another: StringConvertible, operator: str) -> str:
    """Gather two filters by operator"""
    filters = []
    for _filter in (one, another):
        filter_as_str = str(_filter)
        if filter_as_str:
            filters.append(filter_as_str)
    return ('\n' + operator + '\n').join(filters)