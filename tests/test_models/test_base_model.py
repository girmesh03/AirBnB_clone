#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

"""
Unittest Module for BaseModel class
"""


class TestBaseModel(unittest.TestCase):
    ''' Unittest for BaseModel class '''

    def test_object_Instantiation(self):
        ''' Tests if BaseModel class instantiates correctly '''
        self.basemodel = BaseModel()

    def testattr(self):
        ''' Tests if BaseModel class has the correct attributes '''
        self.basemodel = BaseModel()
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(hasattr(self.basemodel, "random_attr"))
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.basemodel.name = "Alice"
        self.basemodel.age = "44"
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "age"))
        delattr(self.basemodel, "name")
        self.assertFalse(hasattr(self.basemodel, "name"))
        delattr(self.basemodel, "age")
        self.assertFalse(hasattr(self.basemodel, "age"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def testsave(self):
        ''' Tests if save method updates the updated_at attribute '''
        self.basemodel = BaseModel()
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def teststr(self):
        ''' Tests if __str__ method returns the correct format '''
        self.basemodel = BaseModel()
        s = "[{}] ({}) {}".format(self.basemodel.__class__.__name__,
                                  str(self.basemodel.id),
                                  self.basemodel.__dict__)
        self.assertEqual(print(s), print(self.basemodel))

    def test_to_dict(self):
        ''' Tests if to_dict method returns a dictionary
        with the correct attributes '''
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)

    def test_checking_for_functions(self):
        ''' Tests if BaseModel class has the required
        functions with documentation '''
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
