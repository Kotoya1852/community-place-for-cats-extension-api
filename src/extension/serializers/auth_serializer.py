from rest_framework import serializers


class AuthPostRequest(object):
    def __init__(self, server_id, user_id):
        self.server_id = server_id
        self.user_id = user_id


class AuthPostRequestSerializer(serializers.Serializer):
    """
    トークン生成リクエストシリアライザー
    """

    server_id = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=100000000000000000,
        max_value=999999999999999999,
    )

    user_id = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=100000000000000000,
        max_value=999999999999999999,
    )

    def create(self, validated_data):
        return AuthPostRequest(**validated_data)


class AuthPostResponse(object):
    def __init__(self, token):
        self.token = token


class AuthPostResponseSerializer(serializers.Serializer):
    """
    トークン生成レスポンスシリアライザー
    """

    token = serializers.UUIDField(required=True, allow_null=False)

    def create(self, validated_data):
        return AuthPostResponse(**validated_data)
