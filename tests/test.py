import os, sys
import unittest

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../src/pyPayNowSg')))

from pyPayNowSg import *

# Woodbridge Hospital Charity Fund
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

        result = PayNowSerializer.serialize("NATIONAL HEALTHCARE GRO", merchant_info)
        self.assertEqual(result, TEST_CODE_1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPayload)
    unittest.TextTestRunner(verbosity=2).run(suite)

