from rest_framework import status
from django.test import TestCase
from django.utils import timezone
from .. import const, commands, models, query


class AuthViewsTest(TestCase):
    """AuthViewsのテスト"""

    url = "/api/auth"

    def test_post_success(self):
        # データ準備
        commands.create_user(100000000000000000, 100000000000000000, "テスト")

        # 実行
        response = self.client.post(self.url, {"server_id": 100000000000000000, "user_id": 100000000000000000})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_exists_token(self):
        # データ準備
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        user = query.get_user_by_user_id_and_server_id(100000000000000000, 100000000000000000)
        commands.create_token(user)

        # 実行
        response = self.client.post(self.url, {"server_id": 100000000000000000, "user_id": 100000000000000000})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_exists_token_expired(self):
        # データ準備
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        user = query.get_user_by_user_id_and_server_id(100000000000000000, 100000000000000000)
        models.DiscordAuthenticationToken.objects.create(
            user=user, generate_date_time=timezone.now() + timezone.timedelta(minutes=-61)
        )

        # 実行
        response = self.client.post(self.url, {"server_id": 100000000000000000, "user_id": 100000000000000000})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_exists_token_expired_set_ex_value(self):
        # データ準備
        commands.create_user(100000000000000000, 100000000000000000, "テスト")
        user = query.get_user_by_user_id_and_server_id(100000000000000000, 100000000000000000)
        models.DiscordExtensionValues.objects.create(
            extension_id=const.EXPIRED_TOKEN_EXTENSION_ID, extension_value="5", publish_flag=True
        )
        models.DiscordAuthenticationToken.objects.create(
            user=user, generate_date_time=timezone.now() + timezone.timedelta(minutes=-6)
        )

        # 実行
        response = self.client.post(self.url, {"server_id": 100000000000000000, "user_id": 100000000000000000})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_validate_error(self):
        # データ準備
        commands.create_user(100000000000000000, 100000000000000000, "テスト")

        # 実行
        response = self.client.post(self.url, {})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNone(response.data["message_id"])
        self.assertEqual(response.data["message"], "不正なリクエストです")

    def test_post_not_exists_user_error(self):
        # 実行
        response = self.client.post(self.url, {"server_id": 100000000000000000, "user_id": 100000000000000000})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNone(response.data["message_id"])
        self.assertEqual(response.data["message"], "ユーザーが存在しません")


class MemberViewsTest(TestCase):
    """MemberViewsのテスト"""

    url = "/api/member"

    def test_post_success(self):
        # 実行
        response = self.client.post(
            self.url, {"server_id": 100000000000000000, "user_id": 100000000000000000, "user_name": "テスト"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_validate_error(self):
        # 実行
        response = self.client.post(self.url, {})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNone(response.data["message_id"])
        self.assertEqual(response.data["message"], "不正なリクエストです")

    def test_post_exists_user_error(self):
        # データ準備
        commands.create_user(100000000000000000, 100000000000000000, "テスト")

        # 実行
        response = self.client.post(
            self.url, {"server_id": 100000000000000000, "user_id": 100000000000000000, "user_name": "テスト"}
        )

        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertIsNone(response.data["message_id"])
        self.assertEqual(response.data["message"], "既に登録済です")

    def test_delete_success(self):
        # データ準備
        commands.create_user(100000000000000000, 100000000000000000, "テスト")

        # 実行
        response = self.client.delete(f"{self.url}?user_id=100000000000000000&server_id=100000000000000000")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_validate_error(self):
        # 実行
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_not_exists_user_error(self):
        # 実行
        response = self.client.delete(f"{self.url}?user_id=100000000000000000&server_id=100000000000000000")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
