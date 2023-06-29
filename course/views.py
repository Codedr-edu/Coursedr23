from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Course, Add
from .forms import Add_Form,Course_Form
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class home(generic.ListView):
    model = Course
    template_name = 'home.html'

    def get_queryset(self):
        add = Course.objects.all()
        return add[::-1]

class DetailView(generic.DetailView):
    model = Course
'''
def home(request):
    model = Course.objects.all()
    context = {'model':model}
    return render('home.html', context)
'''
def Add_form(request):
    form = Add_Form()
    if request.method == 'POST':
        form = Add_Form(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('thank'))


    context = {'form':form}
    return render(request, 'form.html', context)

def thank(request):
    template = loader.get_template('thank.html')
    return HttpResponse(template.render())
    
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('admin_home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('c_pass')
        ad_code = request.POST.get('ad_code')
        if ad_code == 'coursedr.com.admin':
            if pass1!=pass2:
                return HttpResponse("Your password and confrom password are not Same!!")
            else:

                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')
        else:
            return HttpResponse("You not an admin of this site")
    return render (request,'signup.html')

#@login_required(login_url="login")
@method_decorator(login_required, name='dispatch')
class admin_home(LoginRequiredMixin,generic.ListView):
    model = Add
    template_name = 'admin_home.html'

    def get_queryset(self):
        add = Add.objects.all()
        return add[::-1]

class DetailView2(generic.DetailView):
    model = Add

@login_required(login_url='login')
def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def complete(request):
    if request.methods == 'POST':
        apply_id = request.POST.get('apply_id')

        app = Add.objects.filter(id=apply_id)
        if app:
            app.delete()
            return redirect('admin_home')
        else:
            return HttpResponse("Not found apply")
    return render(request,'apply_form.html')

@login_required(login_url='login')
def Course_form(request):
    form = Course_Form()
    if request.method == 'POST':
        form = Course_Form(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('admin_home'))


    context = {'form':form}
    return render(request, 'course_form.html', context)