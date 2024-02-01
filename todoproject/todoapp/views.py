from django.shortcuts import render,redirect
from .forms import taskform
from .models import task as tk
from django.urls import reverse


# Create your views here.
def index(request):
    template = 'main/index.html'
    form = taskform(request.POST or None)
    task = tk.objects.all().values()
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            form = taskform()
            return render(request, template,context={'task': task, 'form': form})
        else:
            form.validate_unique()
            
    
    return render(request, template, context={'task': task, 'form': form})

def delete(request, id):
    t1 = tk.objects.get(id=id)
    t1.delete()
    return redirect(index)

def update(request, id=None):
    t2 = tk.objects.get(id=id)
    template = 'main/update.html'
    
    if request.method == 'POST':
        form = taskform(request.POST, instance=t2)
        
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = taskform(instance=t2)
    
        return render(request, template, context={'form': form, 'value':t2})