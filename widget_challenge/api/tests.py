from django.test import TestCase

from django.test import TestCase
from .models import Finish, Size, Widget, Order, OrderItem
from rest_framework.test import APIClient
from rest_framework import status
# see https://stackoverflow.com/a/43139407/6554056
from django.urls import reverse

class ModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.finish_name = "translucent"
        self.finish = Finish(name=self.finish_name)

    def test_model_can_create_a_finish(self):
        """Test the finish model can create a finish."""
        old_count = Finish.objects.count()
        self.finish.save()
        new_count = Finish.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.finish_data = {'name': 'translucent'}
        self.response = self.client.post(
            reverse('create'),
            self.finish_data,
            format="json"
        )
    
    def test_api_can_create_a_finish(self):
        """Test the api can create buckets."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_finish(self):
        """Test the api can get a given finish"""
        finish = Finish.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': finish.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, finish)

    def test_api_can_update_finish(self):
        """Test the api can update a given finish"""
        finish = Finish.objects.get()
        change_finish = {'name': 'matte'}
        res = self.client.put(
            reverse('details', kwargs={'pk': finish.id}),
            change_finish, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_finish(self):
        """Test the api can delete a finish"""
        finish = Finish.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': finish.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
