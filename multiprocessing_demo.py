# -*- coding: utf-8 -*-
import multiprocessing
import datetime,time
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def worker(ip):
    ctime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # time.sleep(ip)
    print(ctime,ip)



if __name__ == '__main__':
    jobs = []
    ip_list = ["1.1.1.1","1.1.1.12","1.1.1.3","1.1.1.5","1.1.1.100","1.1.1.8"]
    for i in range(100):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
        #p.join()
    for j in jobs:
        j.join()
    print("ok")
