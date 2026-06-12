import numpy as np

def detect_drift(new_data, reference_data, threshold=0.1):
    ks_statistic, p_value = ks_2samp(
        new_data,
        reference_data
    )
    if ks_statistic > threshold:
        logger.warning('Model drift detected', ks=ks_statistic)
    return ks_statistic