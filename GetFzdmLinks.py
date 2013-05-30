# -*- coding=UTF-8 -*-
import urllib2
import os
from urllib import urlretrieve
from bs4 import BeautifulSoup

class PageParser():
    def __init__(self, url, dirName):
        self.url = url;
        self.pageList = []
        self.dirName = dirName
        self.myInit()
        
        
    def myInit(self):
#        self.f = open(self.fileName,'w')
        html1 = self.getAlldataFromUrl(self.url).decode('utf-8','ignore');
        soup = BeautifulSoup(html1, "lxml")
    
        contentDiv = soup.find(id="content")
        contentDiv.find_all('li')
        for link in contentDiv.find_all('a'):
            if link.has_key('href'):
#                print self.url + link['href']
                self.pageList.append(self.url + link['href'])
        self.pageList.reverse()

    def close(self):
        self.f.close
        
    def downloadAllPages(self):
        if len(self.pageList) == 0:
            print "Sorry, the pageList is empty"
            return
        
        for page in self.pageList:
            self.downloadPage(page)
            
    def downloadPage(self, page):
        print "Downloading ... " + page
    
        navContents = []
        imgContents = []
        outpath = os.path.join(".", self.dirName + page.split('/')[-2])
        if not os.path.exists(outpath):
            os.makedirs(outpath)
    
        html1 = self.getAlldataFromUrl(page).decode('utf-8','ignore');
        soup = BeautifulSoup(html1, "lxml")    
        navLink = soup.find(class_="navigation")
        
        if navLink is not None:
            for link in navLink.find_all('a'):
                if link.has_key('href'):
#                    print page + link['href']
                    navContents.append(page + link['href'])
        
        for nav in navContents:
            imgContents.append(self.getImgUrl(nav))
            
        #print imgContents
        if len(imgContents) != len(navContents):
            print "Note: there must something wrong, please try again"
            return
        
        count = 0
        for img in imgContents:
            self.downloadImg(img, outpath + "\\" + str(count) + ".png")
            count = count + 1
            
        print "Download complete"
        print "\n================"

    def getImgUrl(self, nav):
        html1 = self.getAlldataFromUrl(nav).decode('utf-8','ignore');
        soup = BeautifulSoup(html1, "lxml")    
        srcLink = soup.find(id="mhpic")
#        print srcLink['src']
        return srcLink['src']
            
    def downloadImg(self, img, outpath):
        print "Putting img " + img + " to " + outpath 
        urlretrieve(img, outpath)
        
    def getAlldataFromUrl(self, url):
        fp = urllib2.urlopen(url)

        response = ""
        while 1:
            data = fp.read()
            if not data:         # This might need to be    if data == "":   -- can't remember
                break
            response += data
        return response

def retry(attemptTime):
    attempts = 0
    while attempts < attemptTime:
        try:
            print "I'm trying..."
            raise Exception()
        except:
            attempts += 1
            print "catch exception"
#            import traceback
#            traceback.print_exc()
    print "tried " + str(attempts) + " times"

def main():
#    retry(2)
    urlAddress = "http://manhua.fzdm.com/1/";
    parser = PageParser(urlAddress, "dddd\\")
    parser.downloadAllPages()
        
if __name__ == '__main__':
    main();
