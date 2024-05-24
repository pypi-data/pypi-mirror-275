import unittest
from data_cleaner_byzahid.text_cleaner import TextCleaner

class TestTextCleaner(unittest.TestCase):

    def setUp(self):
        self.text = "Hello World! This is a test sentence with numbers 12345 and special characters #@$%."
        self.cleaner = TextCleaner(self.text)

    def test_lowercase(self):
        result = self.cleaner.lowercase()
        self.assertEqual(result, "hello world! this is a test sentence with numbers 12345 and special characters #@$%.")

    def test_remove_punctuation(self):
        self.cleaner.lowercase()
        result = self.cleaner.remove_punctuation()
        self.assertEqual(result, "hello world this is a test sentence with numbers 12345 and special characters ")

    def test_remove_numbers(self):
        self.cleaner.lowercase()
        self.cleaner.remove_punctuation()
        result = self.cleaner.remove_numbers()
        self.assertEqual(result, "hello world this is a test sentence with numbers  and special characters ")

    def test_remove_stopwords(self):
        self.cleaner.lowercase()
        self.cleaner.remove_punctuation()
        self.cleaner.remove_numbers()
        result = self.cleaner.remove_stopwords().strip()
        self.assertEqual(result, "hello world test sentence numbers special characters")

    def test_stem_text(self):
        self.cleaner.lowercase()
        self.cleaner.remove_punctuation()
        self.cleaner.remove_numbers()
        self.cleaner.remove_stopwords()
        result = self.cleaner.stem_text().strip()
        self.assertEqual(result, "hello world test sentenc number special charact")

    def test_lemmatize_text(self):
        self.cleaner.lowercase()
        self.cleaner.remove_punctuation()
        self.cleaner.remove_numbers()
        self.cleaner.remove_stopwords()
        result = self.cleaner.lemmatize_text().strip()
        self.assertEqual(result, "hello world test sentence number special character")

    def test_remove_whitespace(self):
        self.cleaner.lowercase()
        self.cleaner.remove_punctuation()
        self.cleaner.remove_numbers()
        self.cleaner.remove_stopwords()
        self.cleaner.lemmatize_text()
        result = self.cleaner.remove_whitespace()
        self.assertEqual(result, "hello world test sentence number special character")

    def test_remove_special_characters(self):
        self.cleaner.lowercase()
        self.cleaner.remove_punctuation()
        self.cleaner.remove_numbers()
        self.cleaner.remove_stopwords()
        self.cleaner.lemmatize_text()
        self.cleaner.remove_whitespace()
        result = self.cleaner.remove_special_characters()
        self.assertEqual(result, "hello world test sentence number special character")

if __name__ == '__main__':
    unittest.main()
