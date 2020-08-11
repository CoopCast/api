import urllib.request
import io
from lxml import etree


def rss_to_xml(rss_url):
    '''Downloads RSS file and returns xml ElementTree'''

    resp = urllib.request.urlopen(rss_url)

    # construct a file-like string of the data
    data = resp.read()

    # in WordPress RSS, the first line is newline
    # the XML parser doesn't like that so remove it
    if(data[0] == ord('\n')):
        fdata = io.BytesIO(data[1:])
    else:
        fdata = io.BytesIO(data)

    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(fdata, parser)

    return etree.tostring(tree)
