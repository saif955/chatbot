from django.shortcuts import render, redirect
from chatbotapp.forms import UserInputForm
from .models import*
from django.contrib.auth import logout

def home(request):
        if request.user.is_authenticated:
            return redirect('upload')
        else:
            return render(request, 'signin_page.html')
        


def logout_view(request):
    logout(request)
    return redirect('signin')



# this directs to the homepage of chatbot
def chat_homepage(request):
    posts = UserInput.objects.all()
    args = { 'posts': posts}
    return render(request, 'index.html', args)


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


    
    
