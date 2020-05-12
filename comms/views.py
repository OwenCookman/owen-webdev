from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import question
from . forms import QuestionForm, UserQuestionForm, ContactForm
import os

# Create your views here.

MY_EMAIL = os.environ.get('MY_EMAIL')


def create_question(request):
    """ Returns the question.html page and allows the creation of new questions """

    if request.user.is_authenticated:
        if request.method == "POST":
            question_form = UserQuestionForm(request.POST)

            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.client = request.user
                question.name = request.user.username
                question.email = request.user.email
                question.save()

                messages.success(
                    request, "Thank you for your message, I will get back to you shortly")

                return redirect('profile')

            else:
                messages.warning(
                    request, "Sorry your message could not be posted, please try again")

        else:
            question_form = UserQuestionForm()

    else:
        if request.method == "POST":
            question_form = QuestionForm(request.POST)

            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.client = None
                question.save()

                messages.success(
                    request, "Thank you for your message, I will get back to you shortly")

                return redirect('index')

            else:
                messages.warning(
                    request, "Sorry your message could not be posted, please try again")

        else:
            question_form = QuestionForm()

    return render(request, 'question.html', {"question_form": question_form})


def edit_question(request, slug):
    """ Returns the question.html page with the form details filled in ready to be editied """

    form_data = question.objects.get(id=slug)
    question_form = QuestionForm(instance=form_data)

    if request.method == "POST":
        question_form = QuestionForm(request.POST, instance=form_data)

        if question_form.is_valid():
            question_form.save()

            messages.success(request, "Question edited successfully")

            return redirect('profile')

        else:
            question_form = QuestionForm(instance=form_data)

    return render(request, 'question.html', {"question_form": question_form})


def delete_question(request, slug):
    """ returns the delete_question.html page and allows for the deletion of questions """

    this_question = question.objects.get(id=slug)

    if request.method == "POST":
        this_question.delete()

        messages.success(
            request, "Your question was deleted")

        return redirect('profile')

    return render(request, 'delete_question.html', {"question": this_question})


@login_required
def contact(request):
    """ Returns the contact.html page where users can create new orders """
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.client = request.user
            contact.save()

            messages.success(
                request, "Thank you, I will assess your order and be in touch via email with the cost and time it will take for your build")

            return redirect('profile')

        else:
            messages.error(
                request, "Sorry, your request could not be submitted, please try again")

    else:
        contact_form = ContactForm()

    return render(request, 'contact.html', {'contact_form': contact_form})
