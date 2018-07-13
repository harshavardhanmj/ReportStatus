from django.db import models
from django.db.models.signals import post_save, pre_save
from django.core.urlresolvers import reverse
from django.db.models import Q

# Create your models here.
class DailyStatusQC(models.Model):
	QC_STATUS = (('Test Preparation - In Progress', 'Test Preparation - In Progress'),('Testing - In Progress', 'Testing - In Progress'),('Testing - Completed', 'Testing - Completed'))
	ProductName = models.CharField(max_length=100,blank=True,null=True)
	#ReleaseVersion = models.CharField(max_length=30,blank=True,null=True)
	CurrentStatus = models.CharField(max_length=100,blank=True,null=True,choices=QC_STATUS)
	PlanStartDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	PlanEndDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	IssuesLogged = models.CharField(max_length=100,blank=True,null=True)
	LogDate = models.DateField(auto_now=False, auto_now_add=True)
	Remarks = models.CharField(max_length=500,blank=True,null=True)
	
	def __str__(self):
		return self.ProductName
	
	def get_absolute_url(self):
		return reverse('QcStatusEntryUpdate', kwargs={'pk': self.pk})
		
class DailyStatusPQ(models.Model):
	PQ_STATUS = (('IQ,OQ,PQ Script drafting', 'IQ,OQ,PQ Script drafting'),('IQ,OQ,PQ Script dryrun', 'IQ,OQ,PQ Script dryrun'),('IQ execution In-Progress', 'IQ execution In-Progress'),('IQ completed', 'IQ completed'),('OQ execution In-Progress', 'OQ execution In-Progress'),('OQ completed', 'OQ completed'),('PQ execution In-Progress', 'PQ execution In-Progress'),('PQ completed', 'PQ completed'))
	ProductName = models.CharField(max_length=100,blank=True,null=True)
	#ReleaseVersion = models.CharField(max_length=30,blank=True,null=True)
	CurrentStatus = models.CharField(max_length=100,blank=True,null=True,choices=PQ_STATUS)
	PlanStartDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	PlanEndDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	IssuesLogged = models.CharField(max_length=100,blank=True,null=True)
	LogDate = models.DateField(auto_now=False, auto_now_add=True)
	Remarks = models.CharField(max_length=500,blank=True,null=True)
	
	def __str__(self):
		return self.ProductName
	
	def get_absolute_url(self):
		return reverse('PqStatusEntryUpdate', kwargs={'pk': self.pk})
	

class DailyStatusAuto(models.Model):
	AUTO_STATUS = (('Scripting', 'Scripting'),('Stability Phase', 'Stability Phase'),('Scripting Completed', 'Scripting Completed'))
	ProductName = models.CharField(max_length=100,blank=True,null=True)
	#ReleaseVersion = models.CharField(max_length=30,blank=True,null=True)
	CurrentStatus = models.CharField(max_length=100,blank=True,null=True,choices=AUTO_STATUS)
	PlanStartDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	PlanEndDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	TotalScenarios = models.CharField(max_length=100,blank=True,null=True)
	ScenariosCovered = models.CharField(max_length=100,blank=True,null=True)
	ScenariosInprogress = models.CharField(max_length=100,blank=True,null=True)
	LogDate = models.DateField(auto_now=False, auto_now_add=True)
	Remarks = models.CharField(max_length=500,blank=True,null=True)
	
	def __str__(self):
		return self.ProductName
	
	def get_absolute_url(self):
		return reverse('AutoStatusEntryUpdate', kwargs={'pk': self.pk})

PROJ_STATUS = (('Active', 'Active'),('Inactive', 'Inactive'))
		
class ProjectAuto(models.Model):
	ProductName = models.CharField(max_length=100,blank=True,null=True)
	#ReleaseVersion = models.CharField(max_length=30,blank=True,null=True)
	PlanStartDate = models.DateField(auto_now=False, auto_now_add=False)
	PlanEndDate = models.DateField(auto_now=False, auto_now_add=False)
	ProductStatus = models.CharField(max_length=100,blank=True,null=True,choices=PROJ_STATUS,default=PROJ_STATUS[0][0])
	Remarks = models.CharField(max_length=500,blank=True,null=True)
	TempPlanStartDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	TempPlanEndDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	LogDate = models.DateField(auto_now=False, auto_now_add=True)
	
	def __str__(self):
		return self.ProductName
	
	def get_absolute_url(self):
		return reverse('UpdateProjectAuto', kwargs={'pk': self.pk})
	
