from django.shortcuts import redirect


def moderator_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.mc_manager is None:
            return redirect('login_page')
        return func(request, *args, **kwargs)
    return wrapper
