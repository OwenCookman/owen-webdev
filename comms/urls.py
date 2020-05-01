from django.urls import path
from .views import contact, query, edit_question

urlpatterns = [
    path('contact/', contact, name="contact"),
    path('query/', query, name="question"),
    path('edit_question/<slug>', edit_question, name="edit_question"),
]
