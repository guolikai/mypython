# coding=utf-8
import json

data1 = {"name":"张三", "age":"17"}
data2 = {"name":"李四", "age":"18"}
print(json.dumps(data2, indent=2, sort_keys=True, ensure_ascii=False))
# with open("1.txt",'w+',encoding='utf-8') as f:
#     json.dump(data1, f)   # 写为一行
    # json.dump(',', f)
    #json.dump(data1, f,indent=2,sort_keys=True, ensure_ascii=False)  # 写为多行
# with open("1.txt",'r', encoding='utf-8') as f:
#     data = json.load(f)
#     print(data)
"""
with open("1.txt",'w', encoding='utf-8') as f:
    json.dump(data1, f,ensure_ascii=False)
    json.dump('|', f,ensure_ascii=False)
    json.dump(data2, f,ensure_ascii=False)

with open("1.txt",'r', encoding='utf-8') as f:
    datas = f.readlines()
    datas_strings = str(datas).replace("['","").replace("']","").replace('}"|"{',"}|{")
    for data in datas_strings.split('|'):
        print(data)
        json_data = json.loads(data)
        print(type(json_data), json_data)

"""
with open("1.txt",'a', encoding='utf-8') as f:
    f.write(str(data1)+"\n"+str(data2)+"\n")

with open("1.txt",'r', encoding='utf-8') as f:
    datas = f.readlines()
    print(datas)
    for data in datas:
        data = data.replace("\n","")
        print(type(data),data)
        json_data = eval(data)
        print(type(json_data), json_data)
        # data = data.replace("\n","").replace("'","\"")
        # print(type(data),data)
        # json_data = json.loads(data)
        # print(type(json_data), json_data)

