from utils.xml_utils import *
from lxml import etree
import os

TEST_XML_DIR = os.path.join(os.environ['API_DIR'], 'tests', 'test_xml')


def test_rss_to_xml():
    # Soundcloud RSS
    tbs_rss = 'https://theblockchainsocialist.com/feed/'

    # WordPress RSS
    vngrd_rss = 'https://feeds.soundcloud.com/users/soundcloud:users:780914110/sounds.rss'

    # Fans.fm RSS
    antifada_rss = 'https://feeds.fans.fm/105.xml'

    # Add other RSS tests as you come across them to be thorough
    # I think 3 are fine for now

    # test rss_to_xml functions
    tbs_tree = rss_to_xml(tbs_rss)
    vngrd_tree = rss_to_xml(vngrd_rss)
    antifada_tree = rss_to_xml(antifada_rss)

    tbs_test_xml = open(os.path.join(TEST_XML_DIR, 'tbs.xml'))
    vngrd_test_xml = open(os.path.join(TEST_XML_DIR, 'vngrd.xml'))
    antifada_test_xml = open(os.path.join(TEST_XML_DIR, 'antifada.xml'))

    # control group
    parser = etree.XMLParser(remove_blank_text=True)
    test_tbs_tree = etree.parse(tbs_test_xml, parser)
    test_vngrd_tree = etree.parse(vngrd_test_xml, parser)
    test_antifada_tree = etree.parse(antifada_test_xml, parser)

    assert(tbs_tree == test_tbs_tree)
    assert(vngrd_tree == test_vngrd_tree)
    assert(antifada_tree == test_antifada_tree)

    tbs_test_xml.close() 
    vngrd_test_xml.close()
    antifada_test_xml.close()