from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path("api/", include("extension.urls")),
    path("swagger/", include("config.swagger_urls")),
    path("admin/", admin.site.urls),
]

# 静的ファイルの出力用
urlpatterns += staticfiles_urlpatterns()
