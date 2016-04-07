import unittest

from httmock import with_httmock

import not_real
import mocks.not_real

class TestNotReal(unittest.TestCase):

    @with_httmock(mocks.not_real.customer_scoring_query_mock)
    def test_get_customer_scoring_with_one_arguments(self):
        income = 60000

        results_w_one = not_real.get_customer_scoring(income)

        self.assertNotEqual(results_w_one, None)
        self.assertIsInstance(results_w_one, dict)
        self.assertTrue('propensity' in results_w_one)
        self.assertTrue('ranking' in results_w_one)
        self.assertEqual(results_w_one['ranking'], 'C')

    @with_httmock(mocks.not_real.customer_scoring_query_mock)
    def test_get_customer_scoring_with_two_arguments(self):
        income = 60000
        zipcode = 60626

        results_w_two = not_real.get_customer_scoring(income, zipcode)

        self.assertNotEqual(results_w_two, None)
        self.assertIsInstance(results_w_two, dict)
        self.assertTrue('propensity' in results_w_two)
        self.assertTrue('ranking' in results_w_two)
        self.assertEqual(results_w_two['ranking'], 'C')

    @with_httmock(mocks.not_real.customer_scoring_query_mock)
    def test_get_customer_scoring_with_three_arguments(self):
        income = 60000
        zipcode = 60626
        age = 27

        results_w_three = not_real.get_customer_scoring(income, zipcode, age)

        self.assertNotEqual(results_w_three, None)
        self.assertIsInstance(results_w_three, dict)
        self.assertTrue('propensity' in results_w_three)
        self.assertTrue('ranking' in results_w_three)
        self.assertEqual(results_w_three['ranking'], 'C')


    def test_get_customer_scroing_without_arguments(self):
        results = not_real.get_customer_scoring()

        self.assertEqual(results, None)

    @with_httmock(mocks.not_real.customer_scoring_query_mock)
    def test_get_customer_scoring_with_too_many_arguments(self):
        income = 60000
        zipcode = 60626
        age = 27

        results = not_real.get_customer_scoring(income, zipcode, age, 4, 5, 'taco')

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('propensity' in results)
        self.assertTrue('ranking' in results)
        self.assertEqual(results['ranking'], 'C')

    @with_httmock(mocks.not_real.customer_scoring_query_mock)
    def test_get_customer_scoring_with_keyword_argmuents(self):
        i = 60000 # prevent naming colisions
        z = 60626
        a = 27

        results_w_three = not_real.get_customer_scoring(income=i, zipcode=z, age=a)

        self.assertNotEqual(results_w_three, None)
        self.assertIsInstance(results_w_three, dict)
        self.assertTrue('propensity' in results_w_three)
        self.assertTrue('ranking' in results_w_three)
        self.assertEqual(results_w_three['ranking'], 'C')


if __name__ == '__main__':
    unittest.main()
