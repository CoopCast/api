import urllib.request
import io
from lxml import etree

# VNGRD podcast RSS feed
rss = "https://feeds.soundcloud.com/users/soundcloud:users:780914110/sounds.rss"
resp = urllib.request.urlopen(rss)

# construct a file-like string of the data
data = resp.read()

if(data[0] == 10): # if first char is newline
    fdata = io.BytesIO(data[1:])
else:
    fdata = io.BytesIO(data)

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(fdata, parser)

# make pretty
tree.write('vngrd.xml', pretty_print=True)
