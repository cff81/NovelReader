from threading import Thread, Event
import time
 
 
class MyThread(Thread):
    def __init__(self, target, name=None, group=None,
                 args=(),daemon=None):
        Thread.__init__(self, group=group, target=target, name=name,
                        args=args, kwargs=None, daemon=daemon)
        self.target = target
        self.args = args
        self.__running = Event()
        self.__running.set()
        self.__flag = Event()
 
    def run(self):
        """
            功能:重写父类的run方法【当外部调用own_thread.start()开启线程就会自动运行run方法】
            特殊说明:父类run方法的三个属性【_target、_args、_kwargs】都是私有属性【下划线开头】,无法继承！
                    所以这里不能直接super().run(),而是直接调用target方法即可
        """
        while self.__running.isSet():
            self.__flag.wait()
            time.sleep(1)
            self.target(*self.args)
 
    def stop(self):
        self.__running.clear()
        
    def pause(self):
        self.__flag.clear()
    
    def restart(self):
        self.__flag.set()
    
    def exchange(self):
        if self.__flag.is_set():
            self.__flag.clear()
        else:
            self.__flag.set()
