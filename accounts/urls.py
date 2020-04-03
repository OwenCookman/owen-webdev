from django.urls import path
from accounts.views import registration, login, logout, user_profile

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('profile/', user_profile, name="profile"),
]
