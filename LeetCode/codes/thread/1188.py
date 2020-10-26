# time O(1)
# space O(1)
import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = []
        self.edit_lock = threading.Lock()
        self.push = threading.Semaphore(capacity)
        self.pop = threading.Semaphore(0)
    
    def enqueue(self, element: int) -> None:
        self.push.acquire()
        self.edit_lock.acquire()
        self.q.append(element)
        self.edit_lock.release()
        self.pop.release()
            

    def dequeue(self) -> int:
        self.pop.acquire()
        self.edit_lock.acquire()
        result = self.q.pop(0)
        self.edit_lock.release()
        self.push.release()
        return result

    def size(self) -> int:
        return len(self.q)