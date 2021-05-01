from django.views.generic import ListView , DetailView
import json
from django.shortcuts import render, redirect
from .forms import eaddform , daddform , Loginform , laddform 
from .models import employee , Department ,Leave
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .filter import efilter

# Create your views here.

class lview1(ListView):
    model = Leave
    template_name = 'chat_room.html'

class liview1(DetailView):
    model = Leave
    template_name = 'advanced_table.html'
    context_object_name = 'leaves'



@login_required(login_url='login')
def register(request):
   
    user = request.user.get_username()
    noe = employee.objects.filter()
    return render(request , 'index.html' , {'user':user } )

    # path('', views.register ),


    # path('', views.eadd),

@login_required(login_url='login')
def eadd(request):
	form = eaddform(request.FILES or None)
	if request.method == 'POST':
		form = eaddform(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('eview')
		else:
			return render(request , 'general.html' , {'form':form})
	else:
		return render(request , 'general.html' , {'form':form})

    # path('', views.eremove),

@login_required(login_url='login')   
def eremove(request,pk):
    employee.objects.filter(id=pk).delete()
    employees = employee.objects.all()
    context = {
        'employee':employees
    }
    return render(request , 'created5.html' , context)
	
    # path('', views.eview),


@login_required(login_url='login')
def eremauth(request , pk):
    dept = employee.objects.filter(id=pk)
    context = {
        'disp':dept ,
        'pk':pk
    }
    return render(request , 'created4.html' , context )

        
        



@login_required(login_url='login')
def eview(request , **kwargs):
    disp = employee.objects.all()  
    myFilter = efilter(request.GET , queryset = disp)
    disp = myFilter.qs
    return render(request , 'panels.html' , {'disp' : disp , 'myFilter': myFilter })
    # path('', views.laddentity),



@login_required(login_url='login')
def laddentity(request):
    return render(request , 'grids.html')
# def eadd(request):
#     form = eaddform(request.FILES or None)
#     if request.method == 'POST':
#         form = eaddform(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('eview')
#         else:
#             return render(request , 'general.html' , {'form':form})
#     else:
#         return render(request , 'general.html' , {'form':form})

	
    
    # path('', views.ladd),
@login_required(login_url='login')
def ladd(request):
    form = laddform(request.FILES or None)
    if request.method == 'POST':
        form = laddform(request.POST, request.FILES)
        if form.is_valid():
            if form.type=='Annual':
                rannual= form.employee.lannual-1
                remain=rannual
            elif form.type=='Sick':
                rsick= form.employee.lsick-1
                remain=rsick
            elif form.type=='Casual':
                rcasual= form.employee.lcasual-1
                remain=rcasual
            form.save()

            return redirect('lview')
        else:
            return render(request , 'calendar.html' , {'form':form})
    else:
        return render(request , 'calendar.html' , {'form':form})
  	  

    # path('', views.lview),
@login_required(login_url='login')
def lview(request):
    leav = Leave.objects.all()
    # myFilter = efilter(request.GET , queryset = disp)
    return render(request , 'gallery.html' , {"leave":leav })

# @login_required(login_url='login')
def liview(request , **kwargs):
    empp= employee.objects.all()
    pk = empp.kwargs.get('pk')
    emp = employee.objects.filter(id=pk)
    context = {
       'disp':dept ,
         'pk':pk
    }
    return render(request , 'liview.html' , context )

    # path('', views.dadd),
@login_required(login_url='login')
def dadd(request):
    form = daddform( request.FILES  or None)
    if request.method == 'POST':
        form = daddform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dadd')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'dadd'}}">Re-add your Department</a>""")
    else:
        return render(request , 'blank.html' , {'form':form})
    	    
    
    # path('', views.dremove),
@login_required(login_url='login')
def dremove(request , pk):
    Department.objects.filter(id=pk).delete()
    dept = Department.objects.all()
    context = {
        'disp':dept
    }
    return render(request , 'created2.html' , context )
    

@login_required(login_url='login')
def dremauth(request , pk):
    dept = Department.objects.filter(id=pk)
    context = {
        'disp':dept ,
        'pk':pk
    }
    return render(request , 'created3.html' , context )
    
    # path('', views.dview),
@login_required(login_url='login')
def dview(request):
    disp = Department.objects.all()
    return render(request ,  'created.html' , {'disp' : disp})


def img(request):
    img = employee(request.FILES)
    img1= img.cv.url
    return render(request , 'upload.html', {'img' : img1}  )



def login(request):  
    uservalue=''
    passwordvalue=''

    form= Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")
        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            dj_login(request, user)
            context= {'form': form,
                      'error': 'The login has been successful',
                      'user' : user}
            
            return render(request, 'index.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'login.html', context )

    else:
        context= {'form': form}
        return render(request, 'login.html', context)



def logout(request):
    if request.method == "POST":
        logout(request)

        return redirect('login')





def leave(request):

    return render()

class profile(DetailView):
    model = employee
    template_name = 'profile1.html'

# class profile1(DetailView):
#     model = employee
#     template_name = 'profile1.html'
#     context_object_name = 'displ'


# class lview1(ListView):
#     model = Leave
#     template_name = 'chat_room.html'

# class liview1(DetailView):
#     model = Leave
#     template_name = 'advanced_table.html'
#     context_object_name = 'leaves'

