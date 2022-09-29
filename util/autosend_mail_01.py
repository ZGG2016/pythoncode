
import sys
from poplib import POP3
from smtplib import SMTP
from smtplib import SMTPRecipientsRefused

"""
自动发送邮件：

1.安装cron，在命令行中输入 yum -y install cron

2. vi /etc/crontab 在最后加入:
        0 17 * * 1-5 /usr/bin/python autosend_mail_01.py ....[输入参数]
        周一到周五每天下午 5:00 自动发送邮件
"""


def auto_send_mail(msg,content,sender_emailaddr,sender_username,sender_password,receiver_emailaddr,receiver_username,receiver_password):

    smtp_server = 'smtp.163.com'
    pop3_server = 'pop.163.com'

    mail_headers = ('From: %s' % sender_emailaddr,
                   'To: %s' % receiver_emailaddr,
                   'Subject: %s' % msg )
    mail_body = "%s" % content
    # 开头 + 邮件内容
    mail_msg = '/r/n/r/n'.join(['/r/n'.join(mail_headers), '/r/n'.join(mail_body)])

    send_server = SMTP(smtp_server)
    # sendSer.set_debuglevel(1)
    # print sendSer.ehlo()[0]  # 服务器属性等
    send_server.login(sender_username, sender_password)  # 登录
    try:
        # 第二个参数接受一个列表
        errs = send_server.sendmail(sender_emailaddr, receiver_emailaddr, mail_msg)
    except SMTPRecipientsRefused:
        print('server refused....')
        sys.exit(1)
    send_server.quit()

    # 开始接收邮件
    receiver_server = POP3(pop3_server)
    receiver_server.user(receiver_username)
    receiver_server.pass_(receiver_password)

    rsp, msg, siz = receiver_server.retr(receiver_server.stat()[0])
    # sep = msg.index('')
    if msg:
        for i in msg:
            print(i)
    # revcBody = msg[sep + 1:]
    # assert origBody == revcBody
    print('successful get ....')


if __name__ == "__main__":

    msg = sys.argv[1]
    content = sys.argv[2]

    sender_emailaddr = sys.argv[3]
    sender_username = sys.argv[4]
    sender_password = sys.argv[5]

    receiver_emailaddr = sys.argv[6]
    receiver_username = sys.argv[7]
    receiver_password = sys.argv[8]

    auto_send_mail(msg,content,
                   sender_emailaddr,sender_username,sender_password,
                   receiver_emailaddr,receiver_username,receiver_password)

