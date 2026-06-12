from typing import Literal

def create_optimizer(
    method: Literal['adam', 'sgd', 'rmsprop'],
    lr: float
) -> Optimizer:
    optimizers = {
        'adam': AdamOptimizer,
        'sgd': SGDOptimizer,
        'rmsprop': RMSpropOptimizer
    }
    return optimizers[method](lr)