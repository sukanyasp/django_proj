from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from user.forms import UserForm
from user.models import User


def user_list(request):
    #return HttpResponse("Welcome to User List page!!")
    users = User.objects.all()
    context = {'users_key': users}
    return render(request, 'user/user_list.html', context)

def user_details(request,user_id):
    #user = User.objects.get(pk=user_id)
    user = get_object_or_404(User, pk = user_id)
    context = {'user_key': user}
    return render(request, 'user/user_details.html', context)

def user_create(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'user/user_create.html', {'form' : form})
    else:
        form = UserForm(request.POST)
        print(form)
        form.save()