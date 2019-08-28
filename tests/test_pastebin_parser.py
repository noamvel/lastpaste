import unittest
from pastebin_parser import parse_archive, parse_paste


class TestParser(unittest.TestCase):

    def test_parse_archive_success(self):
        with open('txt/test_archive.txt', 'r') as reader:
            text = reader.read()
        self.assertEqual(len(parse_archive(text)), 21, "21 hrefs expected")

    def test_parse_archive_missing_href(self):
        with open('txt/test_archive_missing_href.txt', 'r') as reader:
            text = reader.read()
        self.assertEqual(len(parse_archive(text)), 20, "20 hrefs expected")

    def test_parse_archive_missing_table(self):
        with open('txt/test_archive_missing_table.txt', 'r') as reader:
            text = reader.read()
        self.assertEqual(len(parse_archive(text)), 0, "0 hrefs expected")

    def test_parse_paste_success(self):
        with open('txt/test_single_paste.txt', 'r') as reader:
            text = reader.read()
        self.assertEqual(parse_paste(text).title, 'Homework2_vsokolov', "Title should be 'Homework2_vsokolov'")
        self.assertEqual(parse_paste(text).author, '', "Author should be ''")
        self.assertEqual(parse_paste(text).date.format(), '2019-08-27 13:09:20+00:00', "Date should be '2019-08-27 13:09:20+00:00'")
        self.assertEqual(parse_paste(text).content, 'Test Text', "Content should be 'Test Text'")

    def test_parse_paste_None(self):
        with open('txt//test_single_paste.txt', 'r') as reader:
            text = reader.read()
        self.assertEqual(parse_paste(None), None, "Paste should be 'None'")


if __name__ == '__main__':
    unittest.main()
