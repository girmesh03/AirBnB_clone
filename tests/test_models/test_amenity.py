#!/usr/bin/python3
import unittest
from models.amenity import Amenity

"""
Unittest Module for Amenity class
"""


class TestAmenity(unittest.TestCase):
    ''' Unittest for Amenity class '''

    def test_object_Instantiation(self):
        ''' Tests if Amenity object is properly instantiated '''
        self.amenity = Amenity()

    def test_attributes(self):
        ''' Tests if Amenity class attributes exist '''
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")

    def test_save(self):
        ''' Tests if Amenity class saves updates '''
        self.amenity = Amenity()
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_str(self):
        ''' Tests if __str__ method returns a string '''
        self.amenity = Amenity()
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id), self.amenity.__dict__)
        self.assertEqual(str(s), str(self.amenity))


if __name__ == '__main__':
    unittest.main()
