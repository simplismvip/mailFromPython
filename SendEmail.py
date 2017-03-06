#!/usr/bin/python
# -*- coding: UTF-8 -*-
from email.mime.text import MIMEText
import smtplib
import urllib2

def sendEmail():

    from_addr = '799648397@qq.com'  # 输入邮箱地址和口令
    password = 'mjwnjayqpfbtbbfd'
    to_addr = 'simplismvip@163.com'  # 输入邮箱收件人地址

    smtp_server = 'smtp.qq.com'  # 输入SMTP服务器地址

    #获取当前硬件读取的温度文本
    currTemperature = readData('/Users/mac/Desktop/tem.txt')
    temperatureTur = (currTemperature, 30, 32, 15)


    msgContent = '早上好! 当前室内温度为 %s 摄氏度. 室外温度为 %s 摄氏度, 今天最高温度在下午1点为 %s 摄氏度, 最低温度为凌晨5点, 温度为 %s 摄氏度. 今天天气晴朗, 祝您一天好心情!' % temperatureTur
    msg = MIMEText(msgContent, 'plain', 'utf-8')
    msg['Subject'] = '当前室内温度'
    msg['Content-Type'] = 'Text/HTML'
    msg['From'] = from_addr
    msg['To'] = to_addr

    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print 'Send Success'

    except smtplib.SMTPException, e:
        print 'Send Failed, %s' % e

def readData(path):

    try:
        f = open(path, 'r')
        data = f.read()
    finally:
        if f:
            f.close()
            return data

def getWeather(url):
    # http://api.map.baidu.com/telematics/v3/weather?location=上海&output=JSON&ak=FK9mkfdQsloEngodbFl4FeY3
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent': user_agent}
    requ = urllib2.Request(url, headers=header)
    responds = urllib2.urlopen(requ)
    con = responds.read().decode('utf-8')
    print con


#sendEmail()
getWeather('http://api.map.baidu.com/telematics/v3/weather?location=上海&output=JSON&ak=FK9mkfdQsloEngodbFl4FeY3')










