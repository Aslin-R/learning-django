from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("Hi Bro ::: 404 error : page not found!!!")  