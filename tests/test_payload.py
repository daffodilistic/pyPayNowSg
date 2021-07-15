import os, sys
import unittest

import qrcode
from PIL import Image

from pyPayNowSg import PayNowConfigFactory, PayNowSerializer

# Woodbridge Hospital Charity Fund
# We're using this as a sample because it is shown on their website
# at https://www.imh.com.sg/page.aspx?id=120, and in case anyone tries
# to test a payment, the money goes to a good cause
TEST_CODE_1 = "00020101021126400009SG.PAYNOW010120213200002150HWCF030115204000053037025802SG5923NATIONAL HEALTHCARE GRO6009Singapore6304DF3F"

class TestPayload(unittest.TestCase):
    def test_payload(self):
        """
        Test serializer output matches TEST_CODE_1
        """
        merchant_info = PayNowConfigFactory.build_merchant_account_info(
            2,
            "200002150HWCF",
            True
        )

        result = PayNowSerializer.serialize(
            "NATIONAL HEALTHCARE GRO",
            merchant_info
        )
        self.assertEqual(result, TEST_CODE_1)

        img = qrcode.make(result)
        img.save("test_generate_image.png")

        img = Image.open('test_generate_image.png', 'r')

        img_w, img_h = img.size
        logo = Image.radial_gradient("L")
        logo = logo.resize((192, 192))

        bg_w, bg_h = logo.size
        offset = ((img_w - bg_w) // 2, (img_h - bg_h) // 2)
        img.paste(logo, offset)
        img.save('out.png')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPayload)
    unittest.TextTestRunner(verbosity=2).run(suite)