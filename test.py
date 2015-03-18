#coding:utf-8
import os
import subprocess

class ExeMgr(object):

    def __init__(self,appPath):
        
        self.appPath = appPath
        self.pid = None
        
    def start(self):
        
        if(os.path.exists(self.appPath)):
            p = subprocess.Popen(self.appPath)
            self.pid = p.pid
            if self.pid is None:
                return False
            print self.pid
            print u'程序已成功启动'
            return True
        else:
            print u'应用程序路径'+self.appPath+u'不存在'
            
            
if __name__ == '__main__':
    
    exeMgr = ExeMgr(r'F:\Program Files (x86)\Evernote\Evernote\Evernote.exe')
    exeMgr.start()
    