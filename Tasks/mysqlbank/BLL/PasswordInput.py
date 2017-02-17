#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import sys,tty,termios
class PasswordInput(object):
#for python 2.x
    def __init__(self):
        pass
    def Getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def Getpass(self,maskchar):
        password = ""
        while True:
            ch = self.Getch()
            if ch == "\r" or ch == "\n":
                print
                return password
            elif ch == "\b" or ord(ch) == 127:
                if len(password) > 0:
                    sys.stdout.write("\b \b")
                    password = password[:-1]
            else:
                if maskchar != None:
                    sys.stdout.write(maskchar)
                password += ch
    def PasswdMd5(self,string):
        import hashlib
        string = hashlib.md5(string.encode(encoding="utf-8"))
        return string.hexdigest()

    def PasswordInputMain(self):
        print '\033[35;1m请输入您的密码:\033[0m',
        password = self.Getpass('*')
        data = self.PasswdMd5(password)
        return data
if __name__ == "__main__":
    pwd = PasswordInput()
    print   pwd.PasswordInputMain()
