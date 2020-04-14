from django.urls import path
from portfolio.views import portfolio

urlpatterns = [
    path('portfolio/', portfolio, name="portfolio"),
]