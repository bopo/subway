from __future__ import absolute_import

from collections import defaultdict
from threading import Thread

from Queue import Empty, Queue


class Worker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.results = defaultdict(list)

    def run(self):
        while True:
            try:
                ident, func, args, kwargs = self.queue.get_nowait()
            except Empty:
                break

            try:
                result = func(*args, **kwargs)
                self.results[ident].append(result)
            except Exception as e:
                self.results[ident].append(e)
            finally:
                self.queue.task_done()

        return self.results


class ThreadPool(object):
    def __init__(self, workers=10):
        self.queue = Queue()
        self.workers = []
        self.tasks = []
        for worker in xrange(workers):
            self.workers.append(Worker(self.queue))

    def add(self, ident, func, args=None, kwargs=None):
        if args is None:
            args = ()
        if kwargs is None:
            kwargs = {}
        task = (ident, func, args, kwargs)
        self.tasks.append(ident)
        self.queue.put_nowait(task)

    def join(self):
        for worker in self.workers:
            worker.start()

        results = defaultdict(list)
        for worker in self.workers:
            worker.join()
            for k, v in worker.results.items():
                results[k].extend(v)
        return results
