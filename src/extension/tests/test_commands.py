from django.test import TestCase

from .. import commands, models


class CreateTokenTest(TestCase):
    """トークン生成テスト"""

    def test_success(self):
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        commands.create_token(100000000000000000)

        list = models.DiscordAuthenticationToken.objects.filter(user_id=100000000000000000)
        self.assertEqual(list.count(), 1)


class DeleteTokenTest(TestCase):
    """トークン削除テスト"""

    def test_success(self):
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        commands.create_token(100000000000000000)

        commands.delete_token(100000000000000000)
        list = models.DiscordAuthenticationToken.objects.filter(user_id=100000000000000000)
        self.assertEqual(list.count(), 0)
