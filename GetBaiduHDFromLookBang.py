import sgmllib
import urllib2
from pprint import pprint

class PageParser(sgmllib.SGMLParser):
    def __init__(self):

        # inherit from the SGMLParser class
        sgmllib.SGMLParser.__init__(self)

        # create a list this will store all the links found
        self.links = []

    def unknown_starttag(self, tag, attrs):
        #print "unknown tag start " + tag        
        for key, value in attrs:
            #print key , value
            if key.lower() == "param_url":
                value = unicode(value, 'utf-8')
                print value
                self.links.append(value)

        
def getBaiduHDList(vedioUrl):
    bdhdList = []
    sock = urllib2.urlopen(vedioUrl)
    # make sure the string that is going to be parsed is 8-bit ascii
    if sock.info().dict['content-type'] == 'text/html; charset=utf-8':
        parser = PageParser()
        parser.feed(sock.read())
        bdhdList = parser.links

    return bdhdList

def main(wuxiaUrl):
    #read id from file
    urlPrefix = "http://www.lookbang.com/ajax/callvideo2?id="
    
    txtf = open("./the_fire_id.txt", "r")  
    txtlist = [getBaiduHDList(urlPrefix + l) for l in txtf.readlines()]
    #pprint (txtlist)
  

if __name__ == '__main__':
    main("http://www.lookbang.com/ajax/callvideo2?id=HBsLX4")
    #if len(sys.argv) < 2:
    #    print("Usage: %s xuxiaurl"%sys.argv[0])
    #else:
    #    main(sys.argv[1])
