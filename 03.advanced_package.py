# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:55:54 2020

@author: KINONIA
"""

-------------------------------------------------------------------------------
# 로깅 설정
import logging
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

fileHandler = TimedRotatingFileHandler('test.log', when='midnight')
fileHandler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logger.addHandler(fileHandler)

logger.info('hello world')
logger.info('kinonia')


-------------------------------------------------------------------------------
# 이메일 및 파일첨부
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

contents = MIMEText('파이썬을 학습하자\n매일 1시간씩 하지.'.encode('utf-8'),_charset='UTF-8')
contents['Subject']="파이썬 스터디"

file = "T:/schedule.pdf"
attachments = MIMEBase('application','octet-stream')
attachments.add_header('Content-Disposition','attachment;filename="%s"' % os.path.basename(file))
attachments.set_payload(open(file,'rb').read())
encoders.encode_base64(attachments)

message = MIMEBase('multipart', 'mixed')
message.attach(contents)
message.attach(attachments)

smtpObj = smtplib.SMTP('smtp.kefico.co.kr', 25)
smtpObj.ehlo()
smtpObj.sendmail('hyunbae.jeong@kefico.co.kr', 'hyunbae.jeong@kefico.co.kr', message.as_string())

smtpObj.quit()


