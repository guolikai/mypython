#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlwt
import re,collections
import datetime
Now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CurrentDate=datetime.datetime.now().strftime("%Y%m%d")
LastWeekDate=datetime.date.today() - datetime.timedelta(days=7)

def GetWords(file):
    RET={'hosts':'','problems':'','items':''}
    with open (file) as f:
        host=[]
        problem=[]
        item=[]
        for line in f:
            MSG=line.split(',')[2]
            if re.search(u'故障',MSG):
                 Host=MSG.split(':')[1].split(' ')[0]
                 Problem=MSG.split(':')[2].split(u'故障')[0]
                 ##删除字符串左边的空格:lstrip()
                 Problem=Problem.lstrip()
                 Item="%s'%s'" % (Host,Problem)
                 host.append(Host)
                 problem.append(Problem)
                 item.append(Item)
        RET['hosts']=collections.Counter(host)
        RET['problems']=collections.Counter(problem)
        RET['items']=collections.Counter(item)
        return RET

def WriteOPS(DATA):
    List=[]
    for k in DATA.items():
        List.append(k)
    #List=sorted(List, key=lambda x: (x[1], x[0].lower()))
    List=sorted(List, key=lambda x: (x[1],x[0]))
    List.insert(0,(u'告警项',u'告警数量'))
    List=tuple(List)
    return List

def LinuxWriteThree(Data1,Table1,Data2,Table2,Data3,Table3,SaveDirFile):
    workbook=xlwt.Workbook(encoding='utf-8')  
    booksheet=workbook.add_sheet(Table1,cell_overwrite_ok=True)
    for i,row in enumerate(Data1):  
        for j,col in enumerate(row):
            booksheet.write(i,j,col)  
    
    booksheet=workbook.add_sheet(Table2,cell_overwrite_ok=True)
    for i,row in enumerate(Data2):  
        for j,col in enumerate(row):
            booksheet.write(i,j,col)  

    booksheet=workbook.add_sheet(Table3,cell_overwrite_ok=True)
    for i,row in enumerate(Data3):  
        for j,col in enumerate(row):
            booksheet.write(i,j,col)  
			
    workbook.save('%s' % (SaveDirFile))

def AnalyData(File,WriteToFile):
    data=GetWords(File)
    AnalyDict={}
    for key,value in data.items():
        AnalyDict[key]=WriteOPS(value)
    hostsdata=AnalyDict['hosts']
    problemsdata=AnalyDict['problems']
    itemsdata=AnalyDict['items']
    #print(hostsdata)
    #print(problemsdata)
    #print(itemsdata)
    #生成zabbix_alert_analyse_data Excel文件
    LinuxWriteThree(hostsdata,'HostsData',problemsdata,'ProblemsData',itemsdata,'HostsProblemsData',WriteToFile)
    print("本周Zabbix告警分析见文件:%s" % WriteToFile)

##定义YanxiuMail邮件格式
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class SendMail(object):
    def __init__(self,maillist,mailtitle,mailcontent):
        self.mail_list = maillist
        self.mail_title = mailtitle
        self.mail_content = mailcontent

        self.mail_host = "smtp.lzhot.net"
        self.mail_user = "zabbix@lzhot.net"
        self.mail_pass = "lzhot."
        self.mail_postfix = "lzhot.net"
        self.mail_port = 25
        #print(self.mail_host,self.mail_user,self.mail_pass,self.mail_list)

    def SendMailMain(self,Filedir,File):
        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = self.mail_title
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)
        puretext = MIMEText(self.mail_content)
        msg.attach(puretext)
        Attachment="%s/%s" % (Filedir,File)
        attachmentpart = MIMEApplication(open(Attachment, 'rb').read())
        attachmentpart.add_header('Content-Disposition', 'attachment', filename='%s' % File)
        msg.attach(attachmentpart)
        try:
            #s = smtplib.SMTP()                                #创建邮件服务器对象
            #s.connect(self.mail_host)                         #连接到指定的smtp服务器。参数分别表示smpt主机和端口
            #s.login(self.mail_user, self.mail_pass)           #登录到你邮箱
            #s.sendmail(me,self.mail_list,msg.as_string())     #发送内容
            #s.close()
            smtp = smtplib.SMTP(self.mail_host, self.mail_port)
            smtp.set_debuglevel(0)
            smtp.ehlo()
            smtp.login(self.mail_user,self.mail_pass)
            smtp.sendmail(me, self.mail_list, msg.as_string())
            smtp.close()
            return True
        except Exception as e:
            print(e)
            return False


def main():
    import os
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(BASE_DIR)
    #FileDir='/root/workspace/zabbix_alert'
    FileDir = os.path.dirname(os.path.abspath(__file__))
    File='%s/alert_mail.%s.log' % (FileDir,CurrentDate)
    ToFile='zabbix_alertmail_countanalyse_%s.xls'  %  CurrentDate
    WriteToFile='%s/%s'  %  (FileDir,ToFile)
    AnalyData(File,WriteToFile)
    mailto_list = ["guolikai@yanxiu.com"]
    mail_title = '本周Zabbix告警统计分析:%s~%s'   % (LastWeekDate.strftime("%Y%m%d"),CurrentDate)
    mail_content = '本周Zabbix告警统计分析见附件:\n%s'  %   ToFile
    send_mail = SendMail(mailto_list,mail_title,mail_content)
    send_res = send_mail.SendMailMain(FileDir,ToFile)
    #print(send_res)
    print('本周Zabbix告警统计分析完成')


if __name__ == "__main__":
    main()
