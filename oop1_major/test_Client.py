import unittest
from Client import Client


class TestOop1MajorClient(unittest.TestCase):
    # create the client class for use in add_credits functionality
    def setUp(self):
        # create a tuple of data to initialize the client class
        self.client_data = \
            ('Carrie Cordon',
             'carrie.cordon@gmail.com',
             '404-444-1111',
             'VISA',
             'PAID',
             'asdf',
             'Doesn\'t pay on time',
             'Give notice to pay.')

        # initialize client with that data above
        # this self.client can be used throughout the test sheet
        self.client = Client(self.client_data)

    # test the only method in the class to make sure the credits are added to the client properly
    def test_add_credits(self):
        # when the client is first initialized it should be 0 credits
        self.assertEqual(0, self.client.credits)

        # we add 5 credits through the add_credits method
        self.client.add_credits(5)

        # assert to make sure the client object has 5 credits now
        self.assertEqual(5, self.client.credits)

