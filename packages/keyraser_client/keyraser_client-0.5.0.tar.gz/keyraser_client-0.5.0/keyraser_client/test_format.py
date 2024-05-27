import unittest

from keyraser_client.format import CsvFormat, IdFormat, NdjsonFormat, SingleFormat


class TestIdFormat(unittest.TestCase):

    def test_default_contains_nothing(self):
        params = IdFormat.DEFAULT.as_cli_params()
        self.assertEqual([], params)

    def test_string_utf8_format(self):
        params = IdFormat.STRING_UTF8.as_cli_params()
        self.assertEqual(['-idFormat', 'STRING-UTF8'], params)

    def test_hex_format(self):
        params = IdFormat.HEX.as_cli_params()
        self.assertEqual(['-idFormat', 'HEX'], params)


class TestCsvFormat(unittest.TestCase):

    def test_default_contains_only_format(self):
        csv = CsvFormat()
        params = csv.as_cli_params()
        self.assertEqual(['csv'], params)

    def test_id_column_specified(self):
        csv = CsvFormat(id_column="first_col")
        params = csv.as_cli_params()
        self.assertEqual(['csv', '-id', 'first_col'], params)

    def test_id_format_specified(self):
        csv = CsvFormat(id_format=IdFormat.HEX)
        params = csv.as_cli_params()
        self.assertEqual(['csv', '-idFormat', 'HEX'], params)

    def test_separator_specified(self):
        csv = CsvFormat(separator=',')
        params = csv.as_cli_params()
        self.assertEqual(['csv', '-separator', ','], params)

    def test_enclosing_specified(self):
        csv = CsvFormat(enclosing='"')
        params = csv.as_cli_params()
        self.assertEqual(['csv', '-enclosing', '"'], params)

    def test_contains_header_specified(self):
        csv = CsvFormat(contains_header=True)
        params = csv.as_cli_params()
        self.assertEqual(['csv', '-header'], params)


class TestNdjsonFormat(unittest.TestCase):

    def test_default_contains_only_format(self):
        ndjson = NdjsonFormat()
        params = ndjson.as_cli_params()
        self.assertEqual(['ndjson'], params)

    def test_id_column_specified(self):
        ndjson = NdjsonFormat(id_property="id_prop")
        params = ndjson.as_cli_params()
        self.assertEqual(['ndjson', '-id', 'id_prop'], params)

    def test_id_format_specified(self):
        ndjson = NdjsonFormat(id_format=IdFormat.HEX)
        params = ndjson.as_cli_params()
        self.assertEqual(['ndjson', '-idFormat', 'HEX'], params)


class TestSingleFormat(unittest.TestCase):

    def test_always_requires_an_entity_id(self):
        with self.assertRaisesRegex(TypeError, ''):
            SingleFormat()

    def test_format_args_contain_entity_id(self):
        single = SingleFormat('my-entity')
        params = single.as_cli_params()
        self.assertEqual(['single', '-id', 'my-entity'], params)

    def test_id_format_specified(self):
        single = SingleFormat('my-entity', id_format=IdFormat.HEX)
        params = single.as_cli_params()
        self.assertEqual(['single', '-id', 'my-entity', '-idFormat', 'HEX'], params)


if __name__ == '__main__':
    unittest.main()
