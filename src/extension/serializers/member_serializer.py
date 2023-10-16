from rest_framework import serializers


class MemberPostRequest(object):
    def __init__(self, server_id, user_id, user_name):
        self.server_id = server_id
        self.user_id = user_id
        self.user_name = user_name


class MemberPostRequestSerializer(serializers.Serializer):
    """
    ユーザー登録リクエストシリアライザー
    """

    server_id = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=100000000000000000,
        max_value=999999999999999999,
    )
    """ サーバーID（ギルドID） """

    user_id = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=100000000000000000,
        max_value=999999999999999999,
    )
    """ ユーザーID """

    user_name = serializers.CharField(required=True, allow_null=False, max_length=120)
    """ ユーザー名 """

    def create(self, validated_data):
        return MemberPostRequest(**validated_data)


class MemberDeleteRequest(object):
    def __init__(self, server_id, user_id):
        self.server_id = server_id
        self.user_id = user_id


class MemberDeleteRequestSerializer(serializers.Serializer):
    """
    ユーザー削除リクエストシリアライザー
    """

    server_id = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=100000000000000000,
        max_value=999999999999999999,
    )
    """ サーバーID（ギルドID） """

    user_id = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=100000000000000000,
        max_value=999999999999999999,
    )
    """ ユーザーID """

    def create(self, validated_data):
        return MemberDeleteRequest(**validated_data)
