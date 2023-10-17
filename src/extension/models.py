from django.db import models
import uuid
from django.utils import timezone


class DiscordMemberMaster(models.Model):
    """
    discordメンバーマスター
    """

    member_id = models.UUIDField(verbose_name="メンバーID", name="member_id", primary_key=True, default=uuid.uuid4())
    server_id = models.BigIntegerField(verbose_name="サーバーID", name="server_id", blank=False, null=False, unique=True)
    """ サーバーID """
    user_id = models.BigIntegerField(verbose_name="ユーザID", name="user_id", blank=False, null=False, unique=True)
    """ ユーザID """
    user_name = models.CharField(verbose_name="ユーザ名", name="user_name", max_length=120)
    """ ユーザ名 """

    class Meta:
        db_table = "m_discord_member"


class DiscordAuthenticationToken(models.Model):
    """
    discord認証トークン
    """

    user_id = models.OneToOneField(
        DiscordMemberMaster, on_delete=models.CASCADE, to_field="user_id", primary_key=True, name="user"
    )
    """ ユーザID """
    token = models.UUIDField(verbose_name="トークン", name="token", default=uuid.uuid4())
    """ トークン """
    generate_date_time = models.DateTimeField(verbose_name="トークン生成日時", name="generate_date_time", default=timezone.now)
    """ トークン生成日時 """

    class Meta:
        db_table = "t_discord_authentication_token"


class DiscordExtensionValues(models.Model):
    """
    discord拡張値
    """

    extension_id = models.CharField(
        verbose_name="拡張ID", name="extension_id", primary_key=True, blank=False, null=False, max_length=100
    )
    """ 拡張ID """
    extension_value = models.CharField(
        verbose_name="拡張値", name="extension_value", primary_key=False, blank=True, null=True, max_length=256
    )
    """ 拡張値 """
    publish_flag = models.BooleanField(verbose_name="公開フラグ", name="publish_flag")
    """ 公開フラグ """

    class Meta:
        db_table = "t_discord_extension_values"
