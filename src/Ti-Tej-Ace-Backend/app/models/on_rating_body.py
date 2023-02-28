# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.context import Context  # noqa: F401,E501
from models.error import Error  # noqa: F401,E501
from models.rating_ack import RatingAck  # noqa: F401,E501


class OnRatingBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context: Context=None, message: RatingAck=None, error: Error=None):  # noqa: E501
        """OnRatingBody - a model defined in Swagger

        :param context: The context of this OnRatingBody.  # noqa: E501
        :type context: Context
        :param message: The message of this OnRatingBody.  # noqa: E501
        :type message: RatingAck
        :param error: The error of this OnRatingBody.  # noqa: E501
        :type error: Error
        """
        self.swagger_types = {
            'context': Context,
            'message': RatingAck,
            'error': Error
        }

        self.attribute_map = {
            'context': 'context',
            'message': 'message',
            'error': 'error'
        }
        self._context = context
        self._message = message
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'OnRatingBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The on_rating_body of this OnRatingBody.  # noqa: E501
        :rtype: OnRatingBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self) -> Context:
        """Gets the context of this OnRatingBody.


        :return: The context of this OnRatingBody.
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context: Context):
        """Sets the context of this OnRatingBody.


        :param context: The context of this OnRatingBody.
        :type context: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def message(self) -> RatingAck:
        """Gets the message of this OnRatingBody.


        :return: The message of this OnRatingBody.
        :rtype: RatingAck
        """
        return self._message

    @message.setter
    def message(self, message: RatingAck):
        """Sets the message of this OnRatingBody.


        :param message: The message of this OnRatingBody.
        :type message: RatingAck
        """

        self._message = message

    @property
    def error(self) -> Error:
        """Gets the error of this OnRatingBody.


        :return: The error of this OnRatingBody.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error: Error):
        """Sets the error of this OnRatingBody.


        :param error: The error of this OnRatingBody.
        :type error: Error
        """

        self._error = error
