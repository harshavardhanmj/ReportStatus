"""StatusApp URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from DisStatus.views import ListLog, DeleteUpcoming, UpcomingProjForm, ListUpcoming, AutoStatusEntryUpdate, AutoStatusList, PqStatusEntryUpdate, PqStatusList, QcStatusEntryUpdate, QcStatusList, QcStatusEntry, AutoStatusEntry, AdminView, CreateProject, CreateProjectAuto, CreateProjectPq, PqStatusEntry, ListProjectQc, UpdateProjectQc, ListProjectPq, ListProjectAuto, UpdateProjectAuto, UpdateProjectPq
from maindashboard.views import StatusView, DetailView, PqDetailView

urlpatterns = [
    url(r'^sadmin/', admin.site.urls),
	url(r'^$', StatusView.as_view()),
	url(r'^StatusAdmin/$' ,AdminView.as_view()),
	url(r'^StatusAdmin/upcomingList/$' ,ListUpcoming.as_view()),
	url(r'^StatusAdmin/createUpcomingproject/$' ,UpcomingProjForm.as_view()),
	url(r'^StatusAdmin/upcomingList/(?P<pk>\d+)/$' ,DeleteUpcoming.as_view()),
	url(r'^StatusAdmin/QcProject/$' ,ListProjectQc.as_view()),
	url(r'^StatusAdmin/QcProjectStatus/$' ,QcStatusList.as_view()),
	url(r'^StatusAdmin/QcProject/(?P<pk>\d+)/$' ,UpdateProjectQc.as_view(), name="UpdateProjectQc"),
	url(r'^StatusAdmin/QcProjectStatus/(?P<pk>\d+)/$' ,QcStatusEntryUpdate.as_view(), name="QcStatusEntryUpdate"),
	url(r'^StatusAdmin/AutoProjectStatus/$' ,AutoStatusList.as_view()),
	url(r'^StatusAdmin/AutomationProject/$' ,ListProjectAuto.as_view()),
	url(r'^StatusAdmin/AutomationProject/(?P<pk>\d+)/$' ,UpdateProjectAuto.as_view(), name="UpdateProjectAuto"),
	url(r'^StatusAdmin/AutoProjectStatus/(?P<pk>\d+)/$' ,AutoStatusEntryUpdate.as_view(), name="AutoStatusEntryUpdate"),
	url(r'^StatusAdmin/PqProject/$' ,ListProjectPq.as_view()),
	url(r'^StatusAdmin/PqProjectStatus/$' ,PqStatusList.as_view()),
	url(r'^StatusAdmin/PqProject/(?P<pk>\d+)/$' ,UpdateProjectPq.as_view(), name="UpdateProjectPq"),
	url(r'^StatusAdmin/PqProjectStatus/(?P<pk>\d+)/$' ,PqStatusEntryUpdate.as_view(), name="PqStatusEntryUpdate"),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^Qcform/$', QcStatusEntry.as_view()),
	url(r'^Pqform/$', PqStatusEntry.as_view()),
	url(r'^createprojectQC/$', CreateProject.as_view()),
	url(r'^createprojectPQ/$', CreateProjectPq.as_view()),
	url(r'^createprojectAuto/$', CreateProjectAuto.as_view()),
	url(r'^Automationform/$', AutoStatusEntry.as_view()),
	url(r'^log/$', ListLog.as_view()),
	url(r'^qcdetails/(.*)/$', DetailView.as_view()),
	url(r'^pqdetails/(.*)/$', PqDetailView.as_view()),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)