def pre_save_creDateAuto_receiver(sender, instance, *args, **kwargs):
	if instance.PlanStartDate:
		if not instance.TempPlanStartDate:
			#createObj = ProjectQC.objects.get(Q(ProductName__iexact=instance.ProductName) & Q(ReleaseVersion__iexact=instance.ReleaseVersion))
			instance.TempPlanStartDate = instance.PlanStartDate
	if instance.PlanEndDate:
		if not instance.TempPlanEndDate:
			#createObj = ProjectQC.objects.get(Q(ProductName__iexact=instance.ProductName) & Q(ReleaseVersion__iexact=instance.ReleaseVersion))
			instance.TempPlanEndDate = instance.PlanEndDate
pre_save.connect(pre_save_creDateAuto_receiver, sender=ProjectAuto)
		
class ProjectPq(models.Model):
	ProductName = models.CharField(max_length=100,blank=True,null=True)
	#ReleaseVersion = models.CharField(max_length=30,blank=True,null=True)
	PlanStartDate = models.DateField(auto_now=False, auto_now_add=False)
	PlanEndDate = models.DateField(auto_now=False, auto_now_add=False)
	ProductStatus = models.CharField(max_length=100,blank=True,null=True,choices=PROJ_STATUS,default=PROJ_STATUS[0][0])
	Remarks = models.CharField(max_length=500,blank=True,null=True)
	TempPlanStartDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	TempPlanEndDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	LogDate = models.DateField(auto_now=False, auto_now_add=True)
	
	def __str__(self):
		return self.ProductName
		
	def get_absolute_url(self):
		return reverse('UpdateProjectPq', kwargs={'pk': self.pk})
	
def pre_save_creDatePq_receiver(sender, instance, *args, **kwargs):
	if instance.PlanStartDate:
		if not instance.TempPlanStartDate:
			#createObj = ProjectQC.objects.get(Q(ProductName__iexact=instance.ProductName) & Q(ReleaseVersion__iexact=instance.ReleaseVersion))
			instance.TempPlanStartDate = instance.PlanStartDate
	if instance.PlanEndDate:
		if not instance.TempPlanEndDate:
			#createObj = ProjectQC.objects.get(Q(ProductName__iexact=instance.ProductName) & Q(ReleaseVersion__iexact=instance.ReleaseVersion))
			instance.TempPlanEndDate = instance.PlanEndDate
pre_save.connect(pre_save_creDatePq_receiver, sender=ProjectPq)
		
class ProjectQC(models.Model):
	ProductName = models.CharField(max_length=100,blank=True,null=True)
	#ReleaseVersion = models.CharField(max_length=30,blank=True,null=True)
	PlanStartDate = models.DateField(auto_now=False, auto_now_add=False)
	PlanEndDate = models.DateField(auto_now=False, auto_now_add=False)
	ProductStatus = models.CharField(max_length=100,blank=True,null=True,choices=PROJ_STATUS,default=PROJ_STATUS[0][0])
	Remarks = models.CharField(max_length=500,blank=True,null=True)
	TempPlanStartDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	TempPlanEndDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	LogDate = models.DateField(auto_now=False, auto_now_add=True)
	
	def __str__(self):
		return self.ProductName
		
	def get_absolute_url(self):
		return reverse('UpdateProjectQc', kwargs={'pk': self.pk})
	
def pre_save_creDateQc_receiver(sender, instance, *args, **kwargs):
	if instance.PlanStartDate:
		if not instance.TempPlanStartDate:
			#createObj = ProjectQC.objects.get(Q(ProductName__iexact=instance.ProductName) & Q(ReleaseVersion__iexact=instance.ReleaseVersion))
			instance.TempPlanStartDate = instance.PlanStartDate
	if instance.PlanEndDate:
		if not instance.TempPlanEndDate:
			#createObj = ProjectQC.objects.get(Q(ProductName__iexact=instance.ProductName) & Q(ReleaseVersion__iexact=instance.ReleaseVersion))
			instance.TempPlanEndDate = instance.PlanEndDate
pre_save.connect(pre_save_creDateQc_receiver, sender=ProjectQC)

class UpcomingProj(models.Model):
	ProductName = models.CharField(max_length=100,blank=True,null=True)
	
	def __str__(self):
		return self.ProductName

class logging(models.Model):
	user = models.CharField(max_length=100,blank=True,null=True)
	action = models.CharField(max_length=100,blank=True,null=True)
	LogDate = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
	
	def __str__(self):
		return self.user

class graphData(models.Model):
	projectName = models.CharField(max_length=100,blank=True,null=True)
	plotDate = models.CharField(max_length=100,blank=True,null=True)
	issueLogged = models.CharField(max_length=100,blank=True,null=True)
	issueClosed = models.CharField(max_length=100,blank=True,null=True)
	
	def __str__(self):
		return self.plotDate