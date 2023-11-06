from rest_framework import serializers


class MessageResponse(object):
    def __init__(self, message_id, message):
        self.message_id = message_id
        self.message = message


class MessageResponseSerializer(serializers.Serializer):
    """
    レスポンスに含めるメッセージのシリアライザー
    """

    message_id = serializers.CharField(required=False, allow_null=True, max_length=10)
    """ メッセージID """
    message = serializers.CharField(required=False, allow_null=True, max_length=256)
    """ メッセージ """

    def create(self, validated_data):
        return MessageResponse(**validated_data)
