"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from goats import views


TXT_PK = "(?P<pk>[a-zA-Z0-9][a-zA-Z0-9-_]*)"
INT_PK = "(?P<pk>\d+)"

urlpatterns = [
    url(r'^admin', admin.site.urls),

    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name="login"),

    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name="logout"),

    url(r'^goat/all/$', views.GoatListView.as_view(), name="goats_list"),


    url(r'^goat/%s/$' % INT_PK, views.GoatDetailView.as_view(), name="goat_detail"),

    url(r'^goat/new/$', views.GoatCreateView.as_view(), name="goat_form"),

    url(r'^$', views.HomepageView.as_view(), name="home"),

    url(r'^fbv$', views.show_homepage, name='fbv'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


