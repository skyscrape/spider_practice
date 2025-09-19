import time

import threading



def get_detail():
    print('开始获取详情')
    time.sleep(2)
    print('详情获取完毕')


def get_list():
    print('开始获取列表\n')
    time.sleep(2)
    print('列表获取完毕\n')

start_time = time.time()
t1 = threading.Thread(target=get_detail)
t2 = threading.Thread(target=get_list)
t1.start()
t2.start()
t1.join()
t2.join()
t1.setDaemon(True)
t2.setDaemon(True)

print('总耗时:', time.time() - start_time)