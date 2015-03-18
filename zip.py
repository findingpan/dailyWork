#coding=utf-8
#甄码农python代码
#使用zipfile做目录压缩，解压缩功能
 
import os,os.path
import zipfile
 
f = zipfile.ZipFile('hahah.zip', 'w' ,zipfile.ZIP_DEFLATED)
f.write('1.txt')
f.close()

