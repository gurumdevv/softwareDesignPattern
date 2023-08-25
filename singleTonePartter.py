class Borg:
    __shared_state = {"1", "2"}
    def __init__(self):
        self.x  = 1
        self.__dict__ = self.__shared_state
        pass
    
b = Borg()
b1 = Borg()
b.x = 4