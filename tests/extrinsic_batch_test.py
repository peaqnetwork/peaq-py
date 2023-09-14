import unittest
import sys

sys.path.append('./')

from substrateinterface import SubstrateInterface, Keypair
from tests.utils import PARACHAIN_WS_URL
from peaq.utils import get_account_balance
from peaq.sudo_extrinsic import fund
from peaq.extrinsic import transfer


class TestExtrinsic(unittest.TestCase):
    def setUp(self):
        self.substrate = SubstrateInterface(url=PARACHAIN_WS_URL)
        self.kp_src = Keypair.create_from_uri('//Alice')
        self.num = 500 * 100

    def test_fund(self):
        kp_dst = Keypair.create_from_mnemonic(Keypair.generate_mnemonic())

        bl_hash = fund(self.substrate, self.kp_src, kp_dst, self.num)
        self.assertTrue(bl_hash, f'fund failed {bl_hash}')
        self.assertEqual(get_account_balance(self.substrate, kp_dst.ss58_address), self.num)

    def test_transfer(self):
        kp_dst = Keypair.create_from_mnemonic(Keypair.generate_mnemonic())

        bl_hash = transfer(self.substrate, self.kp_src, kp_dst, self.num)
        self.assertTrue(bl_hash, f'fund failed {bl_hash}')
        self.assertEqual(get_account_balance(self.substrate, kp_dst.ss58_address), self.num)
