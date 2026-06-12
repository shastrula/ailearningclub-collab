import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

model_path = config['models']['path']
batch_size = config['training']['batch_size']