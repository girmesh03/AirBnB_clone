#!/usr/bin/python3
""" Unittest for console """
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand
import unittest
import re


class TestConsole(unittest.TestCase):
    """
    Test the console.py file
    """

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertNotEqual(id, f.getvalue().strip())

    def test_show(self):
        """Test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(id))
            self.assertIn(id, f.getvalue())

    def test_destroy(self):
        """Test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User {}".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(id))
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn("[User]", f.getvalue())

    def test_update(self):
        """Test the update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {} first_name Guillaume".format(id))
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(id))
            self.assertIn("Guillaume", f.getvalue())


if __name__ == '__main__':
    unittest.main()
