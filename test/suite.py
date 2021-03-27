import os.path
import sys
import unittest


if __name__ == '__main__':
    # Find and run all tests defined in paths matching ./*_test.py
    base_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(base_dir))
    suite = unittest.TestLoader().discover(base_dir, pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
