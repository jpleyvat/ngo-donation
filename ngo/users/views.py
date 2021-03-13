from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CustomUserForm, UpdateCustomUserForm
from .models import CustomUser, UserProfile
from django.views.generic import (
    DeleteView,
    CreateView,
    ListView,
)




# ---------------------------- Create, Update, Delete, Users ---------- #

def create_user(request):
    form = CustomUserForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = {
        'form': form
    }
    return render(request, "UserTemps/create_user.html", context)



class UsersListView(ListView):
    model = CustomUser
    paginate_by = 100
    context_object_name = 'users_list'
    queryset = CustomUser.objects.all()
    template_name = 'UserTemps/users_list_view.html'





class delete_user(DeleteView):
    template_name = "UserTemps/delete_user.html"
    model = CustomUser
    success_url = reverse_lazy('Users:All_Users')

# -------------- Profile View -------------#
# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == "POST":
#         user_form = UserProfile(request.POST, instance=request.user)
#