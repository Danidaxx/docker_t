#!/usr/bin/env python
"""
api tests

"""

import sys
import os
import unittest
import requests
import re
from ast import literal_eval
import numpy as np
import json

port = 8080
import requests
files = {'country': (None, 'all')}
try:
    r = requests.post('http://127.0.0.1:{}/predict'.format(port), files=files)
    server_available = True
except:
    server_available = False
    
## test class for the main window function
class ApiTest(unittest.TestCase):
    """
    test the essential functionality
    """
  
    
    @unittest.skipUnless(server_available,"local server is not running")
    def test_01_predict(self):
        """
        test the predict functionality
        """

        response = json.loads(r.text)
        self.assertTrue(response['y_pred'] is not None)
 
        
### Run the tests
if __name__ == '__main__':
    unittest.main()
