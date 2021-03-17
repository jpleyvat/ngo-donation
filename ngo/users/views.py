from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import views as auth_views
from django.views import generic

#permission imports
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required #use this  import  on class based views
from django.utils.decorators import method_decorator


#forms, models and views imports
from .forms import CustomUserForm, UpdateCustomUserForm, ProfileForm, UpdateProfile, LoginForm, RegistrationForm
from .models import CustomUser, Profile
from django.views.generic import (
    DeleteView,
    ListView,
    UpdateView,
)


# ---------------------------- Create, Update, Delete, Users ---------- #
    #use the decorator to only let the admin access user management
def create_user(request):
    form = CustomUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:All_Users'))
    context = {
        'form': form
    }
    return render(request, "UserTemps/create_user.html", context)


def user_registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)



# @method_decorator(login_required, name='users.views.UserUpdateView')
class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'UserTemps/update_user.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        # 'password'
    ]
    success_url =  reverse_lazy('users:All_Users')


# @method_decorator(login_required, name='users.views.UsersListView')
class UsersListView(ListView):
    model = CustomUser
    paginate_by = 100
    context_object_name = 'users_list'
    queryset = CustomUser.objects.all()
    template_name = 'UserTemps/users_list_view.html'
#
# @method_decorator(login_required(login_url ='users:delete_user'), name = dispatch)
# @method_decorator(user_passes_test(profile))
class delete_user(DeleteView):
    template_name = "UserTemps/delete_user.html"
    model = CustomUser
    success_url = reverse_lazy('users:All_Users')



#----------------- Profile ------------------------#
def get_profile(request):
    user = CustomUser.objects.filter(profile = request.user)
    return render(request, '', {})


def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:All_Users'))
    context = {
        'form': form
    }

    return render(request, "UserTemps/create_profile.html", context)


#update this and link it to menu once it's created
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'UserTemps/update_profile.html'
    fields = [
        'bio',
        'location',
        'birth_date',
        'cma_num',
        'phone',
        'addressLineOne',
        'addressLineTwo',
        'city',
        'state',
        'zip_code',
        'country',
        'urbanization',
    ]
    success_url =  reverse_lazy('users:home') 





def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email= form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="users/login.html",
                  context={"form": form})


