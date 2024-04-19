"""
To execute, run (from directory interpol_utils):
python -m unittest tests.test_interpolate -v

(Overall getting source imports to work with unittest is a mess, see e.g.
https://stackoverflow.com/questions/62026129/python-adding-unit-test-inside-package,
https://stackoverflow.com/questions/24210651/importing-in-init-py-to-a-unittest-package#24211483)
"""

import os
from unittest import TestCase
from src.interpolate import interpolate

datadir = "tests/testdata"
expected_text = "This is a plain-text file expecting to be passed a variable called country. Here it is: Nicaragua."

class TestInterpolate(TestCase):
    def test_text(self):
        file = os.path.join(os.getcwd(), datadir, "sample-text")
        country = "Nicaragua"
        formatted = interpolate(file, country = country)  
        self.assertEqual(formatted, expected_text)

