# -*- coding: utf-8 -*-

from pyPayNowSg.EMVCoHeaders import EMVCoDataHeader
from pyPayNowSg.EMVCoSerializer import EMVCoSerializer
from pyPayNowSg.PayNowHeaders import PayNowMerchantAccountInfo

class PayNowConfigFactory:
    # Reference: ISO 4217
    CURRENCY_NUMBER = 702
    COUNTRY_CODE = "SG"
    CITY_NAME = "Singapore"
    GUID_NAME = "SG.PAYNOW"
    ADDITIONAL_DATA_TYPE_BILL = 1

    @staticmethod
    def build_payload(
        poi_method=12,
        txn_amount=None,
        merchant_name=None,
        merchant_account_info=None,
        additional_data=None
    ):
        """Creates a list containing headers and values to serialize.
        Note that the default value returned might not be usable!

        Args:
            merchant_account_info (list, optional): A list containing tuples
            describing a merchant account information. Defaults to None. 
            txn_amount (string, optional): Amount to be pre-filled.
            Defaults to None.
            merchant_name (string, optional): Merchant name to display.
            Defaults to None.
            additional_data (string, optional):  A list containing tuples
            describing additional data. Defaults to None.            

        Returns:
            list: A list of tuples with payload data ready for serialization
        """
        merchant_info_string = ""
        if (merchant_account_info != None):
            for data in merchant_account_info:
                merchant_info_string += \
                    EMVCoSerializer.serialize(data[0],data[1])

        extra_data_string = ""
        if (additional_data != None):
            extra_data_string = EMVCoSerializer.serialize(
                additional_data[0][0],
                additional_data[0][1]
            )

        payload = [
            (EMVCoDataHeader.PAYLOAD_FORMAT, "01"),
            (EMVCoDataHeader.POI_METHOD, poi_method),
            (EMVCoDataHeader.MERCHANT_ACCOUNT_INFO, merchant_info_string),
            (EMVCoDataHeader.MCC, "0000"),
            (EMVCoDataHeader.CURRENCY, PayNowConfigFactory.CURRENCY_NUMBER),
            (EMVCoDataHeader.TXN_AMOUNT, txn_amount),
            (EMVCoDataHeader.COUNTRY_CODE, PayNowConfigFactory.COUNTRY_CODE),
            (EMVCoDataHeader.MERCHANT_NAME, merchant_name),
            (EMVCoDataHeader.MERCHANT_CITY, PayNowConfigFactory.CITY_NAME),
            (EMVCoDataHeader.ADDITIONAL_DATA, extra_data_string)
        ]
        return payload

    @staticmethod
    def build_merchant_account_info(
        proxy_type=None,
        proxy_value=None,
        editable_txn=True,
        expiry_date=None
    ):
        """Creates a merchant_account_info object for use with build_payload()

        Args:
            proxy_type (int, optional): Indicates how this QR code is linked.
            Defaults to None. Possible values are:
                0 - mobile number
                1 - unknown (NRIC?)
                2 - UEN
            proxy_value (string, optional): Value specified by proxy_type.
            Defaults to None.
            is_txn_editable (bool, optional): Allow the user to modify the
            transaction amount. Defaults to True.
            expiry_date (string, optional): A date value in either
            YYYYMMDDHHMMSS or YYYYMMDD format, which this QR code is valid
            for scanning until. Specify None to disable this feature.
            Defaults to None.

        Returns:
            list: A list of tuples containing merchant account information.
        """
        account_info = [
            (PayNowMerchantAccountInfo.GUID, PayNowConfigFactory.GUID_NAME),
            (PayNowMerchantAccountInfo.PROXY_TYPE, 2),
            (PayNowMerchantAccountInfo.PROXY_VALUE, proxy_value),
            (PayNowMerchantAccountInfo.EDITABLE_TXN, int(editable_txn)),
            (PayNowMerchantAccountInfo.QR_CODE_EXPIRY, expiry_date)
        ]
        return account_info

    @staticmethod
    def build_additional_data(text=None):
        """Creates an additional data object for use with build_payload()

        Args:
            text (string, optional): Additional data to be used with the QR
            code (typically bill/reference number). Defaults to None.

        Returns:
            list: A list of tuples containing additional data.
        """
        additional_data = [
            (PayNowConfigFactory.ADDITIONAL_DATA_TYPE_BILL, text)
        ]
        return additional_data
