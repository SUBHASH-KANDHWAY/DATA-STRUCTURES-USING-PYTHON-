import hashlib
import datetime

class block:
    
    def  __init__(self, previousblock_hash, data , timestamp):
        self.previousblock_hash=previousblock_hash
        self.data=data
        self.timestamp=timestamp
        self.hash=self.get_hash()

    @staticmethod
    def create_genesis_block():
        return block("0" , "0" ,datetime.datetime.now())


    def get_hash(self):
        header_bin=(str(self.previousblock_hash)+str(self.data)+str(self.timestamp)).encode()
        inner_hash=hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash=hashlib.sha256(inner_hash).hexdigest()
        return outer_hash
print('all good')