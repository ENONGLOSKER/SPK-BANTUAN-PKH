from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from SPK.models import Alternatif, Kriteria, SubKriteria, Penilaian
from django.views.decorators.csrf import csrf_protect


def home(request):
    template_name='home.html'
    return render(request, template_name)

def index(request):
    jlh_alternatif = Alternatif.objects.all().count()
    jlh_kriteria = Kriteria.objects.all().count()
    jlh_sub_kriteria = SubKriteria.objects.all().count()
    jlh_penilaian = Penilaian.objects.all().count()

    context = {
        'alternatif': jlh_alternatif,
        'kriteria': jlh_kriteria,
        'sub_kriteria': jlh_sub_kriteria,
        'penilaian': jlh_penilaian,
    }

    template_name='index.html'
    return render(request, template_name,context)
@csrf_protect
def user_register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2: 
            messages.warning(request, 'Password tidak sama!')
            return redirect('register')
        else: 
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            messages.success(request,"Selamat Register Berhasil")
            return redirect('login') 

    return render(request,'regis_ter.html')
@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passw')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Selamat, Login Berhasil!")
            return redirect('index')
        else:
            messages.warning(request, 'Username dan Password tidak Valid!!')
            return redirect('login')
    return render(request, 'log_in.html')

def user_logout(request):
    logout(request) 
    return redirect('login')
