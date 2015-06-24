#-*-coding:utf-8-*-
#****Python字符编码问题****
#python 2.7.8
'''
一、python中的str和unicode
unicode：是一种类。例如：哈哈的unicode对象是u'\u54c8\u54c8'
str：是一个字节数组。
'''
su = u'哈哈'
#su
#u'\u54c8\u54c8' 十六位
s_utf8 = su.encode('utf-8')
#s_utf8 #在cmd中的python
#2显示'\xe5\x93\x88\xe5\x93\x88' 八位
print s_utf8
#2显示鍝堝搱
s_gbk = su.encode('gbk')
#s_gbk
#2显示'\xb9\xfe\xb9\xfe' 八位
print s_gbk
#2显示哈哈
print su
#2显示哈哈
'''
二、str和unicode对象的转换
'''
s = '哈哈'
print s.decode('gbk').encode('utf-8')
#decode('gbk')转换成unicode
'''
三、Setdefaultencoding
'''
su = '哈哈'
#su.encode('utf-8')会报错
import sys
reload(sys)
sys.setdefaultencoding('gbk')
su.encoding('utf-8')
#因为python将str解码的使用时基于ascii，所以第一次编码的时候
#会出错，那么设定当前默认编码为'gbk'。
'''
四、操作不同文件的编码格式的文件
'''
#建立一个文件Encode.txt，文件格式用ANSI
'''
五、文件的编码格式和编码声明的作用
'''
#Encode1.py