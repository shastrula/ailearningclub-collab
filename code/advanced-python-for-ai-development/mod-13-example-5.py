class Config(metaclass=Singleton):
    def __init__(self):
        self.debug = False
        self.batch_size = 32
    
    def set_debug(self, enabled):
        self.debug = enabled
    
    @classmethod
    def instance(cls):
        return cls()