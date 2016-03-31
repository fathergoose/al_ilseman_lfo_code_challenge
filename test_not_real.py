import unittest

from httmock import with_httmock

import not_real
import mocks.not_real

class TestNotReal(unittest.TestCase):

    @with_httmock(mocks.not_real.customer_scoring_query_mock)
    def test_get_customer_scoring(self):
        income = 60000
        zipcode = 60626
        age = 27

        results = not_real.get_customer_scoring(income, zipcode, age)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('propensity' in results)
        self.assertTrue('ranking' in results)
        self.assertEqual(results['ranking'], 'C')

    def test_get_customer_scroing_without_arguments(self):
        results = not_real.get_customer_scoring()

        self.assertNotEqual(results, None)

if __name__ == '__main__':
    unittest.main()
