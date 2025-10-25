from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from home.models import Restaurant

class RestaurantInfoAPITest(APITestCase):

    def test_get_restaurant_info(self):
        # Create a sample Restaurant instance
        restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test St',
            phone_number='1234567890',
            email='test@example.com',
            is_active=True
        )

        # Make GET request to the restaurant info API
        url = '/api/restaurant-info/'  # Replace with the actual endpoint if different
        response = self.client.get(url)

        # Assert the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the returned data matches the sample Restaurant
        self.assertEqual(response.data[0]['name'], restaurant.name)
        self.assertEqual(response.data[0]['address'], restaurant.address)
        self.assertEqual(response.data[0]['phone_number'], restaurant.phone_number)
        self.assertEqual(response.data[0]['email'], restaurant.email)
        self.assertEqual(response.data[0]['is_active'], restaurant.is_active)
