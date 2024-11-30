#!/usr/bin/env python3
"""
"""

import numpy as np


def preprocess(data):
    # Perform your data conditioning
    data = [float(value) for value in data['values']]
    data = np.array(data).reshape(1, -1)
    return data
