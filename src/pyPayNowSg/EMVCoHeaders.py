# -*- coding: utf-8 -*-

class EMVCoDataHeader:
    PAYLOAD_FORMAT = 0
    POI_METHOD = 1
    MERCHANT_ACCOUNT_INFO = 26
    MCC = 52
    CURRENCY = 53
    TXN_AMOUNT = 54
    COUNTRY_CODE = 58
    MERCHANT_NAME = 59
    MERCHANT_CITY = 60
    ADDITIONAL_DATA = 62
    CRC = 63

class EMVCoMerchantAccountInfo:
    GUID = 0
