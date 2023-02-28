# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.category import Category  # noqa: F401,E501
from models.descriptor import Descriptor  # noqa: F401,E501
from models.fulfillment import Fulfillment  # noqa: F401,E501
from models.item import Item  # noqa: F401,E501
from models.offer import Offer  # noqa: F401,E501
from models.payment import Payment  # noqa: F401,E501
from models.provider import Provider  # noqa: F401,E501
from models.tags import Tags  # noqa: F401,E501


class Intent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, descriptor: Descriptor=None, provider: Provider=None, fulfillment: Fulfillment=None, payment: Payment=None, category: Category=None, offer: Offer=None, item: Item=None, tags: Tags=None):  # noqa: E501
        """Intent - a model defined in Swagger

        :param descriptor: The descriptor of this Intent.  # noqa: E501
        :type descriptor: Descriptor
        :param provider: The provider of this Intent.  # noqa: E501
        :type provider: Provider
        :param fulfillment: The fulfillment of this Intent.  # noqa: E501
        :type fulfillment: Fulfillment
        :param payment: The payment of this Intent.  # noqa: E501
        :type payment: Payment
        :param category: The category of this Intent.  # noqa: E501
        :type category: Category
        :param offer: The offer of this Intent.  # noqa: E501
        :type offer: Offer
        :param item: The item of this Intent.  # noqa: E501
        :type item: Item
        :param tags: The tags of this Intent.  # noqa: E501
        :type tags: Tags
        """
        self.swagger_types = {
            'descriptor': Descriptor,
            'provider': Provider,
            'fulfillment': Fulfillment,
            'payment': Payment,
            'category': Category,
            'offer': Offer,
            'item': Item,
            'tags': Tags
        }

        self.attribute_map = {
            'descriptor': 'descriptor',
            'provider': 'provider',
            'fulfillment': 'fulfillment',
            'payment': 'payment',
            'category': 'category',
            'offer': 'offer',
            'item': 'item',
            'tags': 'tags'
        }
        self._descriptor = descriptor
        self._provider = provider
        self._fulfillment = fulfillment
        self._payment = payment
        self._category = category
        self._offer = offer
        self._item = item
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> 'Intent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Intent of this Intent.  # noqa: E501
        :rtype: Intent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def descriptor(self) -> Descriptor:
        """Gets the descriptor of this Intent.


        :return: The descriptor of this Intent.
        :rtype: Descriptor
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor: Descriptor):
        """Sets the descriptor of this Intent.


        :param descriptor: The descriptor of this Intent.
        :type descriptor: Descriptor
        """

        self._descriptor = descriptor

    @property
    def provider(self) -> Provider:
        """Gets the provider of this Intent.


        :return: The provider of this Intent.
        :rtype: Provider
        """
        return self._provider

    @provider.setter
    def provider(self, provider: Provider):
        """Sets the provider of this Intent.


        :param provider: The provider of this Intent.
        :type provider: Provider
        """

        self._provider = provider

    @property
    def fulfillment(self) -> Fulfillment:
        """Gets the fulfillment of this Intent.


        :return: The fulfillment of this Intent.
        :rtype: Fulfillment
        """
        return self._fulfillment

    @fulfillment.setter
    def fulfillment(self, fulfillment: Fulfillment):
        """Sets the fulfillment of this Intent.


        :param fulfillment: The fulfillment of this Intent.
        :type fulfillment: Fulfillment
        """

        self._fulfillment = fulfillment

    @property
    def payment(self) -> Payment:
        """Gets the payment of this Intent.


        :return: The payment of this Intent.
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment: Payment):
        """Sets the payment of this Intent.


        :param payment: The payment of this Intent.
        :type payment: Payment
        """

        self._payment = payment

    @property
    def category(self) -> Category:
        """Gets the category of this Intent.


        :return: The category of this Intent.
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category: Category):
        """Sets the category of this Intent.


        :param category: The category of this Intent.
        :type category: Category
        """

        self._category = category

    @property
    def offer(self) -> Offer:
        """Gets the offer of this Intent.


        :return: The offer of this Intent.
        :rtype: Offer
        """
        return self._offer

    @offer.setter
    def offer(self, offer: Offer):
        """Sets the offer of this Intent.


        :param offer: The offer of this Intent.
        :type offer: Offer
        """

        self._offer = offer

    @property
    def item(self) -> Item:
        """Gets the item of this Intent.


        :return: The item of this Intent.
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item: Item):
        """Sets the item of this Intent.


        :param item: The item of this Intent.
        :type item: Item
        """

        self._item = item

    @property
    def tags(self) -> Tags:
        """Gets the tags of this Intent.


        :return: The tags of this Intent.
        :rtype: Tags
        """
        return self._tags

    @tags.setter
    def tags(self, tags: Tags):
        """Sets the tags of this Intent.


        :param tags: The tags of this Intent.
        :type tags: Tags
        """

        self._tags = tags
