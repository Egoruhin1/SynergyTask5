from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import TravelForm
from .models import Travel

def index(request):
    travels = Travel.objects.all()  # убедитесь, что этот запрос возвращает данные
    return render(request, 'diary/index.html', {'travels': travels})

@login_required
def add_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TravelForm()

    return render(request, 'diary/add_travel.html', {'form': form})

def travel_detail(request, pk):
    travel = get_object_or_404(Travel, pk=pk)  # Обработает 404 ошибку, если объект не найден
    return render(request, 'diary/travel_detail.html', {'travel': travel})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'diary/register.html', {'form': form})

