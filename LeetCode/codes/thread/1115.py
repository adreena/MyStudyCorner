import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.print_foo = threading.Semaphore(1)
        self.print_bar = threading.Semaphore(0)
        self.lock = threading.Lock()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            self.print_foo.acquire()
            # self.lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            # self.lock.release()
            self.print_bar.release()
            


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            self.print_bar.acquire()
            # self.lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            # self.lock.release()
            self.print_foo.release()