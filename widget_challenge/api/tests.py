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

class FinishViewTestCase(TestCase):
    """Test suite for the api views."""

    # ===== TEST FINISHES

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.finish_data = {'name': 'translucent'}
        self.response = self.client.post(
            reverse('finish_create'),
            self.finish_data,
            format="json"
        )
    
    def test_api_can_create_a_finish(self):
        """Test the api can create finishes."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_finish(self):
        """Test the api can get a given finish"""
        finish = Finish.objects.get()
        response = self.client.get(
            reverse('finish_details', kwargs={'pk': finish.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, finish)

    def test_api_can_update_finish(self):
        """Test the api can update a given finish"""
        finish = Finish.objects.get()
        change_finish = {'name': 'matte'}
        res = self.client.put(
            reverse('finish_details', kwargs={'pk': finish.id}),
            change_finish, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_finish(self):
        """Test the api can delete a finish"""
        finish = Finish.objects.get()
        response = self.client.delete(
            reverse('finish_details', kwargs={'pk': finish.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class SizeViewTestCase(TestCase):
    """Test suite for the api views."""

    # ===== TEST SIZES

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.size_data = {'name': 'ginormous'}
        self.response = self.client.post(
            reverse('size_create'),
            self.size_data,
            format="json"
        )
    
    def test_api_can_create_a_size(self):
        """Test the api can create sizes."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_size(self):
        """Test the api can get a given size"""
        size = Size.objects.get()
        response = self.client.get(
            reverse('size_details', kwargs={'pk': size.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, size)

    def test_api_can_update_size(self):
        """Test the api can update a given size"""
        size = Size.objects.get()
        change_size = {'name': 'itty-bitty'}
        res = self.client.put(
            reverse('size_details', kwargs={'pk': size.id}),
            change_size, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_size(self):
        """Test the api can delete a size"""
        size = Size.objects.get()
        response = self.client.delete(
            reverse('size_details', kwargs={'pk': size.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class WidgetViewTestCase(TestCase):
    """Test suite for the api views."""

    # ===== TEST WIDGETS

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        # insert size value for test
        self.size_data = {'name': 'ginormous'}
        self.response = self.client.post(
            reverse('size_create'),
            self.size_data,
            format="json"
        )        
        size = Size.objects.get()
        
        # insert finish value for test
        self.finish_data = {'name': 'mauve'}
        self.response = self.client.post(
            reverse('finish_create'),
            self.size_data,
            format="json"
        )        
        finish = Finish.objects.get()

        # insert widget
        self.widget_data = {'name': 'test widget', 'inventory': 15, 'size': size.id, 'finish': finish.id}
        self.response = self.client.post(
            reverse('widget_create'),
            self.widget_data,
            format="json"
        )
    
    def test_api_can_create_a_widget(self):
        """Test the api can create widgets."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_widget(self):
        """Test the api can get a given widget"""
        widget = Widget.objects.get()
        response = self.client.get(
            reverse('widget_details', kwargs={'pk': widget.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, widget)

    # def test_api_can_update_widget(self):
    #     """Test the api can update a given widget"""
    #     widget = Widget.objects.get()
    #     print("[175] widget.name: " + str(widget.name))
    #     change_widget = {'name': 'new and improved'}
    #     res = self.client.put(
    #         reverse('widget_details', kwargs={'pk': widget.id}),
    #         change_widget, format='json'
    #     )
    #     print("[181] res: " + str(res))
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_widget(self):
        """Test the api can delete a widget"""
        widget = Widget.objects.get()
        response = self.client.delete(
            reverse('widget_details', kwargs={'pk': widget.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class OrderViewTestCase(TestCase):
    """Test suite for the api views."""

    # ===== TEST ORDERS

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.order_data = {}
        self.response = self.client.post(
            reverse('order_create'),
            self.order_data,
            format="json"
        )
    
    def test_api_can_create_a_order(self):
        """Test the api can create orders."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_order(self):
        """Test the api can get a given order"""
        order = Order.objects.get()
        response = self.client.get(
            reverse('order_details', kwargs={'pk': order.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, order)

    def test_api_can_delete_order(self):
        """Test the api can delete a order"""
        order = Order.objects.get()
        response = self.client.delete(
            reverse('order_details', kwargs={'pk': order.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class OrderItemViewTestCase(TestCase):
    """Test suite for the api views."""

    # ===== TEST ORDERITEMS

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        # insert size value for test
        self.size_data = {'name': 'ginormous'}
        self.response = self.client.post(
            reverse('size_create'),
            self.size_data,
            format="json"
        )        
        size = Size.objects.get()
        
        # insert finish value for test
        self.finish_data = {'name': 'mauve'}
        self.response = self.client.post(
            reverse('finish_create'),
            self.size_data,
            format="json"
        )        
        finish = Finish.objects.get()

        # insert widget
        self.widget_data = {'name': 'test widget', 'inventory': 15, 'size': size.id, 'finish': finish.id}
        self.response = self.client.post(
            reverse('widget_create'),
            self.widget_data,
            format="json"
        )
        widget = Widget.objects.get()

        # insert order
        self.order_data = {}
        self.response = self.client.post(
            reverse('order_create'),
            self.order_data,
            format="json"
        )
        order = Order.objects.get()

        self.orderitem_data = {'count': 1, 'widget': widget.id, 'order': order.id}
        self.response = self.client.post(
            reverse('orderitem_create'),
            self.orderitem_data,
            format="json"
        )
    
    def test_api_can_create_a_orderitem(self):
        """Test the api can create orderitems."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_orderitem(self):
        """Test the api can get a given orderitem"""
        orderitem = OrderItem.objects.get()
        response = self.client.get(
            reverse('orderitem_details', kwargs={'pk': orderitem.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, orderitem)

    # def test_api_can_update_orderitem(self):
    #     """Test the api can update a given orderitem"""
    #     orderitem = OrderItem.objects.get()
    #     change_orderitem = {'count': 22}
    #     res = self.client.put(
    #         reverse('orderitem_details', kwargs={'pk': orderitem.id}),
    #         change_orderitem, format='json'
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_orderitem(self):
        """Test the api can delete a orderitem"""
        orderitem = OrderItem.objects.get()
        response = self.client.delete(
            reverse('orderitem_details', kwargs={'pk': orderitem.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
