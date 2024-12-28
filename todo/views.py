from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def readCreate(request):
  items = Todo.objects.all()

  if request.method == 'POST':
    title = request.POST.get('title')
    note = request.POST.get('note')
    create = Todo.objects.create(title=title, note=note)
    create.save()

  return render(request, "index.html", {"items": items})

def deleteItem(request, pk):
  item = Todo.objects.get(pk=pk)
  item.delete()
  return redirect('index')

def updateItem(request, pk):
  item = Todo.objects.get(pk=pk)

  if request.method == 'POST':
    item.title = request.POST.get('newTitle')
    item.note = request.POST.get('newNote')
    item.save()
    return redirect('index')
  
  return render(request, 'update.html', {'item': item})
  