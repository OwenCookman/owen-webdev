from django.urls import path, include
from accounts.views import registration, login, logout, user_profile
from accounts import urls_reset

urlpattern = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('profile/', user_profile, name="profile"),
    path('password-reset/', include(urls_reset)),
]
