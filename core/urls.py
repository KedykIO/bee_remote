from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from core import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name='home'),

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('action/', views.my_action, name='my_action'),
    path('submit_form/', views.submit_form, name='submit_form'),
]"""