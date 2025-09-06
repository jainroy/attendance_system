from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegisterForm
from .models import Attendance
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    today = timezone.now().date()
    attendance = Attendance.objects.filter(user=request.user, date=today).first()
    attendance_marked = bool(attendance)
    if request.method == 'POST' and not attendance_marked:
        status = request.POST.get('status')
        if status in ['Present', 'Absent']:
            Attendance.objects.create(user=request.user, date=today, status=status)
            return redirect('dashboard')
    return render(request, 'dashboard.html', {'attendance': attendance, 'attendance_marked': attendance_marked})

@login_required
def history_view(request):
    records = Attendance.objects.filter(user=request.user).order_by('-date')
    return render(request, 'history.html', {'records': records})

@staff_member_required
def admin_view(request):
    records = Attendance.objects.all().select_related('user').order_by('-date')
    return render(request, 'admin_view.html', {'records': records})
