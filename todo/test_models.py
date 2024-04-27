from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item') # this creates a generic item for testing
        self.assertFalse(item.done)
        