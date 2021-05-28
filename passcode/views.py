from django.shortcuts import render, HttpResponse
from .forms import PasswordGeneratorForm
from .models import PasswordGenearator
import string, random

# Create your views here.

def index(request):
    form = PasswordGeneratorForm()
    passwords= []
    if request.method == "POST":
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

            length = form.cleaned_data['length']
            No_of_passwords = form.cleaned_data['No_of_password']
        
            for i in range(int(No_of_passwords)):
                ps = random.sample(phrase, int(length))
                password = ("".join(ps))
                passwords.append(password)
            
    context ={ 
        "form": form,
        "passwords":passwords,

    }
    
    
    return render(request,"index.html", context)