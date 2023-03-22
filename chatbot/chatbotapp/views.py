from django.shortcuts import render, redirect
from chatbotapp.forms import UserInputForm
from .models import*
from django.contrib.auth import logout
#homepage
def home(request):
        if request.user.is_authenticated:
            return redirect('upload')
        else:
            return render(request, 'signin_page.html')
        

#lougout
def logout_view(request):
    logout(request)
    return render(request, 'signin_page.html')



# this directs to the homepage of chatbot
def chat_homepage(request):
    if request.user.is_authenticated:
        posts = UserInput.objects.all()
        args = { 'posts': posts}
        return render(request, 'index.html', args)
    else:
        return render(request, 'signin_page.html')


# this takes in data from user and gives out chatbot's output 
def post(request):
    if request.method == 'POST':
        text= ' '
        posts = UserInput.objects.all()
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data[ 'input' ]
            for post in posts:
                if not post.output:
                    post.output= text
                    post.save()
                else:
                    continue
            return redirect('upload')
        else:
            form= UserInputForm()

            
    return redirect('upload')


    
    
