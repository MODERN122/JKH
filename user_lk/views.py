import logging

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.utils.datetime_safe import datetime

from main.models import Status, Application, Vote, ActiveWork
from user_lk.forms import ApplicationForm, ApplicationCommentForm, VoteForm, VoteCommentForm, UserForm


@login_required
def info_page(request):
    uk = request.user.flat.house.territory.management_company
    return HttpRequest(f'{uk.company_name}\n{uk.email}')


@login_required
def applications_list(request):
    applications = request.user.applications.all()
    return render(request, 'applications/list.html', {'applications': applications})


@login_required
def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.territory = request.user.flat.house.territory
            instance.status = Status.objects.get_or_create(name='принято')[0]
            instance.save()

            return redirect(instance)
    else:
        form = ApplicationForm()

    return render(request, 'applications/create.html', {'form': form})


def application_page(request, pk):
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = ApplicationCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.application = application
            instance.save()
            return redirect(request.path)
    else:
        form = ApplicationCommentForm()

    return render(request, 'applications/page.html', {'application': application, 'comment_form': form})


@login_required()
def create_vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect(instance)
    else:
        form = VoteForm()

    return render(request, 'vote/create.html', {'form': form})


def vote_page(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    form = VoteCommentForm()
    if request.method == 'POST' and request.POST.get('context'):
        form = VoteCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.vote = vote
            instance.save()
            return redirect(request.path)
    elif request.method == 'POST':
        if request.POST.get('vote') == 'agree':
            vote.agree.add(request.user)
            vote.disagree.remove(request.user)
        if request.POST.get('vote') == 'disagree':
            vote.disagree.add(request.user)
            vote.agree.remove(request.user)
        return redirect(request.path)

    if vote.agree.filter(pk=request.user.pk).exists():
        user_vote = 'agree'
    elif vote.disagree.filter(pk=request.user.pk).exists():
        user_vote = 'disagree'
    else:
        user_vote = ''

    print(user_vote)

    return render(request, 'vote/page.html', {'vote': vote, 'comment_form': form, 'user_vote': user_vote})


@login_required
def vote_list(request):
    votes = Vote.objects.filter(user__flat__house__territory__management_company=request.user.flat.house.territory.management_company)
    return render(request, 'vote/vote_list.html', {'votes': votes})


@login_required
def active_works_list(request):
    active_works = ActiveWork.objects.filter(end_date__gt=datetime.now())
    return render(request, 'active_works.html', {'active_works': active_works})


@login_required
def user_edit(request):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(''.join([request.path, '#success']))
    else:
        form = UserForm(instance=request.user)

    return render(request, 'user_edit.html', {'form': form})