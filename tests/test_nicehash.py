from unittest import main, TestCase

import naxhash.nicehash as nh
from naxhash.settings import DEFAULT_SETTINGS
from naxhash.damen import DONATE_ADDRESS


class TestNHMultialgo(TestCase):

    def setUp(self):
        self.settings = DEFAULT_SETTINGS
        self.settings['nicehash']['region'] = 'eu'

    def test_payrate(self):
        mbtc_per_hash = nh.simplemultialgo_info(self.settings)
        self.assertGreater(mbtc_per_hash['cryptonight'], 0.0)

    def test_stratum(self):
        stratums = nh.stratums(self.settings)
        self.assertIn('cryptonight.eu.nicehash.com', stratums['cryptonight'])


if __name__ == '__main__':
    main()

