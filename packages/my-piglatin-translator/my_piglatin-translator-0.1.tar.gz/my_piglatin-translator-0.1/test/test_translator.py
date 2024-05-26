import unittest
from piglatin.translator import translate_word, translate_sentence

class TestPigLatin(unittest.TestCase):
    def test_translate_word(self):
        self.assertEqual(translate_word("hello"), "ellohay")
        self.assertEqual(translate_word("apple"), "appleway")
        self.assertEqual(translate_word("string"), "ingstray")

    def test_translate_sentence(self):
        self.assertEqual(translate_sentence("hello world"), "ellohay orldway")
        self.assertEqual(translate_sentence("I am a student"), "Iway amway away udentstay")

if __name__ == "__main__":
    unittest.main()
