from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('https://github.com/changrunner/simple_redirect_website')
    return response
