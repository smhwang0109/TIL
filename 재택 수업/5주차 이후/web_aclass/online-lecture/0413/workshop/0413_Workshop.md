# 0413_Workshop

![index](C:\Users\user\house\web_aclass\online-lecture\0413\workshop\index.PNG)

![signup](C:\Users\user\house\web_aclass\online-lecture\0413\workshop\signup.PNG)

1. views.py

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from django.contrib.auth import get_user_model
   from django.contrib.auth.forms import UserCreationForm
   
   # Create your views here.
   def index(request):
       User = get_user_model()
       users = User.objects.all()
       context = {
           'users':users
       }
       return render(request, 'accounts/index.html', context)
   
   def signup(request):
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('accounts:index')
   
       else:
           form = UserCreationForm()
       context = {
           'form': form
       }
       return render(request, 'accounts/signup.html', context)
   
   def detail(request, pk):
       User = get_user_model()
       user = get_object_or_404(User, pk=pk)
       context = {
           'user':user
       }
       return render(request, 'accounts/detail.html', context)
   ```
