#!/usr/bin/env python
# _*_ coding:utf8 _*_
'''Created on 2016-11-20 @Author:Guolikai'''
import sys
import time
sys.path.append('/root/python/mysqlbank')
from Model.Bankdata   import UserInfo,UserLocked,AccountDetails
from BLL.AccountLogin import AccountNameExist,AccountNameLock,AccountExit
from BLL.TryOperation import TryOperationStr,TryOperationInt

class AccountSavings(object):
    def __init__(self):
        pass
    def UserOperation(self):
        message = ['select_money','save_money','take_money','transfer_account','accout_details','exit']
        #查询额度、存钱、取钱、转账、账户记录、退出
        for item in enumerate(message,1):
            print item[0],item[1]
        tryoperationint = TryOperationInt()
        your_choice = tryoperationint.TryOperationInt('您接下来的操作[1-6]:')
        return message[your_choice-1]
    def DataTime(self):
        time_result = time.strftime('%Y-%m-%d %H:%M:%S')
        return time_result
    def AccoutRecord(self,username,trans_amount,other_account,description):
        trans_date = DataTime()
        accountdetails = AccountDetails()
        record_result = accountdetails.InsertAccountDetails(trans_date,username,trans_amount,other_account,description)
        #print "时间%s用户%s操作%s金额%s " % (trans_date,username,description,trans_amount)
        return record_result

    def AccoutDetails(self,username):
        accountdetails = AccountDetails()
        data = accountdetails.SelectAccountDetails(username)
        for i in range(len(data)):
            dict  =  data[i]
            print dict['trans_date'],dict['trans_account'],dict['description'],dict['trans_amount'],'元'

    def SelectMoney(self,username):
        userinfo = UserInfo()
        selectmoney = userinfo.SelectCurrentMoney(username)
        print  '您的账户金额是%s' % selectmoney
    def SaveMoney(self,username):
        userinfo = UserInfo()
        save_old = userinfo.SelectCurrentMoney(username)
        save_money = 0
        while True:
            tryoperationint = TryOperationInt()
            save_money_value = tryoperationint.TryOperationInt('您的存款金额:')
            save_money += save_money_value
            save_old += save_money_value
            tryoperationstr = TryOperationStr()
            choice = tryoperationstr.TryOperationStr('您是否继续存钱[y/n]:')
            if choice == 'n':
                save_money_result = userinfo.UpdateUserinfoCurrentMoney(username,save_old)
                if save_money_result ==1:
                    record_result = AccoutRecord(username, save_money, '-', 'SaveMoney')
                    if record_result == 1:
                        print  'SaveMoney Success'
                        break
            else:
                continue
    def TakeMoney(self,username):
        userinfo = UserInfo()
        take_money = 0
        take_old = userinfo.SelectCurrentMoney(username)
        while True:
            take_money_value = TryOperationInt('您的取款金额:')
            if take_old >= take_money_value:
                take_old -= take_money_value
                take_money += take_money_value
                print '您的余额还剩%s元'  %  take_old
                tryoperationstr = TryOperationStr()
                choice = tryoperationstr.TryOperationStr('您是否继续取钱[y/n]:')
                if choice == 'n':
                    take_money_result = userinfo.UpdateUserinfoCurrentMoney(username, take_old)
                    if take_money_result ==1:
                        record_result = AccoutRecord(username, -take_money, '-', 'TakeMoney')
                        if record_result == 1:
                            print  'TakeMoney Success'
                    break
                else:
                    continue
            else:
                print "\033[35;5m您的余额不足剩%s元\033[1m"  %  take_old
                break
    def TransferMoney(self,username):
        userinfo = UserInfo()
        transfer_money = 0
        transfer_old = userinfo.SelectCurrentMoney(username)
        while True:
            transfer_money_value = TryOperationInt('您的转账金额:')
            if transfer_old >= transfer_money_value:
                transfer_old -= transfer_money_value
                transfer_money += transfer_money_value
                print '您的余额还剩%s元' % transfer_old
                tryoperationstr = TryOperationStr()
                choice = tryoperationstr.TryOperationStr('您是否继续转账[y/n]:')
                if choice == 'n':
                    return transfer_money
                else:
                    continue
            else:
                print '您的余额不足，还剩%s元' % transfer_old
                continue
    def TransferOtherAccount(self):
        while True:
            transfer_other_account = raw_input('您的转账账户:')
            lock_result = AccountNameLock(transfer_other_account)
            if lock_result == 'Account Unlock':
                exist_result =  AccountNameExist(transfer_other_account)
                if exist_result == 'Account Exist':
                    return transfer_other_account
                else:
                    tryoperationstr = TryOperationStr()
                    choice = tryoperationstr.TryOperationStr('您是否继续输入转账账户[y/n]:')
                    if choice == 'n':
                        break
                    else:
                        continue

    def ProcessFee(self,money):
        percentage = "%5"
        return money*float(percentage.replace("%",""))/1000

    def TransferAccounts(self,username):
        userinfo = UserInfo()
        other_account = TransferOtherAccount()
        if other_account != username:
            trans_money = TransferMoney(username)
            processfee  = ProcessFee(trans_money)
            current_amount = userinfo.SelectCurrentMoney(username)
            other_amount = userinfo.SelectCurrentMoney(other_account)
            #print '转账前',trans_money,current_amount,other_amount
            current_new_money = current_amount - trans_money - processfee
            other_new_amount  = other_amount + trans_money
            #print '转账后',current_new_money,other_new_amount
            current_update_amount = userinfo.UpdateUserinfoCurrentMoney(username,current_new_money)
            if current_update_amount == 1:
                other_update_amount = userinfo.UpdateUserinfoCurrentMoney(other_account,other_new_amount)
                if other_update_amount ==1:
                    print 'TransAmount Success'
                    AccoutRecord(username,-trans_money,other_account,'AccountTransfer')
                    AccoutRecord(username,-processfee,other_account,'AccountProcessFee')
                    AccoutRecord(other_account,trans_money,username,'AccountReceived')
                else:
                    userinfo.UpdateUserinfoCurrentMoney(username,current_amount)
                    userinfo.UpdateUserinfoCurrentMoney(other_account,other_amount)
        else:
            print '\033[35;1m您不可以对自己转账!\033[0m'
    def AccountSavingsMain(self,username):
        while True:
            login_operation_result = self.UserOperation()
            if login_operation_result=='select_money':
                self.SelectMoney(username)
            elif login_operation_result == 'accout_details':
                self.AccoutDetails(username)
            elif login_operation_result=='save_money':
                self.SaveMoney(username)
            elif login_operation_result == 'take_money':
                self.TakeMoney(username)
            elif login_operation_result == 'transfer_account':
                self.TransferAccounts(username)
            elif login_operation_result == 'exit':
                self.AccountExit(username)
if __name__ == '__main__':
    username = raw_input('\033[32;1mUsername:\033[0m')
    accountsavings = AccountSavings()
    accountsavings.AccountSavingsMain(username)
