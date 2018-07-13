import datetime
from django import forms
from django.db.models import Q
from .models import DailyStatusQC, DailyStatusAuto, ProjectQC, ProjectAuto, ProjectPq, DailyStatusPQ, UpcomingProj
class DailyStatusForm(forms.ModelForm):
	class Meta:
		model = DailyStatusQC
		fields = ['ProductName', 'CurrentStatus', 'PlanStartDate', 'PlanEndDate', 'IssuesLogged', 'Remarks']
	
	def clean(self):
		#ReleaseVersion = self.cleaned_data.get("ReleaseVersion")
		ProductName = self.cleaned_data.get("ProductName")
		currentDate = datetime.datetime.now().date()
		qs2 = DailyStatusQC.objects.filter(Q(ProductName__iexact=ProductName) & Q(LogDate=currentDate))
		if qs2:
			raise forms.ValidationError("Already Posted")
		return

class DailyStatusUpdateForm(forms.ModelForm):
	class Meta:
		model = DailyStatusQC
		fields = ['ProductName', 'CurrentStatus', 'IssuesLogged']
	
	def __init__(self, *args, **kwargs):
		super(DailyStatusUpdateForm, self).__init__(*args, **kwargs)
		self.fields['ProductName'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductName'].widget.attrs['readonly'] = True
		#self.fields['ReleaseVersion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['CurrentStatus'].widget.attrs.update({'class' : 'form-control'})
		self.fields['IssuesLogged'].widget.attrs.update({'class' : 'form-control'})

class PqDailyStatusForm(forms.ModelForm):
	class Meta:
		model = DailyStatusPQ
		fields = ['ProductName', 'CurrentStatus', 'PlanStartDate', 'PlanEndDate', 'IssuesLogged', 'Remarks']
	
	def clean(self):
		#ReleaseVersion = self.cleaned_data.get("ReleaseVersion")
		ProductName = self.cleaned_data.get("ProductName")
		currentDate = datetime.datetime.now().date()
		qs2 = DailyStatusPQ.objects.filter(Q(ProductName__iexact=ProductName) & Q(LogDate=currentDate))
		if qs2:
			raise forms.ValidationError("Already Posted")
		return

class PqDailyStatusUpdateForm(forms.ModelForm):
	class Meta:
		model = DailyStatusPQ
		fields = ['ProductName', 'CurrentStatus', 'IssuesLogged']
	
	def __init__(self, *args, **kwargs):
		super(PqDailyStatusUpdateForm, self).__init__(*args, **kwargs)
		self.fields['ProductName'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductName'].widget.attrs['readonly'] = True
		#self.fields['ReleaseVersion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['CurrentStatus'].widget.attrs.update({'class' : 'form-control'})
		self.fields['IssuesLogged'].widget.attrs.update({'class' : 'form-control'})

class AutoDailyStatusForm(forms.ModelForm):
	class Meta:
		model = DailyStatusAuto
		fields = ['ProductName', 'CurrentStatus', 'PlanStartDate', 'PlanEndDate', 'TotalScenarios', 'ScenariosCovered', 'ScenariosInprogress', 'Remarks']
		
	def clean(self):
		#ReleaseVersion = self.cleaned_data.get("ReleaseVersion")
		ProductName = self.cleaned_data.get("ProductName")
		currentDate = datetime.datetime.now().date()
		qs2 = DailyStatusAuto.objects.filter(Q(ProductName__iexact=ProductName) & Q(LogDate=currentDate))
		if qs2:
			raise forms.ValidationError("Already Posted")
		return

class AutoDailyStatusUpdateForm(forms.ModelForm):
	class Meta:
		model = DailyStatusAuto
		fields = ['ProductName', 'CurrentStatus', 'TotalScenarios', 'ScenariosCovered', 'ScenariosInprogress']
	
	def __init__(self, *args, **kwargs):
		super(AutoDailyStatusUpdateForm, self).__init__(*args, **kwargs)
		self.fields['ProductName'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductName'].widget.attrs['readonly'] = True
		#self.fields['ReleaseVersion'].widget.attrs.update({'class' : 'form-control'})
		self.fields['CurrentStatus'].widget.attrs.update({'class' : 'form-control'})
		self.fields['TotalScenarios'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ScenariosCovered'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ScenariosInprogress'].widget.attrs.update({'class' : 'form-control'})
		
class CreateProjectForm(forms.ModelForm):
	class Meta:
		model = ProjectQC
		fields = ['ProductName', 'PlanStartDate', 'PlanEndDate', 'ProductStatus', 'Remarks']
	
	def clean(self):
		PlanStartDate = self.cleaned_data.get("PlanStartDate")
		PlanEndDate = self.cleaned_data.get("PlanEndDate")
		error_messages = []
		if PlanStartDate >  PlanEndDate:
			raise forms.ValidationError("Enter Valid dates")
		return self.cleaned_data
	
	def clean_ProductName(self):
		ProductName = self.cleaned_data.get("ProductName")
		if "." not in ProductName:
			raise forms.ValidationError("Please Enter Project as in Jira")
		return ProductName

		
class DateInput(forms.DateInput):
	input_type = 'date'


class UpdateProjectQcForm(forms.ModelForm):
	class Meta:
		model = ProjectQC
		fields = ['ProductName', 'PlanStartDate', 'PlanEndDate', 'ProductStatus', 'Remarks']
		widgets = {
            'PlanStartDate': DateInput(), 'PlanEndDate': DateInput()
        }
	
	def __init__(self, *args, **kwargs):
		super(UpdateProjectQcForm, self).__init__(*args, **kwargs)
		self.fields['ProductName'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductName'].widget.attrs['readonly'] = True
		#self.fields['ReleaseVersion'].widget.attrs.update({'class' : 'form-control'})
		#self.fields['ReleaseVersion'].widget.attrs['readonly'] = True
		self.fields['PlanStartDate'].widget.attrs.update({'class' : 'form-control'})
		self.fields['PlanEndDate'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductStatus'].widget.attrs.update({'class' : 'form-control'})
		self.fields['Remarks'].widget.attrs.update({'class' : 'form-control'})
		
	def clean(self):
		PlanStartDate = self.cleaned_data.get("PlanStartDate")
		PlanEndDate = self.cleaned_data.get("PlanEndDate")
		if PlanStartDate >  PlanEndDate:
			raise forms.ValidationError("Enter Valid dates")
		return


class UpdateProjectAutoForm(forms.ModelForm):
	class Meta:
		model = ProjectAuto
		fields = ['ProductName', 'PlanStartDate', 'PlanEndDate', 'ProductStatus', 'Remarks']
		widgets = {
            'PlanStartDate': DateInput(), 'PlanEndDate': DateInput()
        }
	
	def __init__(self, *args, **kwargs):
		super(UpdateProjectAutoForm, self).__init__(*args, **kwargs)
		self.fields['ProductName'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductName'].widget.attrs['readonly'] = True
		#self.fields['ReleaseVersion'].widget.attrs.update({'class' : 'form-control'})
		#self.fields['ReleaseVersion'].widget.attrs['readonly'] = True
		self.fields['PlanStartDate'].widget.attrs.update({'class' : 'form-control'})
		self.fields['PlanEndDate'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductStatus'].widget.attrs.update({'class' : 'form-control'})
		self.fields['Remarks'].widget.attrs.update({'class' : 'form-control'})
		
	def clean(self):
		PlanStartDate = self.cleaned_data.get("PlanStartDate")
		PlanEndDate = self.cleaned_data.get("PlanEndDate")
		if PlanStartDate >  PlanEndDate:
			raise forms.ValidationError("Enter Valid dates")
		return


class UpdateProjectPqForm(forms.ModelForm):
	class Meta:
		model = ProjectPq
		fields = ['ProductName', 'PlanStartDate', 'PlanEndDate', 'ProductStatus', 'Remarks']
		widgets = {
            'PlanStartDate': DateInput(), 'PlanEndDate': DateInput()
        }
	
	def __init__(self, *args, **kwargs):
		super(UpdateProjectPqForm, self).__init__(*args, **kwargs)
		self.fields['ProductName'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductName'].widget.attrs['readonly'] = True
		#self.fields['ReleaseVersion'].widget.attrs.update({'class' : 'form-control'})
		#self.fields['ReleaseVersion'].widget.attrs['readonly'] = True
		self.fields['PlanStartDate'].widget.attrs.update({'class' : 'form-control'})
		self.fields['PlanEndDate'].widget.attrs.update({'class' : 'form-control'})
		self.fields['ProductStatus'].widget.attrs.update({'class' : 'form-control'})
		self.fields['Remarks'].widget.attrs.update({'class' : 'form-control'})
		
	def clean(self):
		PlanStartDate = self.cleaned_data.get("PlanStartDate")
		PlanEndDate = self.cleaned_data.get("PlanEndDate")
		if PlanStartDate >  PlanEndDate:
			raise forms.ValidationError("Enter Valid dates")
		return
		

class CreateProjectAutoForm(forms.ModelForm):
	class Meta:
		model = ProjectAuto
		fields = ['ProductName', 'PlanStartDate', 'PlanEndDate', 'ProductStatus', 'Remarks']
	
	def clean_ProductName(self):
		ProductName = self.cleaned_data.get("ProductName")
		if "-" not in ProductName:
			raise forms.ValidationError("Enter Version separated by -")
		return ProductName
		
	def clean(self):
		PlanStartDate = self.cleaned_data.get("PlanStartDate")
		PlanEndDate = self.cleaned_data.get("PlanEndDate")
		if PlanStartDate >  PlanEndDate:
			raise forms.ValidationError("Enter Valid dates")
		return
		
class CreateProjectPqForm(forms.ModelForm):
	class Meta:
		model = ProjectPq
		fields = ['ProductName', 'PlanStartDate', 'PlanEndDate', 'ProductStatus', 'Remarks']
	
	def clean_ProductName(self):
		ProductName = self.cleaned_data.get("ProductName")
		if "-" not in ProductName:
			raise forms.ValidationError("Enter Version separated by -")
		return ProductName
		
	def clean(self):
		PlanStartDate = self.cleaned_data.get("PlanStartDate")
		PlanEndDate = self.cleaned_data.get("PlanEndDate")
		if PlanStartDate >  PlanEndDate:
			raise forms.ValidationError("Enter Valid dates")
		return
		
class SearchForm(forms.Form):
	date = forms.DateField(required=False)
	widgets = {'date': DateInput()}
	
class UpcomingProject(forms.ModelForm):
	class Meta:
		model = UpcomingProj
		fields = ['ProductName']