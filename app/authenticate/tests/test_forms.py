from django.test import TestCase

class TestTestsWork(TestCase):

  def test_true_is_true(self):
      self.assertEqual(True, True)