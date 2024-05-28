import numpy as np
import tensorflow as tf
from module import *  # Import all functions from module.py

def test_matrix():
  data = [1, 2, 3, 4]
  expected = np.array([1, 2, 3, 4])
  assert np.array_equal(matrix(data), expected)

def test_ghost():
  shape = (2, 3)
  expected = np.zeros(shape)
  assert np.array_equal(ghost(shape), expected)

def test_squad():
  shape = (4, 5)
  expected = np.ones(shape)
  assert np.array_equal(squad(shape), expected)

# Add similar test functions for other functions in module.py

def test_random_uniform():
  shape = (3, 3)
  minval = 5
  maxval = 10
  result = random_uniform(shape, minval, maxval)
  assert tf.rank(result).numpy() == 2  # Check for tensor with rank 2 (matrix)
  assert all(minval <= val <= maxval for val in result.numpy().flatten())  # Check values within range

def test_random_normal():
  shape = (2, 2)
  mean = 2.0
  stddev = 0.5
  result = random_normal(shape, mean, stddev)
  assert tf.rank(result).numpy() == 2  # Check for tensor with rank 2 (matrix)
  # Due to randomness, cannot directly compare values. 
  # You can add checks for standard deviation and mean if needed.

# Add similar test functions for other TensorFlow functions

if __name__ == "__main__":
  test_matrix()
  test_ghost()
  test_squad()
  # Call other test functions here
  test_random_uniform()
  test_random_normal()
  # Call other TensorFlow test functions here
  print("All tests passed!")
