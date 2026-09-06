from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from django.shortcuts import redirect

def custom_404_view(request, exception):
    return redirect('account:account')

def account_view(request):
    form = AuthenticationForm()
    return render(request, "account/account.html", {"form": form})


@require_POST
def ajax_login_view(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        csrf_token = get_token(request)
        response = JsonResponse({
            "success": True,
            "username": user.username,
            "csrf_token": csrf_token
        })
        response.set_cookie('csrftoken', csrf_token, path='/')
        return response
    else:
        return JsonResponse({"success": False, "errors": form.errors}, status=400)


@require_POST
def ajax_logout_view(request):
    logout(request)
    return JsonResponse({"success": True})
