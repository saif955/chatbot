from django.shortcuts import render, redirect
from chatbotapp.forms import UserInputForm
from .models import*
from django.contrib.auth import logout
import sys
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")


# Let's chat for 5 lines
def predict(text, history=[]):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode((text) + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([torch.LongTensor(history),new_user_input_ids],dim=1) 

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=100, 
        pad_token_id=tokenizer.eos_token_id, 
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature = 0.5,
                                      )

    # pretty print last ouput tokens from bot
    return(" {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

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
                    post.output= predict(text)
                    post.save()
                else:
                    continue
            return redirect('upload')
        else:
            form= UserInputForm()

            
    return redirect('upload')


    
    
