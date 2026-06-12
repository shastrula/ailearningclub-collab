import configparser
import time

class ConfigManager:
    def __init__(self, path):
        self.path = path
        self.config = None
        self.mtime = 0
        self.load()
    
    def load(self):
        mtime = os.path.getmtime(self.path)
        if mtime > self.mtime:
            self.config = configparser.ConfigParser()
            self.config.read(self.path)
            self.mtime = mtime
    
    def get(self, section, key):
        self.load()  # Check for updates
        return self.config.get(section, key)