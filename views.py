from django.forms.utils import flatatt
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from account.forms import RegistrationsForm,AddPublicationForm,AddResearchGrantForm,AddConsultancyWorkForm
from django.urls import reverse
from account.models import Account

# Create your views here.


def index(request):
    #if request.user.is_authenticated:
    #    return HttpResponseRedirect(reverse("Research_work:research_work_page"))

    #else :

        if request.method == 'POST':

            email = request.POST.get("email")
            password = request.POST.get("password")


            user = authenticate(request,email=email,password=password)

            

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("Research_work:research_home_page"))

            else:
                 return render(request,"index.html",{"message" : "Invalid Credentials!"})

        return render(request,"index.html")


def signup(request):
    context = {}

    if request.POST:
        form = RegistrationsForm(request.POST)

        if form.is_valid():
            form.save()
            email         = form.cleaned_data.get('email')
            raw_password  = form.cleaned_data.get('password1')
            username      = form.cleaned_data.get('username')
            PF_number     = form.cleaned_data.get('PF_number')
            designation   = form.cleaned_data.get('designation')
            mobile_number = form.cleaned_data.get('mobile_number')
            department    = form.cleaned_data.get('department')

    	   
            user = form.save()
            login(request,user)

            return HttpResponseRedirect(reverse("Research_work:research_home_page"))

        else:
            context['registration_form'] = form

    else:
        form = RegistrationsForm()
        context['registration_form'] = form

    return render(request,'signup.html',context)





def research(request):
    return render(request,'base.html')

    

def publication(request):

    # user variable is set in the name of currently logged in user.
    user = request.user
    
    # all the publications related to the user are quered
    publications = user.publications.all()


    if request.method == 'POST':
         year = request.POST.get("select-year")

         if year == 'ALL':
             return render(request,'publications.html',{"publications":publications})

         publications = publications.filter(date_of_publication__year = year)

         return render(request,'publications.html',{"publications":publications})

    return render(request,'publications.html',{"publications":publications})

def add_publication(request):
    
    
    if request.method == 'POST':
        form = AddPublicationForm(request.POST)

        if form.is_valid():
            form.save()
            teacher_email_id         = form.cleaned_data.get('teacher_email_id')
            paper_title  = form.cleaned_data.get('paper_title')
            paper_authors      = form.cleaned_data.get('paper_authors')
            issn_or_issbn     = form.cleaned_data.get('issn_or_issbn')
            journal_name_or_conference_name   = form.cleaned_data.get('journal_name_or_conference_name')
            publication_type = form.cleaned_data.get('publication_type')
            date_of_publication    = form.cleaned_data.get('date_of_publication')
            DOI    = form.cleaned_data.get('DOI')
            impact_factor    = form.cleaned_data.get('impact_factor')
            publication_status    = form.cleaned_data.get('publication_status')

        return HttpResponseRedirect(reverse("Research_work:publication_page"))

            
    context = {}

    form = AddPublicationForm()

    context['add_publication_form'] = form

    

    return render(request,'add_publications.html',context)

def research_grant(request):
    
    # user variable is set in the name of currently logged in user.
    user = request.user
    
    # all the research grant related to the user are quered
    research_grants = user.research_grants.all()

    if request.method == 'POST':
         year = request.POST.get("select-year")

         if year == 'ALL':
             return render(request,'research_grant.html',{"research_grants":research_grants})

         research_grants = research_grants.filter(submitted_date__year = year)
         return render(request,'research_grant.html',{"research_grants":research_grants})
    
    return render(request,'research_grant.html',{"research_grants":research_grants})


def add_research_grant(request):
    
    
    if request.method == 'POST':
        form = AddResearchGrantForm(request.POST)

        if form.is_valid():
            form.save()
            teacher_email_id         = form.cleaned_data.get('teacher_email_id')
            project_title  = form.cleaned_data.get('project_title')
            principle_investigator_name       = form.cleaned_data.get('principle_investigator_name ')
            co_principle_investigator_name     = form.cleaned_data.get('co_principle_investigator_name')
            funding_agency   = form.cleaned_data.get('funding_agency')
            scheme = form.cleaned_data.get('scheme')
            project_status    = form.cleaned_data.get('project_status')
            granted_date    = form.cleaned_data.get('granted_date')
            submitted_date   = form.cleaned_data.get('submitted_date')

        return HttpResponseRedirect(reverse("Research_work:research_grant_page"))

            
    context = {}

    form = AddResearchGrantForm()

    context['add_research_grant_form'] = form

    

    return render(request,'add_research_grant.html',context)


def consultancy(request):
     # user variable is set in the name of currently logged in user.
    user = request.user
    
    # all the consultancy work related to the user are quered
    consultancies = user.consultancies.all()

    if request.method == 'POST':
        year = request.POST.get("select-year")

        if year == 'ALL':
            return render(request,'consultancy.html',{"consultancies":consultancies})
            
        consultancies = consultancies.filter(revenue_granted_date__year = year)
        return render(request,'consultancy.html',{"consultancies":consultancies})


    return render(request,'consultancy.html',{"consultancies":consultancies})

def add_consultancy(request):
    if request.method == 'POST':
        form = AddConsultancyWorkForm(request.POST)

        if form.is_valid():
            form.save()
            teacher_email_id            = form.cleaned_data.get('teacher_email_id')
            name_of_consultancy         = form.cleaned_data.get('name_of_consultancy')
            name_of_consultancy_project = form.cleaned_data.get('name_of_consultancy_project')
            sponsoring_agency           = form.cleaned_data.get('sponsoring_agency')
            revenue_granted_date        = form.cleaned_data.get('revenue_granted_date')
            revenue_generated           = form.cleaned_data.get('revenue_generated')
            status_of_consultancy_work  = form.cleaned_data.get('status_of_consultancy_work')


        return HttpResponseRedirect(reverse("Research_work:consultancy_page"))

            
    context = {}

    form = AddConsultancyWorkForm()

    context['add_consultancy_work_form'] = form

    

    return render(request,'add_consultancy_work.html',context)

    
def admin_page(request):

    publications = {}
    publications_name = {}

    teachers = Account.objects.all().filter(department = 'CSE')
    teacher_name = teachers.values_list('username',flat=True)

    for teacher in teachers:
        publications[teacher] = teacher.publications.all()

    for i in publications:
        publications_name[]
    

    print(publications)

    if request.method == 'POST':
        teachers = request.POST.get("select-teacher")
      
        return render(request,"admin_page.html",{"teachers":teachers,"teacher_name":teacher_name})


    

        
    return render(request,"admin_page.html",{"teacher_name":teacher_name,"teachers":teachers})

def logout_view(request):
    logout(request)
    return render(request,'index.html')