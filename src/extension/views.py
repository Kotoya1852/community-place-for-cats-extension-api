from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

from extension import query, commands, utils

import logging

from extension.serializers import auth_serializer, message_response_serializer, member_serializer
from .const import *

logger = logging.getLogger("cpfc-extension-api")


@extend_schema(tags=["認証認可API"])
class AuthViews(APIView):
    """認証認可API"""

    serializer_class = auth_serializer.AuthPostRequestSerializer

    @extend_schema(
        summary="トークン生成API",
        parameters=[OpenApiParameter(name="user_id", description="discordユーザーID")],
        operation_id="authTokenGenerate",
        responses={
            201: OpenApiResponse(response=auth_serializer.AuthPostResponseSerializer, description="トークン作成成功"),
            400: OpenApiResponse(
                response=message_response_serializer.MessageResponseSerializer, description="不正なリクエスト"
            ),
            500: OpenApiResponse(response=None, description="システムエラー"),
        },
    )
    def post(self, request):
        """トークン生成API"""

        # バリデーションチェック（デシリアライズ）
        serialize = auth_serializer.AuthPostRequestSerializer(data=request.data)
        if not serialize.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=utils.message_response_deserialize(message="不正なリクエストです")
            )

        # シリアライズ
        serialize.validated_data
        param = serialize.save()

        # メンバー存在チェック
        user = query.get_user_by_user_id_and_server_id(param.user_id, param.server_id)
        if user is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=utils.message_response_deserialize(message="ユーザーが存在しません")
            )

        # トークン確認
        now_token = query.get_token(user)
        token = None
        response_status_code = status.HTTP_201_CREATED
        if now_token is None:
            # トークンが存在しない
            token = commands.create_token(user)
        else:
            # トークン有効時間（分）を取得 ※取得出来なかった場合、デフォルト60分を設定
            expired_token_minute_str = query.get_extension_value(EXPIRED_TOKEN_EXTENSION_ID)
            expired_token_minute_int = 60
            if expired_token_minute_str is not None:
                expired_token_minute_int = int(expired_token_minute_str)

            # 時間チェック用
            expired_token_datetime = now_token.generate_date_time + timezone.timedelta(minutes=expired_token_minute_int)

            # トークン有効期限チェック
            if expired_token_datetime >= timezone.now():
                # 期限が切れていない（既存のトークンをレスポンス）
                token = now_token.token
                response_status_code = status.HTTP_200_OK
            else:
                # 期限が切れている（作り直し）
                commands.delete_token(user)
                token = commands.create_token(user)

        response_serializer = auth_serializer.AuthPostResponseSerializer(data={"token": token})
        response_serializer.is_valid()
        return Response(status=response_status_code, data=response_serializer.data)


@extend_schema(tags=["discordメンバー管理API"])
class MemberViews(APIView):
    """discordメンバー管理API"""

    serializer_class = member_serializer.MemberPostRequestSerializer

    @extend_schema(
        summary="メンバー登録API",
        parameters=[OpenApiParameter(name="user_id", description="discordユーザーID")],
        operation_id="memberRegistration",
        request=member_serializer.MemberPostRequestSerializer,
        responses={
            201: OpenApiResponse(response=None, description="メンバー登録成功"),
            400: OpenApiResponse(
                response=message_response_serializer.MessageResponseSerializer, description="不正なリクエスト"
            ),
            500: OpenApiResponse(response=None, description="システムエラー"),
        },
    )
    def post(self, request):
        """メンバー登録API"""

        # バリデーションチェック（デシリアライズ）
        serialize = member_serializer.MemberPostRequestSerializer(data=request.data)
        if not serialize.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=utils.message_response_deserialize(message="不正なリクエストです")
            )

        # シリアライズ
        serialize.validated_data
        param = serialize.save()

        # 既に登録されているか確認
        user = query.get_user_by_user_id_and_server_id(param.user_id, param.server_id)
        if user is not None:
            # 既に存在する
            return Response(status=status.HTTP_409_CONFLICT, data=utils.message_response_deserialize(message="既に登録済です"))

        # 登録する
        commands.create_user(param.user_id, param.server_id, param.user_name)
        return Response(status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="メンバー削除",
        parameters=[OpenApiResponse(response=None, description="メンバー削除成功")],
        operation_id="memberDeletion",
        request=member_serializer.MemberDeleteRequestSerializer,
        responses={
            204: OpenApiResponse(response=None, description="メンバー削除成功"),
            400: OpenApiResponse(
                response=message_response_serializer.MessageResponseSerializer, description="不正なリクエスト"
            ),
            500: OpenApiResponse(response=None, description="システムエラー"),
        },
    )
    def delete(self, request):
        """メンバー削除"""

        # バリデーションチェック（デシリアライズ）
        serialize = member_serializer.MemberDeleteRequestSerializer(data=request.query_params)
        if not serialize.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=utils.message_response_deserialize(message="不正なリクエストです")
            )

        # シリアライズ
        serialize.validated_data
        param = serialize.save()

        # ユーザー存在チェック
        user = query.get_user_by_user_id_and_server_id(param.user_id, param.server_id)
        if user is None:
            # 存在しない
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=utils.message_response_deserialize(message="未登録です")
            )

        # ユーザー削除
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
