from django.test import TestCase
from django.contrib.auth.models import User
from .models import Receipt
from django.urls import reverse

class ReceiptModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_create_receipt(self):
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Test Item 1, Test Item 2',
            total_amount=100.0
        )
        self.assertEqual(receipt.store_name, 'Test Store')

    def test_update_receipt(self):
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Test Item 1, Test Item 2',
            total_amount=100.0
        )

        receipt.store_name = 'Updated Store'
        receipt.save()
        updated_receipt = Receipt.objects.get(pk=receipt.pk)
        self.assertEqual(updated_receipt.store_name, 'Updated Store')

    def test_delete_receipt(self):
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Test Item 1, Test Item 2',
            total_amount=100.0
        )
        receipt.delete()
        with self.assertRaises(Receipt.DoesNotExist):
            Receipt.objects.get(pk=receipt.pk)

    def test_authenticated_user_can_access_receipts(self):
        # Create another user
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Create a receipt for the authenticated user
        Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Test Item 1, Test Item 2',
            total_amount=100.0
        )

        # Access the receipt list view for the authenticated user
        response = self.client.get(reverse('receipt_list'))

        # Check if the response contains the receipt for the authenticated user
        self.assertContains(response, 'Test Store')
