#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © lanrenzhoumo.com
# Date  : 2015-02-26
# Author: yumi
# Email : <yumi@lanrenzhoumo.com>
#
# Distributed under terms of the MIT license.

'''
    发送一个文本邮件
    参考网址:http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html
'''

import logging
import smtplib
import json

from email.mime.text import MIMEText

class MailSender():

    # 腾讯企业邮箱
    tc_exmail_host      = "smtp.exmail.qq.com"
    dianhun_exmail_host = "mail.dianhun.cn"

    """这个类的职责就是发送邮件"""
    def __init__(self, sendername, sendermail, password):
        self.showname   = sendername + "<" + sendermail + ">"
        self.sendermail = sendermail
        self.password   = password
    
    def send_mail(self, receiver_list, title, content, mail_host=dianhun_exmail_host):
        """发送邮件"""
        assert isinstance(receiver_list, (list, tuple))
        msg = MIMEText(content, _subtype="plain", _charset="utf8")
        msg["Subject"] = title
        msg["From"] = self.showname
        msg["To"] = ";".join(receiver_list)
        try:
            server = smtplib.SMTP()
            server.connect(mail_host)
            server.login(self.sendermail, self.password)
            server.sendmail(self.showname, receiver_list, msg.as_string())
            server.close()
            return True
        except Exception as e:
            logging.error(str(e))
            return False

fh      = open("config.json", "rb")
config  = json.load(fh)
fh.close()

ms_sender_name      = config["name"]
ms_sender_mail      = config["mail"]
ms_sender_password  = config["password"]

mail_sender = MailSender(ms_sender_name, ms_sender_mail, ms_sender_password)
send_mail = mail_sender.send_mail

if __name__ == '__main__':
    if send_mail(["etond@dianhun.cn"], "code completex", "the url https://www.baidu.com code complete is a cool book"):
        print "发送成功"
    else:
        print "发送失败"
