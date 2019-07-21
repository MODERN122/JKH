from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datetime_safe import datetime

from main.models import User, Application, Territory, Status, ActiveWork, Vote, House, Flat
from uk_lk.forms import UserForm, ActiveWorkForm, ManagementCompanyForm
from uk_lk.utils import moderator_required
from user_lk.forms import ApplicationCommentForm, VoteCommentForm


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
    moderate_list = votes.filter(is_moderated=False)
    votes = votes.filter(is_moderated=True, end_date__gt=datetime.now())

    return render(request, 'lk_uk/vote/vote_list.html', {'votes': votes, 'moderate_list': moderate_list})


@moderator_required
@login_required
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
        if request.POST.get('action') == 'remove':
            vote.delete()
            return redirect('votes')
        if request.POST.get('action') == 'publish':
            vote.is_moderated = True
            vote.save()
            return redirect(request.path)
        return redirect(request.path)

    if vote.agree.filter(pk=request.user.pk).exists():
        user_vote = 'agree'
    elif vote.disagree.filter(pk=request.user.pk).exists():
        user_vote = 'disagree'
    else:
        user_vote = ''

    print(user_vote)

    return render(request, 'lk_uk/vote/page.html', {'vote': vote, 'comment_form': form, 'user_vote': user_vote})


@moderator_required
@login_required
def finished_votes(request):
    votes = Vote.objects.filter(user__flat__house__territory__management_company=request.user.flat.house.territory.management_company)
    votes = votes.filter(is_moderated=True, end_date__lte=datetime.now())

    return render(request, 'lk_uk/vote/finished_votes.html', {'votes': votes})


@moderator_required
@login_required
def active_works(request):
    works = ActiveWork.objects.filter(management_company=request.user.mc_manager, end_date__gt=datetime.now()   )
    return render(request, 'lk_uk/active_work/list.html', {'works': works})


@moderator_required
@login_required
def info_page(request):
    if request.method == 'POST':
        form = ManagementCompanyForm(request.POST, instance=request.user.mc_manager)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = ManagementCompanyForm(instance=request.user.mc_manager)
    return render(request, 'lk_uk/info_page.html', {'form': form})


@moderator_required
@login_required
def territories_page(request):
    queryset = request.user.mc_manager.territories.all()
    Form = modelform_factory(Territory, fields=("name", "housing_department"))
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.management_company = request.user.mc_manager
            instance.save()
            return redirect(instance)
    else:
        form = Form()
    return render(request, 'lk_uk/list_and_form.html', {'form': form, 'objs': queryset, 'parent': request.user.mc_manager})


@moderator_required
@login_required
def houses_page(request, pk):
    parent = get_object_or_404(Territory, pk=pk)
    queryset = parent.houses.all()
    Form = modelform_factory(House, fields=("number", "street"))
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.territory = parent
            instance.save()
            return redirect(instance)
    else:
        form = Form()
    return render(request, 'lk_uk/list_and_form.html', {'form': form, 'objs': queryset, 'parent': parent})


@moderator_required
@login_required
def flats_page(request, pk):
    parent = get_object_or_404(House, pk=pk)
    queryset = parent.flats.all()
    Form = modelform_factory(Flat, fields=("number", "entrance", "floor"))
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.house = parent
            instance.save()
            return redirect(instance)
    else:
        form = Form()
    return render(request, 'lk_uk/list_and_form.html', {'form': form, 'objs': queryset, 'parent': parent})