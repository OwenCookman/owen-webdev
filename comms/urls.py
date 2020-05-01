from django.urls import path
from comms.views import contact, question, EditQuestion

urlpatterns = [
    path('contact/', contact, name="contact"),
    path('question/', question, name="question"),
    path('question/<slug>', EditQuestion, name="edit_question"),
]
