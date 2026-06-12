import unittest
import numpy as np

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.X = np.random.randn(100, 10)
        self.y = np.random.randint(0, 2, 100)
    
    def test_predict_shape(self):
        pred = self.model.predict(self.X)
        self.assertEqual(pred.shape, (100,))
    
    def test_predict_range(self):
        pred = self.model.predict(self.X)
        self.assertTrue((pred >= 0).all() and (pred <= 1).all())