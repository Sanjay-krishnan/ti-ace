# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.duration import Duration  # noqa: F401,E501
from models.price import Price  # noqa: F401,E501
from models.quotation_breakup import QuotationBreakup  # noqa: F401,E501


class Quotation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, price: Price=None, breakup: List[QuotationBreakup]=None, ttl: Duration=None):  # noqa: E501
        """Quotation - a model defined in Swagger

        :param price: The price of this Quotation.  # noqa: E501
        :type price: Price
        :param breakup: The breakup of this Quotation.  # noqa: E501
        :type breakup: List[QuotationBreakup]
        :param ttl: The ttl of this Quotation.  # noqa: E501
        :type ttl: Duration
        """
        self.swagger_types = {
            'price': Price,
            'breakup': List[QuotationBreakup],
            'ttl': Duration
        }

        self.attribute_map = {
            'price': 'price',
            'breakup': 'breakup',
            'ttl': 'ttl'
        }
        self._price = price
        self._breakup = breakup
        self._ttl = ttl

    @classmethod
    def from_dict(cls, dikt) -> 'Quotation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Quotation of this Quotation.  # noqa: E501
        :rtype: Quotation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def price(self) -> Price:
        """Gets the price of this Quotation.


        :return: The price of this Quotation.
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price: Price):
        """Sets the price of this Quotation.


        :param price: The price of this Quotation.
        :type price: Price
        """

        self._price = price

    @property
    def breakup(self) -> List[QuotationBreakup]:
        """Gets the breakup of this Quotation.


        :return: The breakup of this Quotation.
        :rtype: List[QuotationBreakup]
        """
        return self._breakup

    @breakup.setter
    def breakup(self, breakup: List[QuotationBreakup]):
        """Sets the breakup of this Quotation.


        :param breakup: The breakup of this Quotation.
        :type breakup: List[QuotationBreakup]
        """

        self._breakup = breakup

    @property
    def ttl(self) -> Duration:
        """Gets the ttl of this Quotation.


        :return: The ttl of this Quotation.
        :rtype: Duration
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl: Duration):
        """Sets the ttl of this Quotation.


        :param ttl: The ttl of this Quotation.
        :type ttl: Duration
        """

        self._ttl = ttl
