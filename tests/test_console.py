#!/usr/bin/python3
"""Unittests for Console"""


import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Tests for the HBNB console"""

    def setUp(self):
        """Setup function"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Teardown function"""
        self.console.do_quit("")

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual("", f.getvalue().strip())

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertEqual("", f.getvalue().strip())

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id = f.getvalue().strip()
            self.assertTrue(len(id) > 0)
            self.assertFalse(id in storage.all().keys())

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(id))
            self.assertTrue("BaseModel" in f.getvalue().strip())
            self.assertTrue(id in f.getvalue().strip())

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            id2 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertTrue("BaseModel" in f.getvalue().strip())
            self.assertTrue(id1 in f.getvalue().strip())
            self.assertTrue("User" in f.getvalue().strip())
            self.assertTrue(id2 in f.getvalue().strip())

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel {} name 'test'".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(id))
            self.assertTrue("test" in f.getvalue().strip())

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(id))
            self.assertEqual("** no instance found **", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
