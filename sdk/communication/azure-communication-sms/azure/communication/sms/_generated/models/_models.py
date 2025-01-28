# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class SendMessageRequest(msrest.serialization.Model):
    """Represents the properties of a send message request.

    All required parameters must be populated in order to send to Azure.

    :param from_property: Required. The sender's phone number in E.164 format that is owned by the
     authenticated account.
    :type from_property: str
    :param sms_recipients: Required. The recipient's phone number in E.164 format. In this version,
     a minimum of 1 and upto 100 recipients in the list are supported.
    :type sms_recipients: list[~azure.communication.sms.models.SmsRecipient]
    :param message: Required. The contents of the message that will be sent to the recipient. The
     allowable content is defined by RFC 5724.
    :type message: str
    :param sms_send_options: Optional configuration for sending SMS messages.
    :type sms_send_options: ~azure.communication.sms.models.SmsSendOptions
    """

    _validation = {
        "from_property": {"required": True},
        "sms_recipients": {"required": True},
        "message": {"required": True, "max_length": 2048, "min_length": 0},
    }

    _attribute_map = {
        "from_property": {"key": "from", "type": "str"},
        "sms_recipients": {"key": "smsRecipients", "type": "[SmsRecipient]"},
        "message": {"key": "message", "type": "str"},
        "sms_send_options": {"key": "smsSendOptions", "type": "SmsSendOptions"},
    }

    def __init__(self, **kwargs):
        super(SendMessageRequest, self).__init__(**kwargs)
        self.from_property = kwargs["from_property"]
        self.sms_recipients = kwargs["sms_recipients"]
        self.message = kwargs["message"]
        self.sms_send_options = kwargs.get("sms_send_options", None)


class SmsRecipient(msrest.serialization.Model):
    """Recipient details for sending SMS messages.

    All required parameters must be populated in order to send to Azure.

    :param to: Required. The recipient's phone number in E.164 format.
    :type to: str
    :param repeatability_request_id: If specified, the client directs that the request is
     repeatable; that is, the client can make the request multiple times with the same
     Repeatability-Request-ID and get back an appropriate response without the server executing the
     request multiple times. The value of the Repeatability-Request-ID is an opaque string
     representing a client-generated, 36-character hexadecimal case-insensitive encoding of a UUID
     (GUID), identifier for the request.
    :type repeatability_request_id: str
    :param repeatability_first_sent: MUST be sent by clients to specify that a request is
     repeatable. Repeatability-First-Sent is used to specify the date and time at which the request
     was first created.eg- Tue, 26 Mar 2019 16:06:51 GMT.
    :type repeatability_first_sent: str
    """

    _validation = {
        "to": {"required": True},
    }

    _attribute_map = {
        "to": {"key": "to", "type": "str"},
        "repeatability_request_id": {"key": "repeatabilityRequestId", "type": "str"},
        "repeatability_first_sent": {"key": "repeatabilityFirstSent", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SmsRecipient, self).__init__(**kwargs)
        self.to = kwargs["to"]
        self.repeatability_request_id = kwargs.get("repeatability_request_id", None)
        self.repeatability_first_sent = kwargs.get("repeatability_first_sent", None)


class SmsSendOptions(msrest.serialization.Model):
    """Optional configuration for sending SMS messages.

    All required parameters must be populated in order to send to Azure.

    :param enable_delivery_report: Required. Enable this flag to receive a delivery report for this
     message on the Azure Resource EventGrid.
    :type enable_delivery_report: bool
    :param tag: Use this field to provide metadata that will then be sent back in the corresponding
     Delivery Report.
    :type tag: str
    """

    _validation = {
        "enable_delivery_report": {"required": True},
    }

    _attribute_map = {
        "enable_delivery_report": {"key": "enableDeliveryReport", "type": "bool"},
        "tag": {"key": "tag", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SmsSendOptions, self).__init__(**kwargs)
        self.enable_delivery_report = kwargs["enable_delivery_report"]
        self.tag = kwargs.get("tag", None)


class SmsSendResponse(msrest.serialization.Model):
    """Response for a successful or multi status send Sms request.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: list[~azure.communication.sms.models.SmsSendResponseItem]
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[SmsSendResponseItem]"},
    }

    def __init__(self, **kwargs):
        super(SmsSendResponse, self).__init__(**kwargs)
        self.value = kwargs["value"]


class SmsSendResponseItem(msrest.serialization.Model):
    """Response for a single recipient.

    All required parameters must be populated in order to send to Azure.

    :param to: Required. The recipient's phone number in E.164 format.
    :type to: str
    :param message_id: The identifier of the outgoing Sms message. Only present if message
     processed.
    :type message_id: str
    :param http_status_code: Required. HTTP Status code.
    :type http_status_code: int
    :param repeatability_result: The result of a repeatable request with one of the
     case-insensitive values accepted or rejected. Possible values include: "accepted", "rejected".
    :type repeatability_result: str or
     ~azure.communication.sms.models.SmsSendResponseItemRepeatabilityResult
    :param successful: Required. Indicates if the message is processed successfully or not.
    :type successful: bool
    :param error_message: Optional error message in case of 4xx/5xx/repeatable errors.
    :type error_message: str
    """

    _validation = {
        "to": {"required": True},
        "http_status_code": {"required": True},
        "successful": {"required": True},
    }

    _attribute_map = {
        "to": {"key": "to", "type": "str"},
        "message_id": {"key": "messageId", "type": "str"},
        "http_status_code": {"key": "httpStatusCode", "type": "int"},
        "repeatability_result": {"key": "repeatabilityResult", "type": "str"},
        "successful": {"key": "successful", "type": "bool"},
        "error_message": {"key": "errorMessage", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SmsSendResponseItem, self).__init__(**kwargs)
        self.to = kwargs["to"]
        self.message_id = kwargs.get("message_id", None)
        self.http_status_code = kwargs["http_status_code"]
        self.repeatability_result = kwargs.get("repeatability_result", None)
        self.successful = kwargs["successful"]
        self.error_message = kwargs.get("error_message", None)
