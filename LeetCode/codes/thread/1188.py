# time O(1)
# space O(1)
import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = []
        self.enq_lock = threading.Semaphore(capacity)
        self.deq_lock = threading.Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.enq_lock.acquire()
        self.q.append(element)
        self.deq_lock.release()

    def dequeue(self) -> int:
        self.deq_lock.acquire()
        val = self.q.pop(0)
        self.enq_lock.release()
        return val

    def size(self) -> int:
        return len(self.q)