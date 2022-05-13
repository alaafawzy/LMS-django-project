from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import BookForm,Categoryform

# Create your views here.
def index(request):
    if request.method =='POST':
        add_book=BookForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_categ=Categoryform(request.POST)
        if add_categ.is_valid():
            add_categ.save()
    context = {
        'category':Category.objects.all(),
        'books':Books.objects.all(),
        'form': BookForm(),
        'catform':Categoryform(),
        'allbooks':Books.objects.filter(active=True).count(),
        'soldbooks':Books.objects.filter(status='sold').count(),
        'rentalbooks':Books.objects.filter(status='rental').count(),
        'availablebooks':Books.objects.filter(status='available').count(),
        
    }
    return render(request,'pages/index.html',context)

def books(request):
    
    search=Books.objects.all()
    title = None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'category':Category.objects.all(),
        'books':search,
        'catform':Categoryform(),
    }
    return render(request,'pages/books.html',context)

def delete(request,id):
    deletebook=  get_object_or_404(Books,id=id)
    if request.method == 'POST':
        deletebook.delete()
        return redirect('/')
    return render(request,'pages/delete.html')

def update(request,id):
    bookid= Books.objects.get(id=id)
    if request.method =='POST':
        save_book=BookForm(request.POST,request.FILES,instance=bookid)
        if save_book.is_valid():
            save_book.save()
            return redirect('/')
    else:
        save_book=BookForm(instance=bookid) #instance is the thing that i want to update based on it
    context={
        'form':save_book,
    }
    return render(request,'pages/update.html',context)