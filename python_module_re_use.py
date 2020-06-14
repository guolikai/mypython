    import re
    string="terway-vlan   31        31        21      31           29          <none>          16d"
    shuzi = re.findall("\d+",string)        #\d+如果需要匹配一位或者多位数的数字时用

    kongbai = re.findall("\S+",string)       #\S匹配任何非空白字符，它相当于类[^\t\n\r\f\v]
    print(shuzi,kongbai)

    a = re.split(r'\s+', string)
    info = " ".join(re.split(r'\s+', string))
    print("'%s'" % info)
