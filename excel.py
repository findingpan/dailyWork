#coding:utf-8
import xlwt
import xlrd
#import xlutils
from xlutils.copy import copy
import subprocess
import os

oldWb = xlrd.open_workbook('1.xlsx')

newWb = copy(oldWb)

newWs = newWb.get_sheet(0)
newWs.write(1, 0, "value1")
newWs.write(1, 1, "value2")
newWs.write(1, 2, "value3")

print "write new values ok"
newWb.save('2.xls')

os.startfile('2.xls')

print "save with same name ok"
            
            