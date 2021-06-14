"""Donations views."""

# Django
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Django REST Framework
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes

# Extra views.
from extra_views import CreateWithInlinesView, InlineFormSetFactory

# Models
from users.models import Profile
from .models import Donation, Charity

# Forms
from .forms import ProfileForm

# Create your views here.
class ListCharities(ListView):
    model = Charity
    template_name = "charities/list.html"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if (
            self.request.get_full_path() == "/donations/charities/"
            and not self.request.user.is_staff
        ):
            return HttpResponseRedirect("/")
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Gets context."""
        context = super().get_context_data(**kwargs)
        charities = Charity.objects.all()
        context["charities"] = charities
        return context


class CreateCharity(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "is_staff"
    redirect_field_name = "/"
    success_url = "/"
    model = Charity
    fields = ["name", "active"]
    template_name = "charities/create.html"


class ListDonations(LoginRequiredMixin, ListView):
    """List donations view"""

    model = Donation
    template_name = "donations/list.html"

    def get_context_data(self, **kwargs):
        """Gets context."""
        user = self.request.user
        context = super().get_context_data(**kwargs)
        if self.request.get_full_path() == "/donations/mydonations/":
            donations = Donation.objects.filter(profile=user.profile.profile_id)
        elif self.request.get_full_path() == "/donations/":
            donations = (
                Donation.objects.all()
                if user.is_staff
                else Donation.objects.filter(profile=user.profile.profile_id)
            )

        context["donations"] = donations
        return context


class DonationInline(InlineFormSetFactory):
    """Donation Inline."""

    model = Donation
    fields = "__all__"
    formset_kwargs = {"form_kwargs": {}}
    factory_kwargs = {
        "extra": 1,
        "max_num": 1,
        "can_order": False,
        "can_delete": False,
    }

    def get_formset_kwargs(self):
        """Brings pending donation."""
        kwargs = super().get_formset_kwargs()

        define_user_and_profile(self)

        if self.profile:
            donations = Donation.objects.filter(
                profile=self.profile.profile_id
            ).filter(completed=False)

            # Modifies kwargs if pending donation.
            if donations:
                kwargs["form_kwargs"].update({"instance": donations[0]})

        return kwargs


class CreateDonation(CreateWithInlinesView):
    """Creates new donation"""

    model = Profile
    inlines = [DonationInline]
    template_name = "donations/create.html"
    form_class = ProfileForm

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""

        define_user_and_profile(self)

        if form_class is None:
            form_class = self.get_form_class()
        # Brings user profile.
        kwargs = self.get_form_kwargs()
        kwargs.update({"instance": self.profile})
        return form_class(**kwargs)

    def get_success_url(self):
        """Sends to payment"""
        return reverse("donations:mock", args=(self.profile.profile_id,))


@api_view(["GET"])
@renderer_classes([TemplateHTMLRenderer])
def mock_payment(request, **kwargs):
    """Mock payment."""
    complete_donation(kwargs["pk"])
    return Response({"status": "200"}, template_name="donations/mock.html")


def define_user_and_profile(instance):
    """Defines user and profile."""
    instance.user = instance.request.user
    if instance.user.profile:
        instance.profile = instance.user.profile


def complete_donation(primary_key):
    """Completes a donation"""
    profile_id = primary_key
    donation = Donation.objects.filter(profile=profile_id).get(completed=False)
    donation_id = donation.donation_id
    charity = Charity.objects.get(charity_id=donation.charity.charity_id)

    donation.completed = True
    donation.save()
    charity.donations.add(donation)
    charity.save()
