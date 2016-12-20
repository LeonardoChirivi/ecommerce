from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_name>\w*)/(?P<category_id>\d*)/$', views.product_view, name='product_view'),
    url(r'^login/', views.UserFormView.as_view(), name='login'),
]
