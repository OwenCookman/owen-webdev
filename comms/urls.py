from django.urls import path
from comms.views import contact, question

urlpatterns = [
    path('contact/', contact, name="contact"),
    path('question/', question, name="question"),
]
