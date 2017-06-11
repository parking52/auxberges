import unittest
from character_dictionnary import create_the_dict
import numpy as np


class TestCharacterDictionnary(unittest.TestCase):

    def test_create_the_dict(self):

        the_dict = create_the_dict(80)

        self.assertEqual(type(the_dict), np.ndarray)
        self.assertEqual(len(the_dict), 80)
