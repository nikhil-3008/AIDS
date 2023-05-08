from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import account , AccountManager
from django.contrib.auth.models import User
from django.contrib import messages
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.


def about(request):
    return render(request,'about.html')

def papers(request):
    return render(request,'papers.html')

def study_material(request):
    return render(request,'study_material.html')

def pdfviewer(request):
    return render(request,'pdfviewer.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1!=password2:
            return HttpResponse("Your password and Repeat password are not same")
        else:
        #    my_user=User.objects.create_user(username,email,password1)
        #    my_user.save() 
           otp = random.randint(100000,999999)
           send_otp(email, otp)

           request.session['signup_data'] = {
            'username': username,
            'email': email,
            'password': password1,
            'otp': otp,
        }
        return redirect('OtpVerification')
    
    return render(request, 'signup.html')


def send_otp(receiver_email, otp):
    myemail = 'contactaids1@gmail.com'
    paswd = 'xfyszfsrezldpcqd'

    message = MIMEMultipart()
    message['From'] = myemail
    message['To'] = receiver_email
    message['Subject'] = 'OTP DO NOT SHARE'

    body = f"Your OTP is {otp}. PLEASE DO NOT SHARE IT"
    message.attach(MIMEText(body, 'plain'))

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(myemail, paswd)
    text = message.as_string()
    connection.sendmail(myemail, receiver_email, text)
    connection.quit()
        
def OtpVerification(request):
    if request.method == 'POST':
        # Get the user-entered OTP and the stored OTP from the session variable
        user_otp = request.POST.get('otp')
        stored_otp = request.session.get('signup_data').get('otp')

        if str(user_otp) == str(stored_otp):
            
            # Create the user account if the OTP is verified
            username = request.session.get('signup_data').get('username')
            email = request.session.get('signup_data').get('email')
            password = request.session.get('signup_data').get('password')
            my_user= User.objects.create_user(username,email,password)
            my_user.save()

            # Clear the session variable
            # del request.session['signup_data']

            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('OtpVerification')

    return render(request, 'otp_verification.html')


def Home(request):
    username = request.user.username
    return render(request, 'index.html', {'username': username})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
           return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def Logout(request):
    logout(request)
    return redirect('login')