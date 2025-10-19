
import unittest
from unittest.mock import patch
from translate_missing.translate_missing import get_missing_keys, remove_extra_keys, translate_and_update

class TestTranslateMissing(unittest.TestCase):

    def test_get_missing_keys(self):
        master = {"a": 1, "b": {"c": 2}}
        target = {"a": 1}
        missing = get_missing_keys(master, target)
        self.assertEqual(missing, {"b": {"c": 2}})

    def test_get_missing_keys_nested(self):
        master = {"a": 1, "b": {"c": 2, "d": 3}}
        target = {"a": 1, "b": {"c": 2}}
        missing = get_missing_keys(master, target)
        self.assertEqual(missing, {"b": {"d": 3}})

    def test_get_missing_keys_no_missing(self):
        master = {"a": 1, "b": {"c": 2}}
        target = {"a": 1, "b": {"c": 2}}
        missing = get_missing_keys(master, target)
        self.assertEqual(missing, {})

    def test_remove_extra_keys(self):
        master = {"a": 1}
        target = {"a": 1, "b": 2}
        remove_extra_keys(master, target)
        self.assertEqual(target, {"a": 1})

    def test_remove_extra_keys_nested(self):
        master = {"a": 1, "b": {"c": 2}}
        target = {"a": 1, "b": {"c": 2, "d": 3}}
        remove_extra_keys(master, target)
        self.assertEqual(target, {"a": 1, "b": {"c": 2}})

    def test_remove_extra_keys_no_extra(self):
        master = {"a": 1, "b": {"c": 2}}
        target = {"a": 1, "b": {"c": 2}}
        remove_extra_keys(master, target)
        self.assertEqual(target, {"a": 1, "b": {"c": 2}})

    @patch('translate_missing.translate_missing.GoogleTranslator')
    def test_translate_and_update(self, MockTranslator):
        mock_translator = MockTranslator.return_value
        mock_translator.translate.side_effect = lambda text: f"{text}-translated"

        missing_keys = {"a": "hello", "b": {"c": "world"}}
        target_data = {}
        lang = "fr"

        translate_and_update(missing_keys, target_data, lang)

        self.assertEqual(target_data, {"a": "hello-translated", "b": {"c": "world-translated"}})
        mock_translator.translate.assert_any_call("hello")
        mock_translator.translate.assert_any_call("world")

if __name__ == '__main__':
    unittest.main()
