# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from HuShi.Common.package_mail import Package_MailContent
import HuShi.Config.mail_config

class Send_Mail:

    def __init__(self,file_new):
        self.file_new = file_new
        self.msg_from = HuShi.Config.mail_config.msg_from
        self.passwd = HuShi.Config.mail_config.passwd
        self.msg_to = HuShi.Config.mail_config.msg_to

    def Send(self,count):

        title = "接口自动化测试报告"  # 主题
        content = Package_MailContent(self.file_new).report_info(count)

        msg = MIMEText(content,_subtype="html",_charset="utf-8")     # 正文
        msg['Subject'] = title
        msg['From'] = self.msg_from
        msg['To'] = self.msg_to
        try:
            # 邮件服务器及端口号
            s = smtplib.SMTP_SSL(HuShi.Config.mail_config.address,HuShi.Config.mail_config.port)
            s.login(self.msg_from, self.passwd)
            s.sendmail(self.msg_from, self.msg_to, msg.as_string())
            # 添加附件
            att = MIMEText(open(file_new,"rb").read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = ('attachment; filename="{}"'.format(self.file_new))
            msg.attach(att)

            print("发送成功")
        except s.SMTPException as e:
            print("发送失败")
        finally:
            s.quit()

if __name__ == "__main__":
    Send_Mail().Send()