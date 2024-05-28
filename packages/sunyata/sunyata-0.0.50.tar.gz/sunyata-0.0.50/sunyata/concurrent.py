from threading import Thread

class Concurrent(object):

    thlist = []

    @classmethod
    def go(cls, target, *args, **kwargs):
        th = Thread(target=target, args=args, kwargs=kwargs)
        cls.thlist.append(th)
        th.start()