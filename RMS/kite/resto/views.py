from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import userdetails
from .forms import messageform
from resto.models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)

            # Store user details in session
            request.session['user_id'] = user.id
            request.session['username'] = user.username

            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/resto/login_page/')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        full_name = request.POST['full_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different one.'
            return render(request, 'signup.html', {'error_message': error_message})

        if password1 == password2:
            user = User.objects.create_user(username, full_name, password1)
            user.save()
            auth.login(request, user)
            return redirect('/resto/login/')
        else:
            error_message = 'Passwords don\'t match'
            return render(request, 'signup.html', {'error_message': error_message})

    return render(request, 'signup.html')

@login_required
def booking(request):
    if request.method == 'POST':
        form = userdetails(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False) 
            new_booking.user = request.user
            new_booking.save()

            subject = 'Booking Confirmation'
            message = f'Dear {request.user.username},\n\nThank you for choosing RESTO for your dining experience! We are thrilled to confirm your booking.\n\nBooking Details:\n- Date: {new_booking.date}\n- Time: {new_booking.time}\n\nWe look forward to welcoming you and ensuring you have a delightful time at our restaurant. If you have any special requests or need to make changes to your reservation, please feel free to contact us.\n\nShould you have any questions or concerns, don\'t hesitate to reach out to us at aswinvidyadharan8@gmail.com.\n\nThank you once again for choosing RESTO. We can\'t wait to serve you!\n\nBest regards,\nThe RESTO Team'
            from_email = 'aswinvidyadharan8@gmail.com'
            recipient_list = [request.user.email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('/resto/login_page/')
    else:
        form = userdetails()
    return render(request, 'booking.html', {'form': form})


@login_required
def login_page(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'login_page.html', {'user_bookings': user_bookings})


def base(request):
    user_details = Booking.objects.last()
    return render(request,'base.html', {'user_details': user_details})

def message_form(request):
    if request.method == 'POST':
        form = messageform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/resto/message/')
    else:
        form = messageform()
    return render(request, 'message_form.html', {'form': form})

def delete_data(request,pk):
    delete=Booking.objects.get(id=pk)
    delete.delete()
    return redirect('/resto/login_page/')

def nav(request):
    return render(request,'nav.html')


