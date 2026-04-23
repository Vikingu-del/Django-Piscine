from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate,
    get_user_model
)
from django.shortcuts import (
    get_object_or_404,
    render,
    redirect
)
from .forms import (
    LoginForm, 
    RegisterForm,
    TipForm
)
import time
import random
from django.conf import settings
from django.http import HttpResponse
from .models import Tip
from django.contrib.auth.decorators import login_required


User = get_user_model()

# Create your views here.
def home(request):
    ss = request.session
    current_time = time.time()
    tips = Tip.objects.all().order_by('-date').select_related('author').prefetch_related('upvotes', 'downvotes')
    form = TipForm()

    session_name = ss.get('name', None)
    start_time = ss.get('start_time', 0)

    if not session_name or (current_time - start_time) > 42:
        ss['name'] = random.choice(settings.ANONYMOUS_NAMES)
        ss['start_time'] = current_time
        ss.modified = True

    if request.user.is_authenticated:
        # tips = tips.exclude(hide=request.user)
        if request.method == 'POST':
            form = TipForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = request.user
                tip.save()
                return redirect('app1:home')

    return render(request, 'app1/home.html', {
        'tips': tips,
        'name': ss['name'],
        'form': form,
    })


def register(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return redirect('app1:home')

    error_message = None
    if request.method == 'POST':
        try:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    password = form.cleaned_data['password']
                )
                auth_login(request, user)
                return redirect('app1:home')
        except Exception as e:
            error_message = str(e)
            print(f"Error during registration: {error_message}")
    else:
        form = RegisterForm()

    return render(request, 'app1/register.html', {'form': form, 'error_message': error_message})


def login(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return redirect('app1:home')

    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('app1:home')
            else:
                error_message = "Invalid username or password."
    else:
        form = LoginForm()
    return render(request, 'app1/login.html', {
        'form': form,
        'error_message': error_message
    })


def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('app1:home')


def vote(request, tip_id, action):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user

    if action == 'up':
        if tip.downvotes.filter(id=user.id).exists():
            tip.downvotes.remove(user)

        if tip.upvotes.filter(id=user.id).exists():
            tip.upvotes.remove(user)
        else:
            tip.upvotes.add(user)
    elif action == 'down':
        is_author = (tip.author == request.user)
        has_permission = user.has_perm('app1.can_downvote_tips')

        if is_author or has_permission:
            if tip.upvotes.filter(id=user.id).exists():
                tip.upvotes.remove(user)

            if tip.downvotes.filter(id=user.id).exists():
                tip.downvotes.remove(user)
            else:
                tip.downvotes.add(user)
        else:
            from django.contrib import messages
            messages.error(request, "You don't have permission to downvote this tip.")
    return redirect('app1:home')


@login_required
def delete(request, tip_id):
    if request.method == 'POST':
        tip = get_object_or_404(Tip, id=tip_id)
        user = request.user

        if tip.author == request.user or request.user.has_perm('app1.delete_tip'):
            tip.delete()
        else:
            from django.contrib import messages
            messages.error(request, "You don't have permission to delete this tip.")
    return redirect('app1:home')
