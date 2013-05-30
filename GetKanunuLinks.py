# -*- coding=UTF-8 -*-
import urllib2
from pprint import pprint
from bs4 import BeautifulSoup

class MyData():
    def __init__(self, url, title):
        self.url = url
        self.title = title

class PageParser():
    def __init__(self, url, fileName):
        self.url = url;
        index = self.url.rfind("/")
        self.prefix = self.url[:(index+1)]
        self.contextList = []
        self.fileName = fileName + ".txt"
        #print prefix
        self.myInit()
        
        
    def myInit(self):
        self.f = open(self.fileName,'w')
        html1 = urllib2.urlopen(self.url).read();
        soup = BeautifulSoup(html1)
    
        #pprint(soup.prettify())
        for contextsTable in soup.find_all("table", attrs={"bgcolor": "#d4d0c8"}):
            #print("==========\n")
            #print type(contextsTable)     
            self.contextList = self.printContextTable(contextsTable) 

    def close(self):
        self.f.close

    def printContextTable(self, contextsTable):
        contextList = []
        for link in contextsTable.find_all("a"):
            # print (link['href'])
            contextList.append(MyData(link['href'], unicode(link.string)))
        return contextList

    def printPara(self):
        for myData in self.contextList:
            #print self.prefix + url, title
            self.printIt(self.prefix + myData.url, myData.title)

    def printIt(self, url, title):
#        print type(title)
        print title + "\n "
        self.f.write(title.encode('gb2312', 'ignore') + "\n ")
        print url
        self.f.write(url+"\n ")

    
        html1 = urllib2.urlopen(url).read().decode('gb2312','ignore');
        soup = BeautifulSoup(html1, "lxml")
        # print soup.prettify();
        for para in soup.find_all("p"):
            # print type(para)
#            print para.text.encode('gb2312', 'ignore') 
            self.f.write(para.text.encode('gb2312', 'ignore'))
            
    def printItTest(self, url, title):
        print title.encode('gb2312', 'ignore')
        self.f.write(title.encode('gb2312', 'ignore'))
        print url
        self.f.write(url)
    
        html1 = urllib2.urlopen(url).read().decode('gb2312','ignore');
        soup = BeautifulSoup(html1, "lxml")
        # print soup.prettify();
        for para in soup.find_all("p"):
            # print type(para)            
            print para.text.encode('gb2312', 'ignore') 
            self.f.write(para.text.encode('gb2312', 'ignore'))

def main():
    #1. get one book
#    沧海
    urlAddress = "http://book.kanunu.org/book/4653/index.html";
    
    parser = PageParser(urlAddress, "dddd")    
    parser.printPara();

    #2. get all book of one author
#    writerUrl = "http://book.kanunu.org/files/writer/231.html"
#    bookPrefix = "http://book.kanunu.org"
    
#    s = u'中国'
#    f = open(s.encode('gb2312'),'w')
#    
#    s = "http://book.kanunu.org/book3/6396/index.html "
#    index = s.rfind("/")
#    print s[:index]
    
#    html1 = urllib2.urlopen(writerUrl).read().decode('gb2312','ignore');
#    soup = BeautifulSoup(html1, "lxml")
#    for contextsTable in soup.find_all("table", attrs={"bgcolor": "#d6d3ce"}):
#        for link in contextsTable.find_all("a"):
#            print ("===========start=============")
#            print bookPrefix + link['href'], unicode(link.string)
#            parser = PageParser(bookPrefix + link['href'], unicode(link.string))    
#            parser.printPara();

if __name__ == '__main__':
    main();
