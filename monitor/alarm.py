#!/usr/bin/evn python2.6
#--coding=utf-8

"""
@author:hongxing.fan
@date:2016-01-27 Wednesday
@desc:报警
"""

import commands
import time
from email.mime.text import MIMEText
import smtplib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Alarm(object):
    """ 
    python报警程序
    """

    def __init__(self):
        """ """
        pass

    def nowTime(self):
        """ 
        获取时间
        """
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        return now

    def sendPhone(self, users_phones, msg):
        """ 
        发送短信
        """
        for phone in users_phones:
            execCmd="gsmsend-script " + phone + "@" + msg
            (status, outputs) = commands.getstatusoutput(execCmd)
            if(status != 0):
                print("%s %s status=%s, error!" % (self.nowTime(), msg, status))
            else:
                print("%s %s status=%s, right!" % (self.nowTime(), msg, status))

    def sendMail(self, users_mail, subject, msg):
        """ 
        发送邮件
        """
        #cbg-data@baidu.com
        mailHost = "mail1-in.baidu.com"
        from_1 = "noah-autopost@baidu.com"
        to_mail = ";".join(users_mail)
        content = MIMEText(msg, _subtype = "html", _charset = "utf-8")  # 创建一个实例，这里设置为文本格式邮件
        content["Subject"] = subject  # 设置主题
        content["From"] = from_1
        content["To"] = to_mail
        content["Accept-Language"] = "zh-CN"
        content["Accept-Charset"] = "ISO-8859-1,utf-8"
        try:
            smtp = smtplib.SMTP()
            smtp.connect(mailHost)
            smtp.sendmail(from_1, users_mail, content.as_string())  # 发送邮件
            smtp.close()
            print("%s %s right!" % (self.nowTime(), msg))
            return True
        except Exception as e:
            print("%s %s error!" % (self.nowTime(), msg))
            return False


if __name__ == "__main__":
   # users_phones = ["13811063282"]
    subject=sys.argv[1]
    msg=sys.argv[2]
    users_mail=sys.argv[3].split(",")
    #msg = "function jobname msg"
    #users_mail = ["fanhx9@163.com","fanhongxing@baidu.com"]
    #subject = "subject_aa"
    mails = users_mail
    print(mails)
    alarm = Alarm()
    #alarm.sendPhone(users_phones, msg)
    alarm.sendMail(mails, subject, msg)
