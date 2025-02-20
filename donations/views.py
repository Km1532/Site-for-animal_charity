from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, AdoptionRequest
from .forms import AdoptionForm

def home(request):
    animals = Animal.objects.filter(needs_help=True)
    return render(request, 'donations/home.html', {'animals': animals})

def animals_list(request):
    age_filter = request.GET.get('age')
    if age_filter:
        animals = Animal.objects.filter(age=age_filter, needs_help=True)
    else:
        animals = Animal.objects.filter(needs_help=True)
    return render(request, 'donations/animals_list.html', {'animals': animals})

def adopt(request, id):
    animal = get_object_or_404(Animal, id=id)
    
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.animal = animal
            adoption_request.save()
            animal.needs_help = False  
            animal.save()
            return redirect('home')  
    
    else:
        form = AdoptionForm() 

    return render(request, 'donations/adopt.html', {'animal': animal, 'form': form})

def about(request):
    return render(request, 'donations/about.html')

def contact(request):
    return render(request, 'donations/contact.html')