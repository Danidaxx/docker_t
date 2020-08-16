#!/usr/bin/env python
"""
model tests
"""

import sys
import os
sys.path.append(os.getcwd())


import unittest

## import model specific functions and variables
from model import *

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):   
        """
        test the train functionality
        """

        ## train the model
        data_dir = os.path.join(".","data","cs-train")
        
        model_train(data_dir, test=True)
        self.assertTrue(os.path.exists(data_dir))

    def test_02_load(self):
        """
        test the load functionality
        """                        
        ## train the model
        all_data, all_models = model_load(prefix='test', training=False)
        self.assertTrue(all_data is not None)

       
    def test_03_predict(self):
        """
        test the predict function input
        """
     
        ## ensure that a list can be passed
        country='all'
        year='2018'
        month='01'
        day='05'
     

        result = model_predict(country,year,month,day,all_models=None,test=True)   
        y_pred = result['y_pred']
        print(y_pred[0])
        self.assertTrue(y_pred[0] is not None)

          
### Run the tests
if __name__ == '__main__':
    unittest.main()
