from django.shortcuts import render, redirect
from myprojectapp.forms import UserForm
from django.http import HttpResponse
from myprojectapp.models import User


def insert(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse('<h1>Data sent to Database</h1>')
            except:
                pass
    form = UserForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    user = User.objects.all()
    return render(request, "show.html", {'user': user})


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/show')


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})


def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'user': user})
