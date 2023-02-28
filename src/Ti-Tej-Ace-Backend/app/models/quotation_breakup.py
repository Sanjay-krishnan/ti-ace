# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.price import Price  # noqa: F401,E501


class QuotationBreakup(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, title: str=None, price: Price=None):  # noqa: E501
        """QuotationBreakup - a model defined in Swagger

        :param title: The title of this QuotationBreakup.  # noqa: E501
        :type title: str
        :param price: The price of this QuotationBreakup.  # noqa: E501
        :type price: Price
        """
        self.swagger_types = {
            'title': str,
            'price': Price
        }

        self.attribute_map = {
            'title': 'title',
            'price': 'price'
        }
        self._title = title
        self._price = price

    @classmethod
    def from_dict(cls, dikt) -> 'QuotationBreakup':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Quotation_breakup of this QuotationBreakup.  # noqa: E501
        :rtype: QuotationBreakup
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self) -> str:
        """Gets the title of this QuotationBreakup.


        :return: The title of this QuotationBreakup.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this QuotationBreakup.


        :param title: The title of this QuotationBreakup.
        :type title: str
        """

        self._title = title

    @property
    def price(self) -> Price:
        """Gets the price of this QuotationBreakup.


        :return: The price of this QuotationBreakup.
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price: Price):
        """Sets the price of this QuotationBreakup.


        :param price: The price of this QuotationBreakup.
        :type price: Price
        """

        self._price = price
