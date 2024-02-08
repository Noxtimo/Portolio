from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse

def home(request):
    user_email = None
    if request.method == 'POST':
        name = request.POST.get('Name')
        user_email  = request.POST.get('Email')
        message = request.POST.get('Message')
    
        subject = 'New Message from Your Website'
        email_message = f"Name: {name}\nEmail: {user_email}\nMessage: {message}"
        from_email = 'canbuulo12@gmail.com'  # Replace with your email
        recipient_list = ['canbuulo12@gmail.com']  # Replace with your email

        send_mail(subject, email_message, from_email, recipient_list)
        return JsonResponse({'message': 'Message sent successfully!', 'user_email': user_email})


    return render(request, 'my_portfolio/home.html', {'user_email': user_email})


def about(request):

    return render(request, 'my_portfolio/about.html')
