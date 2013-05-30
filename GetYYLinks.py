import sgmllib
import urllib2
from pprint import pprint

class PageParser(sgmllib.SGMLParser):
    def __init__(self, aFile):
        # inherit from the SGMLParser class
        sgmllib.SGMLParser.__init__(self)

        # create a list this will store all the links found
        self.links = []
        self.isInBox = False;
        self.isThunder = False;
        self.thunderCount = 0;
        self.file = aFile;
                        
    def handle_data(self, data):
        if(self.isInBox and self.isThunder):
            self.thunderCount = self.thunderCount + 1;
            if(self.thunderCount == 3) :
                print data;
                self.isThunder = False; #eat it
                self.thunderCount = 0;

    def unknown_starttag(self, tag, attrs):
        for key, value in attrs:
            #print "key and value", key, value
            #if key == "thunderrestitle" and value.endswith('rmvb'):
            if key == "thunderrestitle":
                self.isThunder = True;
                
        if(self.isThunder):
            # print unicode(attrs[2][1], 'utf-8'), ",", attrs[5][1]
            print attrs[5][1].strip(); 
            self.file.write(unicode(attrs[2][1], 'utf-8'));
            self.file.write(",");
            self.file.write(attrs[5][1].strip());
            self.file.write("\n");
            self.isThunder = False; #eat it
        
def getBaiduHDList(vedioUrl):
    bdhdList = []
    sock = urllib2.urlopen(vedioUrl)
    f = open('thunder.csv', 'w')
    # make sure the string that is going to be parsed is 8-bit ascii
    if sock.info().dict['content-type'] == 'text/html; charset=utf-8':
        parser = PageParser(f)
        parser.feed(sock.read());
        parser.close();
        f.close();
        #bdhdList = parser.links

    return bdhdList

def main():
    #read id from file
#    urlAddress = "http://www.yyets.com/php/resource/26351";
    urlAddress = "http://www.yyets.com/php/resource/26263";
    
    getBaiduHDList(urlAddress);
    #pprint (txtlist)
  

if __name__ == '__main__':
    main();