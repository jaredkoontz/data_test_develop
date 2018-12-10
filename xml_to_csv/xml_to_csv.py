import csv
import uuid

from lxml import etree


class XmlToCSVHelper(object):
    """
    Simple helper class that takes in an xml documents and outputs a csv documents

    also handles filtering and sorting, but this can easily be extended to other classes
    """

    def __init__(self, xml_file_url, data_filter, sort):
        # Parse the remote XML file into an lxml tree
        self.xml_tree = etree.parse(xml_file_url)
        self.filter = data_filter
        self.sort = sort

    def _filter_xml(self, criteria):
        """
        use the xml module for initial filtering
        """
        return self.xml_tree.xpath(criteria)

    @staticmethod
    def _extract_xml_fields(xml_data, fieldnames):
        """

        :param xml_data: the xml to parse
        :param fieldnames: wanted fields names
        :return: the filtered data
        """
        rows = []

        for xml_row in xml_data:
            row = dict()

            for path, field_name in fieldnames.iteritems():
                found = xml_row.find(path)
                if found is None:
                    # move on we do not want this row
                    continue

                # find if this path has children
                sub_elements = found.xpath('*[count(child::*) = 0]')

                if sub_elements:
                    # truncate to 200 chars
                    row[field_name] = ','.join([element.text[:200] for element in sub_elements])
                elif found.text:
                    # truncate to 200 chars
                    row[field_name] = found.text[:200]
            rows.append(row)

        return rows

    @staticmethod
    def _write_csv(fieldnames, rows, filename):
        """

        :param fieldnames: fields to write
        :param rows: the data to write
        :param filename: name of the output file
        :return:
        """
        filename = filename if filename.endswith('.csv') else '{}.csv'.format(filename)
        with open(filename, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
            csv_file.close()
        print "data written to {}".format(filename)

    def convert_and_filter(self, wanted_fields, filename=str(uuid.uuid4())):
        """
        :param wanted_fields: the fields we are filtering
        :param filename: the name of the output file. defaults to a uuid

        :return:
        """

        filtered_data = self._filter_xml(self.filter)
        filtered_data.sort(key=self.sort, reverse=False)
        rows = self._extract_xml_fields(filtered_data, wanted_fields)
        self._write_csv(wanted_fields.values(), rows, filename)
