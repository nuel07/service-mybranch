#!/usr/bin/python3
"""
Defines unittests for the review model
"""

from datetime import datetime
import inspect
import models
from models import review
from models.base_model import BaseModel
import pep8
import unittest
Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and pep style of Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_funcs = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for the review.py module docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in Review methods"""
        for func in self.review_funcs:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestReview(unittest.TestCase):
    """Test the Review class"""
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "creation"))
        self.assertTrue(hasattr(review, "update"))

    def test_branch_id_attr(self):
        """Test Review has attr branch_id, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "branch_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.branch_id, None)
        else:
            self.assertEqual(review.branch_id, "")

    def test_user_id_attr(self):
        """Test Review has attr user_id, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.user_id, None)
        else:
            self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """Test Review has attr text, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if models.storage_t == 'db':
            self.assertEqual(review.text, None)
        else:
            self.assertEqual(review.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        rvw = Review()
        new_dct = rvw.to_dict()
        self.assertEqual(type(new_dct), dict)
        self.assertFalse("_sa_instance_state" in new_dct)
        for attr in rvw.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dct)
        self.assertTrue("__class__" in new_dct)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        rvw = Review()
        new_dct = rvw.to_dict()
        self.assertEqual(new_dct["__class__"], "Review")
        self.assertEqual(type(new_d["create"]), str)
        self.assertEqual(type(new_dct["update"]), str)
        self.assertEqual(new_dct["creation"], r.creation.strftime(t_format))
        self.assertEqual(new_dct["update"], r.update.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))

if __name__ == "__main__":
    unittest.main
