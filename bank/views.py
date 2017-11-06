from django.shortcuts import render, redirect   # importing modules for render page and redirect page
from django.contrib.auth import authenticate, login, logout # importing modules for authenticate, login and logout
from django.contrib.auth.decorators import login_required   # importing modules for redirecting to login page if entering page that needs login
from django.contrib.auth.models import User # importing User objects that already exist in Django
from django.contrib import messages # importing message for alert if there's error
from django.core.exceptions import ObjectDoesNotExist   # importing raise error
from .models import Account # importing account object


# main page
def index(request):
    return render(request, 'index.html')

# login page
def login_form(request):
    if not request.user.is_authenticated:   # if not authenticated render login, else go to menu
        return render(request, 'account/login.html')
    else:
        return redirect('bank:menu')

# login action
def login_action(request):
    # get the username and password then authenticate it
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None: # if authenticate is successful then login and redirect to menu
        login(request, user)
        return redirect('bank:menu')
    else:   # else show error
        messages.error(request, 'Sorry, wrong username / password or either account is not registered. ')
        return redirect('bank:login_form')

# logout action
def logout_action(request):
    logout(request) # logout and redirect to main
    return redirect('bank:main')

# menu, need login to see this page
@login_required
def menu(request):
    name = request.user.get_full_name() # show the full name
    return render(request, 'menu/menu.html', {'full_name': name})

# balance, need login to see this page
@login_required
def balance(request):
    acc = Account.objects.get(user_id=request.user.id) # get the balance for the user that logged on
    return render(request, 'menu/balance.html', {'acc': acc})

# transfer action, need login to see this page
@login_required
def transfer(request):

    # Checking if user that receives the money exist.
    try:
        # Variables
        u_receive = request.POST['to']  # Username that will receive the money
        acc_sender = Account.objects.get(user_id=request.user.id)  # Getting the sender account object
        username_receiver = User.objects.get(username=u_receive)  # Getting the receiver object
        acc_receiver = Account.objects.get(user_id=username_receiver.id)  # Getting the account of receiver object
        amt = int(request.POST['amount'])  # Getting the amount of transferring

        # Checking if transfer to yourself. because if you're transferring to yourself there's money duplication bug.
        if u_receive != request.user.username:

            # Validates if amt less or equal than sender account balance.
            if amt <= acc_sender.balance and amt >= 10000:
                acc_sender.balance -= amt  # Subtracting your balance with the amount of amt
                acc_receiver.balance += amt  # Adding balance with the amount of amt
                acc_sender.save()  # Saving balance that has been subtracted to DB.
                acc_receiver.save()  # Saving balance that has been added to DB.
                messages.success(request, 'You have transferred Rp. {} to {}. You now only have Rp. {}'.format(
                    amt, u_receive, acc_sender.balance))
                return redirect('bank:transfer_form')
            else:
                messages.error(request, 'You don\'t have that much amount of balance. You only have Rp. {}'.format(acc_sender.balance))
                return redirect('bank:transfer_form')
        else:
            messages.error(request, 'You can\'t transfer to yourself!')
            return redirect('bank:transfer_form')
    except ObjectDoesNotExist:
        messages.error(request, 'You can\'t transfer to \'{}\' because that user doesn\'t exist.'.format(request.POST['to']))
        return redirect('bank:transfer_form')

# transfer page, need to be logged on
@login_required
def transfer_form(request):
    return render(request, 'menu/transfer.html')