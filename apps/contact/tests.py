from django.test import TestCase


class SomeTests(TestCase):
    def test_math(self):
        self.assertEquals(2+2, 4)
