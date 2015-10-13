import sys, dircache, os
import pyclamav

############################################################################
def scanfile(file):
	
	ret = pyclamav.scanfile(file)
	
	if ret[0]==0:
		print "____________________________"
		print "[*]", file, 'is not infected.......'
		print "____________________________"
		return True
			
	elif ret[0]==1:
		print "____________________________"
		print '[*]', file, 'is infected with', ret[1], '  !!!!'
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
        folder =dircache.listdir('./')
        if folder!=[]:
            for file in folder:
                scanfile(file)  
#######################################################################
