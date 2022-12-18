from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.
def home(request):
    project = Project.objects.all()
    # serch_id = request.GET.get('item')
    return render(request, 'my_portfolio/home.html', {'tittle': 'Ruslan\'s portfolio', 'project': project})


def portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Project, pk=portfolio_id)
    return render(request, 'my_portfolio/portfolio.html', {'tittle': f'Portfolio #{portfolio_id}', 'portfolio': portfolio})