from django.http import HttpResponse


def admin_only(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            return HttpResponse("{'data':'You have no permission!'}")

    return wrap