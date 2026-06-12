from concurrent.futures import ThreadPoolExecutor

def load_batch(batch_id):
    return load_data_from_disk(f'batch_{batch_id}.npz')

with ThreadPoolExecutor(max_workers=4) as executor:
    batches = list(executor.map(load_batch, range(100)))