from django.conf.urls import url
from django.urls import path, include
from .views import AliasList, AliasDetail

urlpatterns = [
    path('alias/', AliasList.as_view()),
    path('alias/<int:id>', AliasDetail.as_view())
]
