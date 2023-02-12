from django.http import HttpResponse,HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("Hi Bro ::: 404 error : page not found!!!")  
