import datetime
import unittest
from collections import OrderedDict
from io import BytesIO

import mock

from xml_to_csv.xml_to_csv import XmlToCSVHelper

wanted_filter = (
    "//Listing[starts-with(ListingDetails/DateListed, '2016') and contains(BasicDetails/Description, ' and ')]"
)

# sort by date listed
wanted_sort = lambda x: datetime.datetime.strptime(
    x.findtext('ListingDetails/DateListed'), '%Y-%m-%d %H:%M:%S')

output_fields = OrderedDict([
    ('ListingDetails/MlsId', 'MlsId'),
    ('ListingDetails/MlsName', 'MlsName'),
])


class TestXmlToCsv(unittest.TestCase):

    def setUp(self):
        xml_url = './small_xml_data.xml'
        self.xml_parser = XmlToCSVHelper(xml_url, wanted_filter, wanted_sort)

    def test_extract(self):
        result = self.xml_parser._filter_xml(wanted_filter)
        rows = self.xml_parser._extract_xml_fields(result, output_fields)
        self.assertEqual(len(rows), 1)
        for fieldname in output_fields.values():
            self.assertIn(fieldname, rows[0])

    def test_filter(self):
        result = self.xml_parser._filter_xml(wanted_filter)
        # There are 3 rows in the test data, and only 1 matches the query
        self.assertEqual(len(result), 1)

    def test_write_csv(self):
        result = self.xml_parser._filter_xml(wanted_filter)
        rows = self.xml_parser._extract_xml_fields(result, output_fields)
        with mock.patch('xml_to_csv.open', mock.mock_open(read_data=BytesIO(''))):
            self.xml_parser._write_csv(output_fields.values(), rows, 'filename')
