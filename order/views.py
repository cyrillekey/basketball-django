from django.shortcuts import render,redirect

# Create your views here
#.
def checkout(request):
    if request.user.is_authenticated:
        return render(request,"order/checkout.html")
    else:    
        return redirect('login')