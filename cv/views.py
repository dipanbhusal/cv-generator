from django.views import View
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from django.template.defaulttags import register
from .forms import cvForm
from .render import Render
# Create your views here.

 
cv_context = {}  

def index(request):
    return render(request, 'index.htm', {}) 

def CvFormView(request):
    if request.method =='POST':
        form = cvForm(request.POST)
        
        name = request.POST.get('fullname') 
        email = request.POST.get('email')
        github = request.POST.get('github')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        if request.POST.get('address2'):
            address2 = request.POST.get('address2')
        
        university1 = {
            'name' : request.POST.get('uni-name1'),
            'degree' : request.POST.get('degree1'),
            'faculty' : request.POST.get('faculty1'),
            'start_date' : request.POST.get('start-year1'),
            'end_date' : request.POST.get('end-year1'),
        }
        
        project1 = request.POST.get('project1-desc')
        programming_lang1 = request.POST.get('programming-lang1')
        
        programming_languages = [programming_lang1]
        if request.POST.get('programming-lang2'):
            programming_languages.append(request.POST.get('programming-lang2'))
        if request.POST.get('programming-lang3'):
            programming_languages.append(request.POST.get('programming-lang3'))
        if request.POST.get('programming-lang4'):
            programming_languages.append(request.POST.get('programming-lang4'))
        
        if request.POST.get('company-name1'):
            company = request.POST.get('company-name1')
            position = request.POST.get('position1')
            start_year = request.POST.get('job-start-year1')
            end_year = request.POST.get('job-end-year1')
            project_desc = request.POST.get('exp1-project-desc')
            experience1 = {
                'company': company, 
                'position' :  position,
                'project' : project_desc,
                'start_year': start_year, 
                'end_year': end_year,
                }
        software1 = request.POST.get('soft1')
        softwares = [software1]
        if request.POST.get('soft2'):
            softwares.append(request.POST.get('soft2'))

        global cv_context 
        cv_context = {
        'fullname'  : name,
        'email' : email,
        'address1' : address1,
        'github' : github,
        'phone' : phone,
        'university1' : university1, 
        'project1' : project1,
        'programming_languages' : programming_languages,
        'softwares' : softwares,
        'experience1' : experience1,
        }
        print(cv_context) 
        return render( request,'cv.htm', cv_context )  
    else:
        form = cvForm()
    form_context = { 
        'form':form,
    }
    return render(request, 'cv_form.htm', form_context)  

class FormPdf(View):
    def get(self,request, *args, **kwargs):
        cv_res = Render.cvRender('cv.htm', cv_context)
        return HttpResponse(cv_res, content_type='application/pdf')  
        
 