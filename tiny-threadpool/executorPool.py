# !/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
import threading
import Queue


class Task():
    def run(self):
        return

    def callback(self):
        return


class Worker(threading.Thread):
    def __init__(self, task_queue, total_size, res_queue):

        threading.Thread.__init__(self)

        self.__total_size = total_size

        self.task_queue = task_queue

        self.res_queue = res_queue

        self.start()

    def run(self):

        """


        """
        while True:

            try:

                task, index = self.task_queue.get(block=False)

                res = task.run()

                self.res_queue.put((res, index))

                self.task_queue.task_done()

            except:

                break

            # print (str(1 - self.task_queue.qsize() / self.total_size) + '\n')


class FixedExecutor():
    def __init__(self, pool_size=10):

        self.__pool_size = pool_size

        self.__total_size = 0

        self.__threads = []

        self.__res = []

    def invoke_all(self, task_list):

        #初始化结果队列
        self.__init_result_queue()

        # 初始化任务队列
        self.__init_task_queue(task_list)

        # 初始化线程数组
        self.__init_threads(self.__pool_size)

        #等待所有任务执行完毕
        self.__task_queue.join()

        self.__get_result_list()

        return self.__res

    def __get_result_list(self):

        while self.__result_queue.qsize():
            res, index = self.__result_queue.get(block=False)

            self.__res[index] = res

    def __init_result_queue(self):

        self.__result_queue = Queue.Queue()

    def __init_task_queue(self, task_list):

        self.__task_queue = Queue.Queue()

        for i in range(len(task_list)):
            self.__task_queue.put((task_list[i], i))

            self.__res.append(None)

            self.__total_size += 1

    def __init_threads(self, pool_size):

        self.__threads = []

        for i in range(pool_size):
            self.__threads.append(Worker(self.__task_queue, self.__total_size, self.__result_queue))
