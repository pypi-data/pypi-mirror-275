import unittest
import tempfile
from pathlib import Path
import oceansoundscape
from oceansoundscape.raven import BLEDParser
from oceansoundscape.spectrogram import conf
from oceansoundscape import testdata

import importlib.resources as resources

class TestRaven(unittest.TestCase):
    def test_bled_parser(self):
        max_samples = 10 * 60 * 2e3
        bled_path = resources.files('oceansoundscape.testdata').joinpath("MARS-20150910T000000Z-2kHz.wav.Table01.txt")
        print(f"bled_file: {bled_path}")
        parser = BLEDParser(bled_path, conf.CONF_DICT['blueA'], max_samples=max_samples, sampling_rate=2e3)
        df_subset = parser.data[0:1]
        actual = df_subset.to_dict()
        print(f"Actual {actual}")
        expected = {'Selection': {0: 2},
                    'Classification': {0: 'baf'},
                    'Begin Time (s)': {0: 161.79},
                    'End Time (s)': {0: 180.99},
                    'call_start': {0: 317780.0},
                    'call_end': {0: 367780.0},
                    'image_filename': {0: '20150910T000241_baf.323580.361980.sel.02.ch01.spectrogram.jpg'},
                    'has_label': {0: True}}

        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
