# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'
app_name = 'djangoapp'

urlpatterns = [
    path(route='login', view=views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.registration, name='register')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
