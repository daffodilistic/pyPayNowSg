# -*- coding: utf-8 -*-

from pyPayNowSg.EMVCoHeaders import EMVCoMerchantAccountInfo

class PayNowMerchantAccountInfo(EMVCoMerchantAccountInfo):
    PROXY_TYPE = 1
    PROXY_VALUE = 2
    EDITABLE_TXN = 3
    QR_CODE_EXPIRY = 4