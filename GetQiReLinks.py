import sgmllib
import urllib2
from pprint import pprint
from bs4 import BeautifulSoup

class PageParser(sgmllib.SGMLParser):
    def __init__(self, aPrefix):
        # inherit from the SGMLParser class
        sgmllib.SGMLParser.__init__(self)

        # create a list this will store all the links found
        self.links = []
        self.prefix = aPrefix;
        
    def unknown_starttag(self, tag, attrs):
        for key, value in attrs:
            #print "key and value", key, value
            if key == "href" and value.startswith('/videos/'):
                self.links.append(self.prefix + value)

class PageParserForBaidhHD(sgmllib.SGMLParser):
    def __init__(self):

        # inherit from the SGMLParser class
        sgmllib.SGMLParser.__init__(self)

        # create a list this will store all the links found
        self.links = []
        
    def unknown_starttag(self, tag, attrs):
        print "unknown tag start " + tag        
        for key, value in attrs:
            print key , value
            if key.lower() == "param_url":
                value = unicode(value, 'utf-8')
                print value
                self.links.append(value)
        
def getGiRenList(vedioUrl):
    bdhdList = []
    sock = urllib2.urlopen(vedioUrl)
    # make sure the string that is going to be parsed is 8-bit ascii
    if sock.info().dict['content-type'] == 'text/html':
        parser = PageParser("http://www.qire123.com/")
        parser.feed(sock.read());
        parser.close();
        bdhdList = parser.links

    return bdhdList

def getBaiduHDAddress(vedioUrl):
    bdhdList = []
    sock = urllib2.urlopen(vedioUrl)
    if sock.info().dict['content-type'] == 'text/html':
#        page = sock.read()
        soup = BeautifulSoup(sock)
        soup.prettify()
        for anchor in soup.findAll('object'):
            print anchor['href']

    return bdhdList

def main():
    urlAddress = "http://www.qire123.com/occident/yifanzhuizongdiyiji/";
    
    #pprint (getGiRenList(urlAddress));
    list1 = getGiRenList(urlAddress);
    list1.reverse();
    for aUrl in list1:
        getBaiduHDAddress(aUrl);
    #pprint (txtlist)
  

if __name__ == '__main__':
    main();