from concurrent.futures import ProcessPoolExecutor

def preprocess_batch(batch):
    return expensive_preprocessing(batch)

with ProcessPoolExecutor(max_workers=4) as executor:
    processed = list(executor.map(preprocess_batch, data_batches))