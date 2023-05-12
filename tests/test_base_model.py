#!/usr/bin/python3

import unittest
import datetime
from uuid import UUID
from models.base_model import BaseModel

class test_basemodel(unittest.TestCase):


     #def test_str(self):
        # """ """
         #i = self.value()
         #self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
          #               i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    if __name__ == "__main__":

        unittest.main()
