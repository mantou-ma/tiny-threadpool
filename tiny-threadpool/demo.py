# !/usr/bin/env python
# -*- coding:utf-8 -*-
import executorPool

class MyTask(executorPool.Task):

    def __init__(self, *param):

        self.param = param

    def run(self):

        return


if __name__ == '__main__':

    thread_pool = executorPool.FixedExecutor(3)

    tasks = []

    for i in range(1000):

        tasks.append(MyTask(i, i))

    thread_pool.invoke_all(tasks)

    # exit(0)

