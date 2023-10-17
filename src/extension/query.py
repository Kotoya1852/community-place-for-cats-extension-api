from .models import DiscordMemberMaster, DiscordAuthenticationToken, DiscordExtensionValues


def get_user_by_user_id_and_server_id(user_id: int, server_id: int):
    """
    サーバーIDとユーザーIDが一致するユーザー情報を返却します。

    Args:
        server_id: discordサーバーID
        user_id: discordユーザーID
    """
    return DiscordMemberMaster.objects.filter(server_id=server_id, user_id=user_id).first()


def get_token(user: DiscordMemberMaster):
    """
    ユーザーIDのトークンを取得します。

    Args:
        user: discordユーザー
    """
    return DiscordAuthenticationToken.objects.filter(user=user).first()


def get_extension_value(extension_id: str) -> str | None:
    """
    拡張値を取得します。

    Args:
        extension_id: 拡張ID
    """
    extension = DiscordExtensionValues.objects.filter(extension_id=extension_id).first()
    if extension is None:
        return None
    else:
        return extension.extension_value
