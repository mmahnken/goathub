# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from forms import CommentCreateForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


from .models import Goat, Comment


class HomepageView(generic.TemplateView):
    """The homepage of the site."""

    template_name = "goats/homepage.html"


class GoatListView(generic.ListView):
    """See all goats."""

    model = Goat

    def get_template_names(self):
        format = self.request.GET.get('format')
        if format == 'pinterest':
            return ['goats/goat_list_pinterest.html']
        else:
            return ['goats/goats_list.html']

class CommentCreateFormMixin(object):
    """Mixin to add a comment box to GoatDetail page."""

    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(request.POST)
        comment = form.save(commit=False)
        comment.goat = self.get_object()
        comment.user = self.request.user
        form.save()
        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super(CommentCreateFormMixin, self).get_context_data(**kwargs)
        context['comment_form'] = CommentCreateForm()
        return context

class GoatDetailView(CommentCreateFormMixin, generic.DetailView):
    """See a single goat."""

    model = Goat
    template_name = "goats/goat_detail.html"


class GoatCreateView(LoginRequiredMixin, generic.CreateView):
    """Create a goat."""

    model = Goat
    fields = ['name', 'description', 'photo']
    success_url = '/'

    def form_valid(self, form):
        """Auto assign logged in user to Goat's user."""

        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Goat added.')
        return super(GoatCreateView, self).form_valid(form)

def show_homepage(request):
    return render(request, 'goats/homepage.html')



















