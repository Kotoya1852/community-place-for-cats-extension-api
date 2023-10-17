from django.test import TestCase

from .. import commands, models, query


class CreateTokenTest(TestCase):
    """トークン生成テスト"""

    def test_success(self):
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        user = query.get_user_by_user_id_and_server_id(100000000000000000, 100000000000000000)
        commands.create_token(user)

        list = models.DiscordAuthenticationToken.objects.filter(user=user)
        self.assertEqual(list.count(), 1)


class DeleteTokenTest(TestCase):
    """トークン削除テスト"""

    def test_success(self):
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        user = query.get_user_by_user_id_and_server_id(100000000000000000, 100000000000000000)
        commands.create_token(user)

        commands.delete_token(100000000000000000)
        list = models.DiscordAuthenticationToken.objects.filter(user_id=100000000000000000)
        self.assertEqual(list.count(), 0)
