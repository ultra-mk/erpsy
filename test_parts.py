import unittest
import parts


class PartTest(unittest.TestCase):

    def test_part_num_no_format(self):
        part = parts.Part()
        re = r'^[0-9]{8}$'
        self.assertRegex(part.number(), re)

    def test_part_num_style_1(self):
        part = parts.Part()
        re = r'^[0-9]{4}$'
        self.assertRegex(part.number(style='####'), re)

    def test_part_num_style_2(self):
        part = parts.Part()
        re = r'^[0-9]{7}$'
        self.assertRegex(part.number(style='#######'), re)

    def test_part_num_style_3(self):
        part = parts.Part()
        re = r'^[A-Z]{2}[0-9]{2}$'
        self.assertRegex(part.number(style='AA##'), re)

    def test_name(self):
        part = parts.Part()
        self.assertEqual(True, isinstance(part.name(), str))

    def test_name_len(self):
        part = parts.Part()
        self.assertTrue(1 < len(part.name()) < 100)


if __name__ == '__main__':
    unittest.main()
