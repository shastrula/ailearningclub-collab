from typing import Union, Callable, TypeVar, Generic
import numpy as np

T = TypeVar('T')

def process_data(
    data: np.ndarray,
    processor: Callable[[np.ndarray], np.ndarray],
    cache: dict[str, np.ndarray]
) -> tuple[np.ndarray, dict]:
    result = processor(data)
    return result, cache