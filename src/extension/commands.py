from uuid import UUID
from .models import DiscordAuthenticationToken, DiscordMemberMaster


def create_token(user: DiscordMemberMaster) -> UUID:
    """
    指定されたユーザーIDのトークンを作成し、返却します。

    Args:
        user: discordユーザー
    """
    token = DiscordAuthenticationToken.objects.create(user=user)
    return token.token


def delete_token(user: DiscordMemberMaster):
    """
    指定されたユーザーIDのトークンを全て削除します。

    Args:
        user: discordユーザー
    """
    tokens = DiscordAuthenticationToken.objects.filter(user=user)
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
