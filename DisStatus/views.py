from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import logging, DailyStatusQC, DailyStatusAuto, ProjectQC, ProjectAuto, ProjectPq, DailyStatusPQ, UpcomingProj
from .forms import UpcomingProject, AutoDailyStatusUpdateForm, PqDailyStatusUpdateForm, DailyStatusUpdateForm, DailyStatusForm, AutoDailyStatusForm, CreateProjectForm, CreateProjectAutoForm, CreateProjectPqForm, PqDailyStatusForm, UpdateProjectQcForm, UpdateProjectPqForm, UpdateProjectAutoForm
import requests
import datetime
from datetime import timedelta
from requests.auth import HTTPBasicAuth
import json
from .mixins import AjaxFormMixin
# Create your views here.

class QcStatusEntry(LoginRequiredMixin, CreateView):
	template_name = 'formQC.html'
	form_class = DailyStatusForm
	success_url = '/StatusAdmin/QcProjectStatus/'
	
	def get_context_data(self, **kwargs):
		context = super(QcStatusEntry, self).get_context_data(**kwargs)
		context['proj_list'] = ProjectQC.objects.filter(ProductStatus="Active")
		projName = ProjectQC.objects.filter(ProductStatus="Active").values('ProductName')
		defectCountList = []
		defectProjList = []
		for proj in projName:
			temp = proj["ProductName"]
			totProj = temp.split(",")
			itr1 = 0
			issueCount = 0
			while itr1 < len(totProj):
				print(totProj[itr1])
				url = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred, -) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) ORDER BY key DESC'''
				headers = {'Content-Type': 'application/json'}
				response = requests.get(url, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
				geodata1 = response.json()
				try:
					issueCount = issueCount + int(geodata1["total"]);
				except:
					issueCount = 0;
				itr1 = itr1 + 1
			try:
				defectCountList.append(issueCount)
			except:
				defectCountList.append(0)
			defectProjList.append(proj["ProductName"])
		context['defect_count_list'] = defectCountList
		context['defect_proj_list'] = defectProjList
		logging.objects.create(user = self.request.user, action = "QC status new entry")
		return context


class QcStatusList(LoginRequiredMixin, ListView):
	template_name = 'projectStatusList.html'
	
	def get_queryset(self):
		currentDate = datetime.datetime.now().date()
		qs = DailyStatusQC.objects.filter(LogDate=currentDate)
		if qs.exists():
			return DailyStatusQC.objects.filter(LogDate=currentDate)

class QcStatusEntryUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'formUpdateQC.html'
	form_class = DailyStatusUpdateForm
	success_url = '/StatusAdmin/QcProjectStatus/'
	
	def get_context_data(self, **kwargs):
		context = super(QcStatusEntryUpdate, self).get_context_data(**kwargs)
		context['proj_list'] = ProjectQC.objects.filter(ProductStatus="Active")
		logging.objects.create(user = self.request.user, action = "QC status update entry")
		return context
	
	def get_queryset(self):
		currentDate = datetime.datetime.now().date()
		qs = DailyStatusQC.objects.filter(LogDate=currentDate)
		if qs.exists():
			return DailyStatusQC.objects.filter(LogDate=currentDate)

class PqStatusEntry(LoginRequiredMixin, CreateView):
	template_name = 'formPQ.html'
	form_class = PqDailyStatusForm
	success_url = '/StatusAdmin/PqProjectStatus/'
	
	def get_context_data(self, **kwargs):
		context = super(PqStatusEntry, self).get_context_data(**kwargs)
		context['proj_list'] = ProjectPq.objects.filter(ProductStatus="Active")
		projName = ProjectPq.objects.filter(ProductStatus="Active").values('ProductName')
		defectCountListpq = []
		defectProjListpq = []
		for proj in projName:
			temp = proj["ProductName"]
			totProj = temp.split(",")
			itr1 = 0
			issueCount = 0
			while itr1 < len(totProj):
				url = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred, -) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation ORDER BY key DESC'''
				headers = {'Content-Type': 'application/json'}
				response = requests.get(url, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
				geodata1 = response.json()
				try:
					issueCount = issueCount + int(geodata1["total"]);
				except:
					issueCount = 0;
				itr1 = itr1 + 1
			try:
				defectCountListpq.append(issueCount)
			except:
				defectCountListpq.append(0)
			defectProjListpq.append(proj["ProductName"])
		context['defect_count_list'] = defectCountListpq
		context['defect_proj_list'] = defectProjListpq
		logging.objects.create(user = self.request.user, action = "PQ status new entry")
		return context

class PqStatusList(LoginRequiredMixin, ListView):
	template_name = 'pqprojectStatusList.html'
	
	def get_queryset(self):
		currentDate = datetime.datetime.now().date()
		qs = DailyStatusPQ.objects.filter(LogDate=currentDate)
		if qs.exists():
			return DailyStatusPQ.objects.filter(LogDate=currentDate)

class PqStatusEntryUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'formUpdatePQ.html'
	form_class = PqDailyStatusUpdateForm
	success_url = '/StatusAdmin/PqProjectStatus/'
	
	def get_context_data(self, **kwargs):
		context = super(PqStatusEntryUpdate, self).get_context_data(**kwargs)
		context['proj_list'] = ProjectQC.objects.filter(ProductStatus="Active")
		logging.objects.create(user = self.request.user, action = "PQ status update entry")
		return context
	
	def get_queryset(self):
		currentDate = datetime.datetime.now().date()
		qs = DailyStatusPQ.objects.filter(LogDate=currentDate)
		if qs.exists():
			return DailyStatusPQ.objects.filter(LogDate=currentDate)

class CreateProject(LoginRequiredMixin, CreateView):
	template_name = 'formProj.html'
	form_class = CreateProjectForm
	success_url = '/StatusAdmin/QcProject/'
	
	def get_context_data(self, **kwargs):
		context = super(CreateProject, self).get_context_data(**kwargs)
		context['name'] = "QC"
		logging.objects.create(user = self.request.user, action = "qc project new entry")
		return context

class CreateProjectAuto(LoginRequiredMixin, CreateView):
	template_name = 'formProj.html'
	form_class = CreateProjectAutoForm
	success_url = '/StatusAdmin/AutomationProject/'
	
	def get_context_data(self, **kwargs):
		context = super(CreateProjectAuto, self).get_context_data(**kwargs)
		context['name'] = "AUTOMATION"
		logging.objects.create(user = self.request.user, action = "auto project new entry")
		return context

class UpdateProjectQc(LoginRequiredMixin, UpdateView):
	template_name = 'formProjUpdate.html'
	form_class = UpdateProjectQcForm
	queryset = ProjectQC.objects.all();
	success_url = '/StatusAdmin/QcProject/'
	
	def get_context_data(self, **kwargs):
		context = super(UpdateProjectQc, self).get_context_data(**kwargs)
		context['name'] = "QC"
		logging.objects.create(user = self.request.user, action = "qc project update entry")
		return context

class UpdateProjectAuto(LoginRequiredMixin, UpdateView):
	template_name = 'formProjUpdate.html'
	form_class = UpdateProjectAutoForm
	queryset = ProjectAuto.objects.all();
	success_url = '/StatusAdmin/AutomationProject/'
	
	def get_context_data(self, **kwargs):
		context = super(UpdateProjectAuto, self).get_context_data(**kwargs)
		context['name'] = "AUTOMATION"
		logging.objects.create(user = self.request.user, action = "auto project update entry")
		return context

class UpdateProjectPq(LoginRequiredMixin, UpdateView):
	template_name = 'formProjUpdate.html'
	form_class = UpdateProjectPqForm
	queryset = ProjectPq.objects.all();
	success_url = '/StatusAdmin/PqProject/'
	
	def get_context_data(self, **kwargs):
		context = super(UpdateProjectPq, self).get_context_data(**kwargs)
		context['name'] = "PQ"
		logging.objects.create(user = self.request.user, action = "pq project update entry")
		return context

class ListProjectQc(LoginRequiredMixin, ListView):
	template_name = 'projectList.html'
	queryset = ProjectQC.objects.all();
	
	def get_context_data(self, **kwargs):
		context = super(ListProjectQc, self).get_context_data(**kwargs)
		context['name'] = "QC"
		return context

class ListProjectAuto(LoginRequiredMixin, ListView):
	template_name = 'projectListAuto.html'
	queryset = ProjectAuto.objects.all();
	
	def get_context_data(self, **kwargs):
		context = super(ListProjectAuto, self).get_context_data(**kwargs)
		context['name'] = "Automation"
		return context
		
class ListProjectPq(LoginRequiredMixin, ListView):
	template_name = 'projectListPq.html'
	queryset = ProjectPq.objects.all();
	
	def get_context_data(self, **kwargs):
		context = super(ListProjectPq, self).get_context_data(**kwargs)
		context['name'] = "PQ"
		return context

class CreateProjectPq(LoginRequiredMixin, CreateView):
	template_name = 'formProj.html'
	form_class = CreateProjectPqForm
	success_url = '/StatusAdmin/PqProject/'
	
	def get_context_data(self, **kwargs):
		context = super(CreateProjectPq, self).get_context_data(**kwargs)
		context['name'] = "PQ"
		logging.objects.create(user = self.request.user, action = "pq project new entry")
		return context

class AutoStatusEntry(LoginRequiredMixin, CreateView):
	template_name = 'formAuto.html'
	form_class = AutoDailyStatusForm
	success_url = '/StatusAdmin/AutoProjectStatus/'
	
	def get_context_data(self, **kwargs):
		context = super(AutoStatusEntry, self).get_context_data(**kwargs)
		context['proj_list'] = ProjectAuto.objects.filter(ProductStatus="Active")
		logging.objects.create(user = self.request.user, action = "auto status new entry")
		return context

class AutoStatusList(LoginRequiredMixin, ListView):
	template_name = 'autoprojectStatusList .html'
	
	def get_queryset(self):
		currentDate = datetime.datetime.now().date()
		qs = DailyStatusAuto.objects.filter(LogDate=currentDate)
		if qs.exists():
			return DailyStatusAuto.objects.filter(LogDate=currentDate)

class AutoStatusEntryUpdate(LoginRequiredMixin, UpdateView):
	template_name = 'formUpdateAuto.html'
	form_class = AutoDailyStatusUpdateForm
	success_url = '/StatusAdmin/AutoProjectStatus/'
	
	def get_context_data(self, **kwargs):
		context = super(AutoStatusEntryUpdate, self).get_context_data(**kwargs)
		context['proj_list'] = ProjectQC.objects.filter(ProductStatus="Active")
		logging.objects.create(user = self.request.user, action = "auto status update entry")
		return context
	
	def get_queryset(self):
		currentDate = datetime.datetime.now().date()
		qs = DailyStatusAuto.objects.filter(LogDate=currentDate)
		if qs.exists():
			return DailyStatusAuto.objects.filter(LogDate=currentDate)
	
class AdminView(LoginRequiredMixin, TemplateView):
	template_name = "admin.html"
	
	def get_context_data(self, **kwargs):
		context = super(AdminView, self).get_context_data(**kwargs)
		context['user'] = self.request.user
		return context
		
class UpcomingProjForm(LoginRequiredMixin, CreateView):
	template_name = 'formUpcoming.html'
	form_class = UpcomingProject
	success_url = '/StatusAdmin/upcomingList/'
	
class ListUpcoming(LoginRequiredMixin, ListView):
	template_name = 'upccmingProjList.html'
	queryset = UpcomingProj.objects.all();
	
class DeleteUpcoming(LoginRequiredMixin, DeleteView):
	model = UpcomingProj
	template_name = 'upcomingproj_confirm_delete.html'
	success_url = '/StatusAdmin/upcomingList/'
	
class ListLog(LoginRequiredMixin, ListView):
	template_name = 'log.html'
	queryset = logging.objects.all();