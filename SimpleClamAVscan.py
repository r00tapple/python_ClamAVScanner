import sys, dircache, os
import pyclamav
from HTMLParser import HTMLParser, HTMLParseError
import urllib2


############################################################################
class Parse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
	self.span_flag = False
	self.td_flag = False
    
    def handle_starttag(self, tag, attrs):
	if tag == 'span':
		self.span_flag = True
	if tag == 'td':
		self.td_flag = True

    def handle_data(self, data):
	 if self.span_flag:
            self.span = data
            self.span_flag = False

	 if self.td_flag:
            self.td = data
            self.td_flag = False
############################################################################

############################################################################
def scanfile(file):
	
	try:
		ret = pyclamav.scanfile(file)

	except ValueError, e:
		print '[*]ValueError :', e, '("'+file+'")'
		return None
	except TypeError, e:
		print '[*]TyperError :', e, '("'+file+'")'
		return None

	else:
		if ret[0]==0:
			print "____________________________"
			print "[*]", file, 'is not infected.......'
			print "____________________________"
			return True
		elif ret[0]==1:
			print "____________________________"
			print '[*]', file, 'is infected with', ret[1], '  !!!!'
			url = 'http://totalhash.com/search/av:' + ret[1]
			response = urllib2.urlopen(url)
			html = Parse()
			html.feed(response.read())
			html.close()
			print '%s - %s' % (url, html.span)
			print "____________________________"
			return False
############################################################################

############################################################################
if __name__ == '__main__':
    
    if len(sys.argv)>1:
        
        dirlisting=dircache.listdir(sys.argv[1])
        if dirlisting!=[]:
            for file in dirlisting:
                scanfile(file)
        else:
            scanfile(sys.argv[1])

    else:
        dirlisting=dircache.listdir('./')
        if dirlisting!=[]:
            for file in dirlisting:
                scanfile(file)  
#######################################################################
