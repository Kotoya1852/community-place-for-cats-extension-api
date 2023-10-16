from uuid import UUID
from .models import DiscordAuthenticationToken, DiscordMemberMaster


def create_token(user_id: int) -> UUID:
    """
    指定されたユーザーIDのトークンを作成し、返却します。

    Args:
        user_id: discordユーザーID
    """
    token = DiscordAuthenticationToken.objects.create(user_id=user_id)
    return token.token


def delete_token(user_id: int):
    """
    指定されたユーザーIDのトークンを全て削除します。

    Args:
        user_id: discordユーザーID
    """
    tokens = DiscordAuthenticationToken.objects.filter(user_id=user_id)
    tokens.delete()


def create_user(user_id: int, server_id: int, user_name: str):
    """
    ユーザーを作成します。

    Args:
        user_id: discordユーザーID
        server_id: discordサーバーID
        user_name: ユーザー名
    """
    DiscordMemberMaster.objects.create(user_id=user_id, server_id=server_id, user_name=user_name)
