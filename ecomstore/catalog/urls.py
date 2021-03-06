from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<category_name>\w*)/(?P<category_id>\d*)/$', views.product_view, name='product_view'),
    url(r'^add-user/', views.UserFormView.as_view(), name='add-user'),
    url(r'^logout$', views.user_logout_view, name='user_logout')
]
