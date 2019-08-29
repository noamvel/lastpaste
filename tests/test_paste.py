import unittest
from pbsrc.paste import Paste


class TestPaste(unittest.TestCase):

    def test_paste_not_normalized(self):
        paste = Paste('test_title', 'test_author', 'test_date', 'test_content')
        self.assertEqual(paste.title, 'test_title', "Title should be 'test_title'")
        self.assertEqual(paste.author, 'test_author', "Author should be 'test_author'")
        self.assertEqual(paste.date.format(), 'test_date', "Date should be 'test_date'")
        self.assertEqual(paste.content, 'test_content', "Content should be 'test_content'")

    def test_paste_normalized_cdt_tz(self):
        paste = Paste(date='Tuesday 27th of August 2019 08:09:20 AM CDT')
        self.assertEqual(paste.date.format(), '2019-08-27 13:09:20+00:00', "Date should be '2019-08-27 13:09:20+00:00'")

    def test_paste_normalized_cst_tz(self):
        paste = Paste(date='Tuesday 27th of August 2019 08:09:20 AM CST')
        self.assertEqual(paste.date.format(), '2019-08-27 14:09:20+00:00', "Date should be '2019-08-27 14:09:20+00:00'")

    def test_paste_normalized_none(self):
        paste = Paste(None, None, None, None)
        self.assertEqual(paste.title, '', "Title should be ''")
        self.assertEqual(paste.author, '', "Author should be ''")
        self.assertEqual(paste.date.format(), '', "Date should be ''")
        self.assertEqual(paste.content, '', "Content should be ''")

    def test_paste_normalized_str_1(self):
        paste = Paste(title='', author='', content='', date='')
        self.assertEqual(paste.title, '', "Title should be ''")
        self.assertEqual(paste.author, '', "Author should be ''")
        self.assertEqual(paste.content, '', "Content should be ''")
        self.assertEqual(paste.date.format(), '', "Date should be ''")

    def test_paste_normalized_str_2(self):
        paste = Paste(title='Untitled', author='a guest', content=' strip ')
        self.assertEqual(paste.title, '', "Title should be ''")
        self.assertEqual(paste.author, '', "Author should be ''")
        self.assertEqual(paste.content, 'strip', "Content should be 'strip'")

    def test_paste_normalized_strip(self):
        paste = Paste(title='Untitled', author='a guest    ', content=' strip ')
        self.assertEqual(paste.title, '', "Title should be ''")
        self.assertEqual(paste.author, '', "Author should be ''")
        self.assertEqual(paste.content, 'strip', "Content should be 'strip'")

    def test_paste_normalized_str_3(self):
        paste = Paste(title='Unknown', author='Unknown')
        self.assertEqual(paste.title, '', "Title should be ''")
        self.assertEqual(paste.author, '', "Author should be ''")


if __name__ == '__main__':
    unittest.main()
