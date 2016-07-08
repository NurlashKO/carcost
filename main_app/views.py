from django.shortcuts import render
from .cost import car_cost

def index(request):
    if request.method == "POST":
        mark = request.POST['mark'].lower()
        model = request.POST['model'].lower()
        is_year = request.POST['is_year'].lower()
        return render(request, 'main_app/index.html', {'cost' : car_cost(mark, model, is_year)})
    return render(request, 'main_app/index.html', {'cost': 0})
