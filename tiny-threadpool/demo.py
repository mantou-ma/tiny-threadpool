# !/usr/bin/env python
# -*- coding:utf-8 -*-
import executorPool


class MyTask(executorPool.Task):
    def __init__(self, *param):
        self.param = param

    def run(self):
        # print '-'.join([str(self.param[0]), str(self.param[1])]) + '\n'
        return self.param[0]


if __name__ == '__main__':

    thread_pool = executorPool.FixedExecutor(3)

    tasks = []

    for i in range(100):
        tasks.append(MyTask(i, i + 1))

    res = thread_pool.invoke_all(tasks)

    print str(res)

    # exit(0)

