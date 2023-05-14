from django.urls import path

from .views import pubViews as views
from .views import chatViews as chat

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views.authViews import RegisterAPI

urlpatterns = [
    # Publication
    path("publications/", views.publications, name="publications"),
    path("publication/<int:pk>", views.publication, name="publication"),
    path("publication/create/", views.pub_creation, name="pub_creation"),
    path("publication/update/<int:pk>", views.pub_update, name="pub_update"),
    path('publication/delete/<int:pk>', views.del_pub, name="del_pub"),

    # Discussion
    path("chats/", chat.dicussions, name="dicussions"),
    path("chat/<int:pk>", chat.dicussion, name="dicussion"),
    path("chat/create/", chat.chat_creation, name="chat_creation"),
    path("chat/update/<int:pk>", chat.chat_update, name="chat_update"),
    path('chat/delete/<int:pk>', chat.del_chat, name="del_chat"),

    # Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPI.as_view(), name='register'),
]
