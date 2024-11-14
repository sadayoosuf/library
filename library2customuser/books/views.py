from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book
from django.db.models import Q

@login_required
def home(request):

    return render(request,'home.html')

@login_required
def add_books(request):

    if request.method == "POST":
        t=request.POST['t']
        a=request.POST['a']
        pa=request.POST['p']
        p=request.POST['pr']
        l=request.POST['l']

        c=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,pages=pa,price=p,language=l,cover=c,pdf=f)  #creates a  new record to book table
        b.save()  #saves the record inside table

        return view_books(request)


    return render(request,'add.html')


@login_required
def view_books(request):

    k=Book.objects.all()  #read all records from table book and assign it to k

    return render(request,'view.html',{'book':k})

@login_required
def detail(request,p):
    k=Book.objects.get(id=p)
    return render(request,'detail.html',{'book':k})

@login_required
def edit(request,p):
    k=Book.objects.get(id=p)
    if request.method == "POST":
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.pages=request.POST['p']
        k.price=request.POST['pr']
        k.language=request.POST['l']

        if request.FILES.get('i')==None:
            k.save()
        else:
            k.cover=request.FILES.get('i')

        if request.FILES.get('f')==None:
            k.save()
        else:
            k.pdf=request.FILES.get('f')
        k.save()
        return view_books(request)

    return render(request,'edit.html',{'book':k})

@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return view_books(request)

def searchbooks(request):
    k=None #initialize k as None
    if request.method=="POST":
        query=request.POST['q']
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)) #it checks the key in title and author field in every records.
            #filter function returns only the matching records.

    return  render(request,'search.html',{'book':k})
