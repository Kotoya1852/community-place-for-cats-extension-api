from django.test import TestCase

from .. import const, commands, query, models


class GetUserByUserIdTest(TestCase):
    """ユーザーIDからユーザー情報を取得するテスト"""

    def test_success(self):
        commands.create_user(100000000000000000, 100000000000000000, "テスト")

        user = query.get_user_by_user_id(100000000000000000)

        self.assertEqual(user.count(), 1)


class GetUserByUserIdAndServerId(TestCase):
    """サーバーIDとユーザーIDからユーザー情報を取得するテスト"""

    def test_success(self):
        commands.create_user(100000000000000000, 100000000000000000, "テスト")

        user = query.get_user_by_user_id_and_server_id(100000000000000000, 100000000000000000)

        self.assertEqual(user.server_id, 100000000000000000)
        self.assertEqual(user.user_id, 100000000000000000)


class GetToken(TestCase):
    """トークン取得テスト"""

    def test_success(self):
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        create_token = commands.create_token(100000000000000000)

        token = query.get_token(100000000000000000)

        self.assertEqual(token.token, create_token)
        self.assertEqual(token.user_id, 100000000000000000)


class GetExtensionValue(TestCase):
    """拡張値取得テスト"""

    def test_success(self):
        models.DiscordExtensionValues.objects.create(
            extension_id=const.EXPIRED_TOKEN_EXTENSION_ID, extension_value="5", publish_flag=True
        )

        extension_value = query.get_extension_value(const.EXPIRED_TOKEN_EXTENSION_ID)

        self.assertEqual(extension_value, "5")

    def test_success_none(self):
        extension_value = query.get_extension_value(const.EXPIRED_TOKEN_EXTENSION_ID)

        self.assertIsNone(extension_value)
