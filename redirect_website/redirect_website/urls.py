from django.contrib import admin
from django.urls import path
from .views import redirect_view
from django.http import HttpResponse

def bad_request_handler(request, exception=None):
    html_response = """
<html>
<body>
<h1>Website redirect issue</h1>
<p>Your Message
</p>
</body>
</html>
    """
    return HttpResponse(html_response)


handler500 = bad_request_handler

urlpatterns = [
    path('', redirect_view),
    path('admin/', admin.site.urls),
]
