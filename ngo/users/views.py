from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import CustomUserForm, UpdateCustomUserForm, ProfileForm, UpdateProfile
from .models import CustomUser, Profile
from django.views.generic import (
    DeleteView,
    ListView,
    UpdateView,
)




# ---------------------------- Create, Update, Delete, Users ---------- #

def create_user(request):
    form = CustomUserForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:All_Users'))
    context = {
        'form': form
    }
    return render(request, "UserTemps/create_user.html", context)

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'UserTemps/update_user.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'password'
    ]
    success_url =  reverse_lazy('users:All_Users')


class UsersListView(ListView):
    model = CustomUser
    paginate_by = 100
    context_object_name = 'users_list'
    queryset = CustomUser.objects.all()
    template_name = 'UserTemps/users_list_view.html'



class delete_user(DeleteView):
    template_name = "UserTemps/delete_user.html"
    model = CustomUser
    success_url = reverse_lazy('users:All_Users')



#----------------- Profile ------------------------#
def create_profile(request):
    form = ProfileForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:All_Users'))   #change this to the homepage once it's created
    context = {
        'form': form
    }
    return render(request, "profile/create_profile.html", context)



class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile/update_profile.html'
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
    success_url =  reverse_lazy('users:All_Users') #update this to home once it's created