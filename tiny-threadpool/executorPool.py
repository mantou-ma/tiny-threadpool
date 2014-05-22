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

    def __init__(self, task_queue, total_size):

        threading.Thread.__init__(self)

        self.total_size = total_size

        self.task_queue = task_queue

        self.start()

    def run(self):

        while True:

            try:

                task = self.task_queue.get(block=False)

                task.run()

                task.callback()

                self.task_queue.task_done()

            except:

                break

            print (str(1 - self.task_queue.qsize()/self.total_size) + '\n')


class FixedExecutor():

    def __init__(self, pool_size = 10):

        self.pool_size = pool_size

        self.total_size = 0

        self.threads = []


    def invoke_all(self, task_list):

        # 初始化任务队列
        self.__init_task_queue(task_list)

        # 初始化线程数组
        self.__init_threads(self.pool_size)


    def __init_task_queue(self, task_list):

        self.task_queue = Queue.Queue()

        for task in task_list:

            self.task_queue.put(task)

            self.total_size += 1


    def __init_threads(self, pool_size):

        self.threads = []

        for i in range(pool_size):

            self.threads.append(Worker(self.task_queue, self.total_size))
