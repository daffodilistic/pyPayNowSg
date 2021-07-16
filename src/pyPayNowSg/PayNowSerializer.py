# -*- coding: utf-8 -*-

import sys
import crcmod

from pyPayNowSg.EMVCoHeaders import EMVCoDataHeader
from pyPayNowSg.EMVCoSerializer import EMVCoSerializer
from pyPayNowSg.PayNowConfigFactory import PayNowConfigFactory

class PayNowSerializer:
    @staticmethod
    def serialize(merchant_name, merchant_info, amount=None, additional_info=None):
        """Serializes 

        Args:
            amount (string): Amount to be pre-filled. Defaults to None.
            name (string): Name of merchant to be displayed.
            merchant_info (list): A list of tuples generated from
            PayNowConfigFactory.build_merchant_account_info().
            additional_info (list, optional): A list of tuples generated from
            PayNowConfigFactory.build_additional_data(). Defaults to None.

        Returns:
            string: A PayNow string which can be converted to a QR code.
        """
        payload = PayNowConfigFactory.build_payload(
            poi_method=11,
            txn_amount=amount,
            merchant_name=merchant_name,
            merchant_account_info=merchant_info,
            additional_data=additional_info
        )
        payload_string = ""
        for data in payload:
            payload_string += EMVCoSerializer.serialize(data[0],data[1])

        crc16 = crcmod.mkCrcFun(0x11021, rev=False)
        plaintext = payload_string + str(EMVCoDataHeader.CRC) + "04"
        crcmod_plaintext = PayNowSerializer.__crcmod_string(plaintext)
        checksum = '{:04X}'.format(crc16(crcmod_plaintext)) 
        output = plaintext + checksum
        return output

    @staticmethod
    def __crcmod_string(source):
        """Converts a string to be compatible for use with crcmod functions

        Args:
            source (string): A native string type on either Python 2 or 3

        Returns:
            string: A string compatible with crcmod.mkCrcFun() function
        """
        unicode_type = u''.__class__
        PY3 = sys.version_info[0] == 3
        if PY3:
            unicode_type = str

        if isinstance(source, unicode_type):
            # Note that EMVCo specs only allows ASCII
            source = source.encode("ascii", "strict")
        return source

