#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
      
sender = 'yi.pan@ncich.com.cn'  
receiver = ['yi.pan@ncich.com.cn','zheng.zhang@ncich.com.cn']  
subject = 'python email test'  
smtpserver = 'mail.ncich.com.cn'  
username = 'yi.pan'  
password = '112344'  
      
msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = 'test message'  
      
#构造附件  
att = MIMEText(open('e:\\hahah.zip', 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="hahah.zip"'  
msgRoot.attach(att)  

try:
    smtp = smtplib.SMTP()  
    smtp.connect('mail.ncich.com.cn')
    smtp.login(username, password)  
    smtp.sendmail(sender, receiver, msgRoot.as_string())
except Exception, e:
    print e
else:
    print 'send successful'
finally:
    smtp.quit() 
           
 
 
