from django.test import TestCase
from .. import utils


class MessageResponseDeserialize(TestCase):
    def test_success(self):
        serializer = utils.message_response_deserialize(message_id="TEST0001", message="MESSAGE")

        self.assertEqual(serializer["message_id"], "TEST0001")
        self.assertEqual(serializer["message"], "MESSAGE")
