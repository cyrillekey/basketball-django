from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from account.forms import RegistrationForm,AccountAuthentication
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    context={}
    
    user=request.user
    #check if user is authenticated and redirect to home page if authenticated otherwise login the user
    if user.is_authenticated:
        return redirect('mainpage:home')
    #check is the request is a POST request if it is a post request check the details and log in the user otherwise show the login form 
    if request.POST:
        form=AccountAuthentication(request.POST)
        #check if the form was filled and is valid
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            #authenticate using the django authenticate method to check if the user exists
            user=authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect('mainpage:home')
        else:
             #if from is invalid redirect user back to form to fill it correctly
            context['loginform']=form      
    else:
        #user accessing form through get initialive the form and pass it to the login template
        form=AccountAuthentication() 
        context['loginform']=form         
    #render the form for user to signin  
    return render(request, 'account/login.html',context) 
def signup_view(request):
    context={}
    user=request.user
    #check is user is loged in
    if not user.is_authenticated:
        #if user is not logged in proceed with signing up the user
        if request.POST:       
            form=RegistrationForm(request.POST)
            #check if the form was filled correctly
            if form.is_valid():
                #save the records in the account md=odel
                form.save()
                email=form.cleaned_data.get('email')
                raw_password=form.cleaned_data.get('password1')
                #use the password and email to create a session and redirect the user to the home page
                account=authenticate(email=email,password=raw_password)
                login(request,account)
                return redirect('mainpage:home')
            else:
                #form has some errors redirect the user to fill the form again
                context['registration_form']=form        

        else:
            #if form was accesed using a get method initialze the form and render the form
            form=RegistrationForm()
            context['registration_form']=form
        return render(request, 'account/signup.html',context)
    else:
        #user is authenticated so redirect to the homepage
        return redirect('mainpage:home')                
              
def logout_view(request):
    #destroy the current session and redirect user to homepage
    logout(request)
    return redirect('mainpage:home')        

def account(request):
    user=request.user
    if user.is_authenticated:
        return render(request,'account/account.html')    
    else:
        return redirect('login')    