#codig=gbk
import codecs
import sys
reload(sys)
sys.setdefaultencoding('gbk')
data = open('Encode.txt').read()
if data[:3] == codecs.BOM_UTF8:
	data = data[3:]
print data.decode('utf-8')