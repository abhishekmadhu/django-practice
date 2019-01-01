from django.shortcuts import render
# from django.http import HttpResponse
# from second_app.models import User
from second_app.forms import NewUserForm


# Create your views here.
def index(request):
    myDict = {'username': "My name"}
    return render(request, 'second_app/index.html', context=myDict)

def help(request):
    myDict = {'content': "help content"}
    return render(request, 'second_app/help.html', context=myDict)


def users(request):
    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users': user_list}
    # return render(request, 'second_app/users.html', context=user_dict)
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error!")

    return render(request, "second_app/users.html", {'form':form})
