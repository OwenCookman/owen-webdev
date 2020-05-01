from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import question
from . import forms
import os

# Create your views here.

MY_EMAIL = os.environ.get('MY_EMAIL')


def query(request):
    if request.method == "POST":
        question_form = forms.QuestionForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            if request.user.is_authenticated:
                question.client = request.user
                question.save()
            else:
                question.client = None
                question.save()
            messages.success(request, "Thank you for your message, I will get back to you shortly")
            return redirect('index')

        else:
            messages.warning(request, "Sorry your message could not be posted, please try again")

    else:
        question_form = forms.QuestionForm()
    return render(request, 'question.html', {"question_form": question_form})


def edit_question(request, slug):
    form_data = question.objects.get(id=slug)
    question_form = forms.QuestionForm(instance=form_data)

    if request.method == "POST":
        question_form = forms.QuestionForm(request.POST, instance=form_data)

        if question_form.is_valid():
            question_form.save()
            messages.success(request, "Question edited successfully")
            return redirect('profile')

        else:
            question_form = forms.QuestionForm(instance=form_data)

    else:
        messages.warning(request, "Sorry that could not be submitted")

    return render(request, 'question.html', {"question_form": question_form})


@login_required
def contact(request):
    if request.method == "POST":
        contact_form = forms.ContactForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.client = request.user
            contact.save()
            messages.success(request, "Your form submitted successfully")
            #message = contact_form.cleaned_data['message']
            #subject = "order"
            #from_email = request.user.email

            #email = EmailMessage(subject, message, from_email, to=['MY_EMAIL'])
            #email.send()

            return redirect('profile')

        else:
            messages.error(
                request, "Sorry, your request could not be submitted, please try again")

    else:
        contact_form = forms.ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
