from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime
from .forms import ResumeForm
from django.http import HttpResponseRedirect
# Create your views here.
class ResumeDetailView(DetailView):
   model = Resume
   template_name = 'resume.html'
@login_required    
def create_resume(request):
    if request.method == 'POST':
        form  = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request, 'Resume created Successfully')
                return HttpResponseRedirect('/thanks/')
        else:
                messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
    return render(request, 'create-resume.html', context)
    if request.method == 'GET':
        form  = ResumeForm()
        context = {'form': form}
        return render(request, 'create-resume.html', context)
    return render(request, 'create-resume.html', {})

