from django.shortcuts import render, redirect

from chatbotapp.forms import UserInputForm

from .models import*

# this directs to the homepage of chatbot
def homepage(request):
    posts = UserInput.objects.all()
    args = { 'posts': posts}
    return render(request, 'temp1.html', args)


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


    
    
