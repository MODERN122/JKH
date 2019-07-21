from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datetime_safe import datetime

from main.models import User, Application, Territory, Status, ActiveWork, Vote
from uk_lk.forms import UserForm, ActiveWorkForm
from uk_lk.utils import moderator_required
from user_lk.forms import ApplicationCommentForm


@moderator_required
@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.set_password(form.cleaned_data['temp_password'])
            instance.save()
            return redirect(instance)
    else:
        form = UserForm()
    return render(request, 'lk_uk/user/create.html', {'form': form})


@moderator_required
@login_required
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.set_password(form.cleaned_data['temp_password'])
            instance.save()
            return redirect(instance)
    else:
        form = UserForm(instance=user)
    return render(request, 'lk_uk/user/create.html', {'form': form})


@moderator_required
@login_required
def user_list(request):
    users = User.objects.filter(flat__house__territory__management_company=request.user.mc_manager)
    return render(request, 'lk_uk/user/list.html', {'users': users})


@moderator_required
@login_required
def applications_list(request, territory=None):
    if territory is not None:
        territory = get_object_or_404(Territory, pk=territory)
        applications = Application.objects.filter(territory=territory)
    else:
        applications = Application.objects.filter(territory__management_company=request.user.mc_manager)
    applications = applications.exclude(status__name='завершено')
    return render(request, 'lk_uk/applications/list.html', {'applications': applications})


@moderator_required
@login_required
def application_page(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST' and request.POST.get('status'):
        status = request.POST.get('status')
        application.status = Status.objects.get_or_create(name=status)[0]
        application.save()
        return redirect(request.path)

    if request.method == 'POST':
        form = ApplicationCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.application = application
            instance.user = request.user
            instance.save()
            return redirect(request.path)
    else:
        form = ApplicationCommentForm()

    return render(request, 'lk_uk/applications/page.html', {'application': application, 'comment_form': form, 'status_list': Status.objects.all()})


@moderator_required
@login_required
def create_active_work(request):
    if request.method == 'POST':
        form = ActiveWorkForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.management_company = request.user.mc_manager
            instance.save()
            return redirect(instance)
    else:
        form = ActiveWorkForm()

    return render(request, 'lk_uk/active_work/create.html', {'form': form})


@moderator_required
@login_required
def active_work(request, pk):
    work = get_object_or_404(ActiveWork, pk=pk)
    if request.method == 'POST':
        if request.POST.get('complete'):
            work.end_date = datetime.now()
            work.save()
            return redirect('active_works')

    return render(request, 'lk_uk/active_work/page.html', {'work': work})


@moderator_required
@login_required
def vote_list(request):
    votes = Vote.objects.filter(user__flat__house__territory__management_company=request.user.mc_manager)
    my_finished_votes = request.user.votes.filter(end_date__lte=datetime.now())
    moderate_list = votes.filter(is_moderated=False)
    votes = votes.filter(is_moderated=True, end_date__gt=datetime.now())

    return render(request, 'vote/vote_list.html', {'votes': votes, 'my_finished_votes': my_finished_votes, 'moderate_list': moderate_list})
