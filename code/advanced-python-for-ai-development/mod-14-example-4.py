class BatchProcessor:
    def __init__(self, batch_size=32):
        self.batch_size = batch_size
    
    def process(self, data):
        batches = [
            data[i:i+self.batch_size]
            for i in range(0, len(data), self.batch_size)
        ]
        return [self.process_batch(b) for b in batches]
    
    def process_batch(self, batch):
        return self.model.predict(batch)