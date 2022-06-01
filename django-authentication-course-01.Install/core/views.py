from msilib.schema import CreateFolder
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'index.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = "/accounts/login"
    template_name = "registration/signup.html"
