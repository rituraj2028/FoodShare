from django.shortcuts import render, redirect
from .forms import FoodItemForm
from .models import FoodItem
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'foodapp/home.html')

@login_required
def donate_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('available')
    else:
        form = FoodItemForm()
    return render(request, 'foodapp/donate.html', {'form': form})

def available_food(request):
    items = FoodItem.objects.filter(available=True).order_by('-posted_on')
    return render(request, 'foodapp/available.html', {'items': items})
