from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from main.models import Status, Application
from user_lk.forms import ApplicationForm


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
            instance.management_company = request.user.flat.house.territory.management_company
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
    return render(request, 'applications/page.html', {'application': application})