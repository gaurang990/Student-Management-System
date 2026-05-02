from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import student

# Home page
def home(request):
    return render(request,'index.html')

# Contact page
def contact(request):
    return render(request,'contact.html')

# About page
def about(request):
    return render(request,'about.html')

# Login
def user_login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['upass']
        admin = authenticate(username=u, password=p)
        try:
            if admin is not None and admin.is_staff:
                login(request, admin)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    return render(request, 'login.html', {'error': error})

# Students Dashboard
def stu_home(request):
    return render(request,'students_dashboard.html')

# Add student
def add_student(request):
    error=""
    if request.method=="POST":
        try:
            n = request.POST['sname']
            e = request.POST['email']
            c = request.POST['college']
            city = request.POST['city']
            jdate = request.POST['joining_date']
            tfee = request.POST['total_fee']
            pfee = request.POST['paid_fee']
            lfee = request.POST['left_fee']
            phone = request.POST['number']
            tech = request.POST['technology']
            img = request.FILES.get('image')

            student.objects.create(
                name=n,
                email=e,
                college=c,
                city=city,
                joining_date=jdate,
                total_fee=tfee,
                paid_fee=pfee,
                left_fee=lfee,
                number=phone,
                technology=tech,
                image=img
            )

            error = "no"
            return redirect('view_records')  # Redirect after success

        except Exception as e:
            error = str(e)

    return render(request, 'add_student.html', {'error': error})

# View all students
def view_records(request):
    data = student.objects.all()
    return render(request, 'view_records.html', {'data': data})

# Edit student
def edit_stu(request, id):
    try:
        stu = student.objects.get(id=id)
    except student.DoesNotExist:
        return redirect('view_records')  # Redirect if student not found

    if request.method=="POST":
        try:
            stu.name = request.POST['sname']
            stu.email = request.POST['email']
            stu.college = request.POST['college']
            stu.city = request.POST['city']
            stu.joining_date = request.POST['joining_date']
            stu.total_fee = request.POST['total_fee']
            stu.paid_fee = request.POST['paid_fee']
            stu.left_fee = request.POST['left_fee']
            stu.number = request.POST['number']
            stu.technology = request.POST['technology']

            if 'image' in request.FILES:
                stu.image = request.FILES['image']

            stu.save()  # Save updates to database
            return redirect('view_records')

        except Exception as e:
            return render(request, 'edit_stu.html', {'data': stu, 'error': str(e)})

    return render(request, 'edit_stu.html', {'data': stu})


def del_stu(request,id):
     data=student.objects.get(id=id) 
     data.delete() 
     return redirect('view_records')

def search_stu(request):
     return render(request,"search_stu.html")  
def search_student(request):
     n=request.POST['sname'] 
     data=student.objects.filter(name__icontains=n)
     d={'data':data}
     return render(request,"view_records.html",d)

def change_pass(request):
     return render(request,"change_pass.html")

def update_pass(request):
     op=request.POST['cp']
     np=request.POST['np']
     user=request.user
     if not user.check_password(op):
          return redirect('change_pass')
     user.set_password(np)
     user.save()
     return redirect('login')
def admin_logout(request):
     logout(request)
     return redirect('login')