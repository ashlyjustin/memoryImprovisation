from django.urls import include, path

from django.conf.urls import url,include

from books import views

urlpatterns = [
    url(r'generate/',views.add_data,name='data'),
    url(r'json/1/',views.some_view,name='view1'),
    url(r'json/2/',views.optimized_view,name='view2')
]
