from django.shortcuts import render

# Create your views here.


def portfolio(request):
    """ Returns the portfolio.html file """

    return render(request, 'portfolio.html')
