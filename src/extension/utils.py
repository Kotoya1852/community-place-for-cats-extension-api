from .serializers.message_response_serializer import MessageResponseSerializer


def message_response_deserialize(
    message_id: str | None = None, message: str | None = None, **kwargs
) -> MessageResponseSerializer:
    """
    レスポンスに設定するメッセージをデシリアライズします。
    """
    deserialize = MessageResponseSerializer(data={"message_id": message_id, "message": message})
    deserialize.is_valid()
    return deserialize.data
