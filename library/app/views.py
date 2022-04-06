from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views.generic import TemplateView,ListView,CreateView
from .models import Book,BookType

class Home(ListView):
    template_name= 'index.html'
    model=Book

@login_required
def myBooks(request):
    template_name='mybooks.html'
    user_name = request.user
    book_list = Book.objects.filter(user=user_name)
    return render(request,template_name,{'book':book_list})

@login_required
def addBook(request):
    if(request.method=='POST'):
        user_name = request.user
        book = request.POST['book']
        author_name = request.POST['author']
        book_t = request.POST['type']
        type_obj = BookType.objects.filter(book_type=book_t)[0]
        obj = Book(user=user_name,bookName=book,
                   author=author_name,bookType=type_obj)
        obj.save()
        return redirect('mybooks')
        
    else:
        template_name='add.html'
        booktype = BookType.objects.all()
        return render(request,template_name,{'bookType':booktype})

@login_required
def update(request,book_id):
    if(request.method=='POST'):
        user_name = request.user
        book = request.POST['book']
        author_name = request.POST['author']
        book_t = request.POST['type']
        type_obj = BookType.objects.filter(book_type=book_t)[0]
        obj = Book.objects.filter(id=book_id)[0]
        obj.bookName=book
        obj.author=author_name
        obj.bookType=type_obj
        obj.save()
        return redirect('mybooks')
        
    else:
        template_name='update.html'
        booktype = BookType.objects.all()
        book = Book.objects.filter(id=book_id)[0]
        return render(request,template_name,{'bookType':booktype,
                                             'book':book})
@login_required
def delete(request,book_id):
    obj=Book.objects.filter(id=book_id)[0]
    if(request.user == obj.user):
        obj.delete()
    return redirect('mybooks')
    
    

def signup(request):
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            user_name = form.cleaned_data.get('email')
            user_name = user_name.lower()
            user = User.objects.filter(email=user_name)
            if(len(user) != 0):
                form._errors["email"]=ErrorList([
                    u'This Email is already registered'])
                return render(request,'signup.html',{'form':form})
            else:
                new_user = form.save(commit=False)
                email = form.cleaned_data.get('email')
                last_name = form.cleaned_data.get('last_name')
                email=email.lower()
                new_user.username=email
                new_user.save()
                return redirect('login')
        else:
            form._errors=ErrorList([
                    u'This Email is already registered'])
            form = SignUpForm()
            return render(request,'signup.html',{'form':form,'err':
                                                 "Please Enter Correct Details"})
    else:
        form = SignUpForm()
        return render(request,'signup.html',{'form':form})
    
                
