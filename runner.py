import datetime
from collections import OrderedDict

from xml_to_csv.xml_to_csv import XmlToCSVHelper

if __name__ == '__main__':
    # input data
    feed_url = 'http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml'

    # mapping of xml fields to csv fields names
    output_fields = OrderedDict([
        ('ListingDetails/MlsId', 'MlsId'),
        ('ListingDetails/MlsName', 'MlsName'),
        ('ListingDetails/DateListed', 'DateListed'),
        ('Location/StreetAddress', 'StreetAddress'),
        ('ListingDetails/Price', 'Price'),
        ('BasicDetails/Bedrooms', 'Bedrooms'),
        ('BasicDetails/Bathrooms', 'Bathrooms'),
        ('BasicDetails/FullBathrooms', 'FullBathrooms'),
        ('BasicDetails/HalfBathrooms', 'HalfBathrooms'),
        ('BasicDetails/ThreeQuarterBathrooms', 'ThreeQuarterBathrooms'),
        ('RichDetails/Appliances', 'Appliances'),  # comma joined
        ('RichDetails/Rooms', 'Rooms'),  # comma joined
        ('BasicDetails/Description', 'Description'),  # only the first 200 characters
    ])

    wanted_filter = (
        "//Listing[starts-with(ListingDetails/DateListed, '2016') and contains(BasicDetails/Description, ' and ')]"
    )

    # sort by date listed
    wanted_sort = lambda x: datetime.datetime.strptime(
        x.findtext('ListingDetails/DateListed'), '%Y-%m-%d %H:%M:%S')

    # init the class
    helper = XmlToCSVHelper(feed_url, wanted_filter, wanted_sort)
    # convert the xml
    helper.convert_and_filter(output_fields)
