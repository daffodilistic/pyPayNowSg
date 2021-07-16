# -*- coding: utf-8 -*-

class EMVCoSerializer:
    @staticmethod
    def serialize(header_id, value):
        """Serializes a given value and header ID to a string

        Args:
            header_id (int): Header ID of the data object
            value (string): Data value

        Returns:
            string: Serialized string in the format [header][data length][data]
        """
        if ((value != None) & (value != "")):
            packed_data = "{:02}{:02}{}".format(
                header_id,
                len(str(value)),
                value
            )
            return packed_data
        else:
            return ""
