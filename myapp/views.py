from django.shortcuts import render
from django.http import HttpResponse
from myapp import forms
from django.core.files.storage import FileSystemStorage


# Create your views here.

def builtinforms(request):
    
    if request.method=="POST":
        form=forms.SampleForm(request.POST)# we creating aform instance with the data filled,all the fields will get the specified value
        if form.is_valid():
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            phno=form.cleaned_data.get('phno')
            pwd=form.cleaned_data.get('pwd')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month=form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            
            data=form.cleaned_data
            return render(request,"display_data.html",context=data)
    form=forms.SampleForm()        
    return render(request,"builtin.html",{'form':form})


#forms is afile or a library
#in Forms form is a class so we inherit from forms.Form