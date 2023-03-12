from django.shortcuts import render, redirect

from chatbotapp.forms import UserInputForm

from .models import*


def homepage(request):
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
        posts = UserInput.objects.all()
        return redirect('upload')
    args = {'text': text, 'form': form, 'posts': posts}
    return render(request, 'temp1.html', args)