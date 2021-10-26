import time


def calRunningTime(fn):
    start = time.time()
    fn()
    end = time.time()
    print('运行耗时{}秒'.format(end=start))
