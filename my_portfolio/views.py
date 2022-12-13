from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
    project = Project.objects.all()
    # serch_id = request.GET.get('item')
    return render(request, 'my_portfolio/home.html', {'tittle': 'Ruslan\'s blog', 'project': project})
