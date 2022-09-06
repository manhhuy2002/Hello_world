from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path(r'form.html', views.form),
    path(r'signin.html', views.signin),
    path(r'signup.html',views.signup),
    path(r'table.html',views.table),
    path(r'typography.html',views.typography),
    path(r'index.html',views.index),
    path(r'button.html',views.button),
    path(r'chart.html', views.chart),
    path(r'element.html', views.element),
    path(r'widget.html',views.widget),
    path(r'404.html',views.four),
    path(r'blank.html',views.blank),
   
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)