from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404,reverse
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import context
from .models import User,Cv,Profile,Academic,Referee,Experience,Skill
from django.contrib.auth.hashers import make_password
import pdfkit



def registerForm(request):
    return render(request, 'core/register.html')


def registerUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        check_user = User.objects.filter(username=username).count()
        check_mail = User.objects.filter(email=email).count()

        if( check_user > 0):
            messages.error(request, 'Username is already taken')
            return redirect('reg_form')
        elif(check_mail > 0):
            messages.error(request, 'Email is already taken')
            return redirect('reg_form') 
        else:
            User.objects.create(username=username,email=email,password= make_password(password))
            messages.success(request, 'Account Created Successfully, Please login')
            return redirect('reg_form')
    else:
        messages.success(request, 'Request Failed, Try Again')
        return redirect('reg_form')            


def index(request):
    return render(request, 'core/index.html')

@login_required
def dashboard(request):
    has_cv = False
    user_id = request.user.id
    check_cv = Cv.objects.filter(user_id=user_id).count()
    if(check_cv > 0):
        has_cv = True
    else:
        has_cv = False
    print('CV status',has_cv)
    context = {'cv_status':has_cv}        
    return render(request, 'core/dashboard.html',context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            return redirect('dashboard')
        else:
            messages.info(request,'Invalid Username Or Password, Try again')
            return redirect('login')
    else:
        return render(request, 'core/login.html')        



def logoutView(request):
	logout(request)
	return redirect('index')




def view_PDF(request, id=None):
    user_profile = Profile.objects.filter(user_id = id).values()
    user_profile = list(user_profile)
    user_email = User.objects.filter(id= id).values_list('email', flat=True)
    user_email = list(user_email)
    print('User email',user_email)
    user_education = Academic.objects.filter(user_id = id).values()
    user_education = list(user_education)
    print('User education',user_education)
    user_referees = Referee.objects.filter(user_id = id).values()
    user_referees = list(user_referees)
    print('User referees',user_referees)
    user_exp = Experience.objects.filter(user_id = id).values()
    user_exp = list(user_exp)
    print('User exp',user_exp)
    user_skill = Skill.objects.filter(user_id = id).values()
    user_skill = list(user_skill)
    print('User skill',user_skill)

    
    print(user_profile)

    context = {
        "company": {
            "name": "Ibrahim Services",
            "address" :"67542 Jeru, Chatsworth, CA 92145, US",
            "phone": "(818) XXX XXXX",
            "email": "contact@ibrahimservice.com",
        },
        "user_profile": user_profile,
        "user_education": user_education,
        "user_referees": user_referees,
        "user_exp": user_exp,
        "user_skill": user_skill,
        "user_email":user_email[0],
        "fname": 'user_profile.fname',
        "invoice_id": 'invoice.id',
        "invoice_total": 'invoice.total_amount',
        "customer": 'invoice.customer',
        "customer_email": 'invoice.customer_email',
        "date": 'invoice.date',
        "due_date": 'invoice.due_date',
        "billing_address": 'invoice.billing_address',
        "message": 'invoice.message',
        "lineitem": 'lineitem',

    }
    return render(request, 'core/pdf_template.html', context)


def generate_PDF(request, id):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('cv-detail', args=[id])), False)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'

    return response