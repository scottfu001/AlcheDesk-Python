from django.conf.urls import url
from django.urls import path, include
from .views import AliasList, AliasDetail

urlpatterns = [
    path('alias/<int:pk>/', AliasDetail.as_view()),
    path('alias/', AliasList.as_view()),
]
