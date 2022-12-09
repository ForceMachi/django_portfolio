from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'my_portfolio/home.html', {'title': 'Password generator'})
