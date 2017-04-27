def red(info):
    '''定义红色字体'''
    print("""\033[1;31m %s \033[1m""" % (info))

def black(info):
    '''定义黑色字体'''
    print("""\033[1;30m %s \033[1m""" % (info))

def green(info):
    '''定义绿色字体'''
    print("""\033[1;32m %s \033[1m""" % (info))

def passwd_md5(string):
    import hashlib
    string = hashlib.md5(string.encode(encoding="utf-8"))
    return string.hexdigest()

def process_fee(money):
    percentage = "%5"
    return money*float(percentage.replace("%",""))/100

# 打开用户信息文件并且赋值给user_lines变量，方便重复调用
with open(r"E:\tmp.txt", "r") as user_file:
    user_lines = user_file.readlines()
# 打开用户锁定文件并且赋值给lock_lines变量，方便重复调用
with open(r"E:\tmp.lock.txt", "r") as lock_file:
    lock_lines = lock_file.readlines()

def login():
    #调用red函数输出主题使用红色字体
    red("\n\t\t欢迎使用自助银行系统\n")
    #调用black函数输出信息使用黑色字体
    black("请输入你的用户名和密码")
    global username
    #让用户输入用户名
    username = input("用户：")
    #初始化i变量为0，当i等于3的时候循环退出，然后将用户锁定
    i = 0
    while i<3:
        #检查输入的用户是否被锁定
        for lock_line in lock_lines:
            if username in lock_line:
                return "用户已经被锁定禁止登陆"
                exit()
        #检查输入的用户是否存在
        user_all = ",".join(user_lines)
        if username not in user_all:
            return "用户不存在"
            exit()
        #循环用户信息文件
        for line in user_lines:
            #输入的用户匹配上后将列表的第0个元素和第1个元素赋值给user和passwd
            if username in line:
                l1 = line.strip("\n").split()
                user,passwd = l1[0:2]
                #用户输入密码
                password = input("密码：")
                #判断用户输入的用户和密码是否正确，正确返回登录成功，错误提示并且重新输入密码
                passwd = passwd_md5(passwd)
                password = passwd_md5(password)
                if username == user and password == passwd:
                    return "登陆成功"
                    exit()
                else:
                    red("密码错误，请重新登陆")
                    i += 1
    else:
        #输入密码超过三次将用户写入锁定文件
        w_lock_file = open(r"E:\tmp.lock.txt", "w")
        w_lock_file.write(username)
        w_lock_file.close()
        return "密码输错三次，账户锁定"

def current_user():
    #找出当前用户的金额
    for line in user_lines:
        if username in line:
            l1 = line.strip("\n").split()
            #金额的类型为数字类型
            current_user_money = int(l1[2])
            return current_user_money

def write_file(total_money):
    import os
    current_user_money = current_user()
    # 以写入的方式打开一个空文件
    w_file = open(r"E:\tmp(2).txt", "w")
    for line in user_lines:
        # 匹配上当前用户就更改他的金额到文件
        if username in line:
            w_file.write(line.replace(str(current_user_money), str(total_money)))
        else:
            # 其他没有匹配上的也写入文件
            w_file.write(line)
    # 关闭文件
    w_file.close()
    # 判断主文件是否存在，如果存在的话就删除然后改名
    if os.path.exists(r"E:\tmp.txt"):
        os.remove(r"E:\tmp.txt")
        os.rename(r"E:\tmp(2).txt", r"E:\tmp.txt")
    else:
        # 不存在的话就直接修改名字
        os.rename(r"E:\tmp(2).txt", r"E:\tmp.txt")

