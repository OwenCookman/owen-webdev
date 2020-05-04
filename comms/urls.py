from django.urls import path
from .views import contact, create_question, edit_question, delete_question

urlpatterns = [
    path('contact/', contact, name="contact"),
    path('query/', create_question, name="question"),
    path('edit_question/<slug>', edit_question, name="edit_question"),
    path('delete_question/<slug>', delete_question, name="delete_question"),
]