def tranfer():
    #导入os模块使用判断文件是否存在已经更新文件内容使用
    import os
    global transfer_user
    #输入需要转账的用户
    transfer_user = input("请输入你要转账的用户：")
    #将文件列表转换为字符
    user_all = ",".join(user_lines)
    #判断转账的用户是否存在如果不存在的话重新输入
    while transfer_user not in user_all:
        red("你输入的用户不存在，请重新输入")
        transfer_user = input("请输入你要转账的用户：")
    #输入转账的金额
    transfer_money = int(input("请输入你要转账的金额："))

    current_user_money = current_user()
    #如果转账的金额大于当前拥有的金额会提示金额不足
    while transfer_money > current_user_money:
        red("你的余额不足，转账失败，请重新输入")
        transfer_money = int(input("请输入你要转账的金额："))
    #获取当前用户的所剩金额，总金额-转账金额=剩余金额
    money1 = process_fee(transfer_money)
    free_money = current_user_money - transfer_money - money1
    #找出被转账用户的当前金额
    transfer_user_money = transfer_users()
    # 当前金额+转账金额=转账后的总金额
    add_money = transfer_user_money  + transfer_money

    #打开一个文件记录这些转账后的文件变动，然后更改为主文件
    w_file = open(r"E:\tmp(2).txt", "w")
    for line in user_lines:
        #匹配上当前用户就更改他的金额到文件
        if username in line:
            w_file.write(line.replace(str(current_user_money),str(free_money)))
        #匹配上被转账用户就更改他的金额到文件
        elif transfer_user in line:
            w_file.write(line.replace(str(transfer_user_money),str(add_money)))
        else:
            #其他没有匹配上的也写入文件
            w_file.write(line)
    #关闭文件
    w_file.close()
    #判断主文件是否存在，如果存在的话就删除然后改名
    if os.path.exists(r"E:\tmp.txt"):
        os.remove(r"E:\tmp.txt")
        os.rename(r"E:\tmp(2).txt",r"E:\tmp.txt")
    else:
        #不存在的话就直接修改名字
        os.rename(r"E:\tmp(2).txt", r"E:\tmp.txt")
        ###################################
    #输出当前用户的剩余金额
    print("当前用户：\033[1;32m%s\033[1m\n"
          "当前所剩余额：\033[1;32m%s\033[1m"
          "手续费扣除：\033[1;32m%s\033[1m" % (username,free_money,str(money1)))

def transfer_users():
    for line in user_lines:
        if transfer_user in line:
            l1 = line.strip("\n").split()
            #被转账用户的当前金额
            transfer_user_money = int(l1[2])
            return transfer_user_money

def inquire():
    money = current_user()
    #输出用户的金额
    print("当前用户：\033[1;32m%s\033[1m\n"
          "当前所剩余额：\033[1;32m%s\033[1m" % (username, money))

def save_money():
    #输入需要存储的金额
    save_mon = int(input("请输入你要存储的金额："))
    #遍历循环文件找出当前用户，并且获取当前用户的金额
    current_user_money = current_user()
    #当前金额+需要存储的金额=存储后的总金额
    total_money = current_user_money + save_mon
    write_file(total_money)
    #输出当前用户和当前用户的总金额
    print("当前用户：\033[1;32m%s\033[1m\n"
          "当前所剩余额：\033[1;32m%s\033[1m" % (username,total_money))

def take_money():
    #输入需要取款的金额
    take_mon = int(input("请输入你取款的金额："))
    #遍历循环文件找出当前用户，并且获取当前用户的金额
    current_user_money = current_user()
    #当前的总金额 - 取款的金额=剩余金额
    money1 = process_fee(take_mon)
    money = float(current_user_money) - float(take_mon) - money1
    write_file(money)
    print("当前用户：\033[1;32m%s\033[1m\n"
          "当前所剩余额：\033[1;32m%s\033[1m"
          "手续费扣除：\033[1;32m%s\033[1m" % (username,money,str(money1)))

def features():
    global featuresd
    featuresds = ["转账","查询","存钱","取款"]
    login_ret =  login()
    if login_ret == "登陆成功":
        while True:
            black("\n本银行系统有如下的功能列表")
            for feat in enumerate(featuresds,1):
                green(str(feat))
            feat_num = int(input("\n请选择你要使用的功能："))

            while feat_num > 4 or feat_num <= 0:
                red("该功能不存在，请重新输入")
                feat_num = int(input("\n请选择你要使用的功能："))
            if feat_num == 1:
                tranfer()
            elif feat_num == 2:
                inquire()
            elif feat_num == 3:
                save_money()
            elif feat_num == 4:
                take_money()
            exit_value = input("请问是否继续(y/n)：")
            if exit_value == "n" or exit_value == "no":
                red("\n欢迎再次使用自助查询系统，再见！")
                exit()
            else:
                continue
    else:
        red(login_ret)
features()
