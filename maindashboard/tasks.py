from __future__ import absolute_import, unicode_literals
from celery import task
from celery.decorators import task
import datetime
from datetime import timedelta
import requests
from requests.auth import HTTPBasicAuth
import json
from django.db.models import Q

@task(name="task_number_one")
def task_number_one():
	if datetime.date.today().weekday() == 4:
		print("inside")
		from DisStatus.models import DailyStatusQC, ProjectQC, graphData
		projectQcList = ProjectQC.objects.filter(ProductStatus="Active").values('ProductName')
		globalitr = 0
		while globalitr < projectQcList.count():
			itr1 = 0
			issueCount = 0
			proj = projectQcList[globalitr]['ProductName']
			globalitr = globalitr + 1
			totProj = proj.split(",")
			while itr1 < len(totProj):
				closedMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Closed AND priority = Minor ORDER BY key DESC'''
				headers = {'Content-Type': 'application/json'}
				closedMinorResponse = requests.get(closedMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
				geodata1 = closedMinorResponse.json()
				try:
					issueCount = issueCount + int(geodata1["total"]);
				except:
					issueCount = 0;
				itr1 = itr1 + 1
			try:
				closed1 = issueCount
			except:
				closed1 = "0"
			itr1 = 0
			issueCount = 0
			while itr1 < len(totProj):
				closedMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Closed AND priority = Major ORDER BY key DESC'''
				headers = {'Content-Type': 'application/json'}
				closedMajorResponse = requests.get(closedMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
				geodata1 = closedMajorResponse.json()
				try:
					issueCount = issueCount + int(geodata1["total"]);
				except:
					issueCount = 0;
				itr1 = itr1 + 1
			try:
				closed2 = issueCount
			except:
				closed2 = "0"
			itr1 = 0
			issueCount = 0
			while itr1 < len(totProj):
				closedCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Closed AND priority = Critical ORDER BY key DESC'''
				headers = {'Content-Type': 'application/json'}
				closedCriticalResponse = requests.get(closedCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
				geodata1 = closedCriticalResponse.json()
				try:
					issueCount = issueCount + int(geodata1["total"]);
				except:
					issueCount = 0;
				itr1 = itr1 + 1
			try:
				closed3 = issueCount
			except:
				closed3 = "0"
			year = datetime.date.today().year
			month = (datetime.date.today().month) - 1
			date = datetime.date.today().day
			graphdate = "" + str(year) + ", " + str(month) + ", " + str(date)
			issueClo = int(closed1) + int(closed2) + int(closed3)
			projIssueLoggedObj = DailyStatusQC.objects.filter(ProductName__iexact=proj)
			if projIssueLoggedObj.exists():
				reqObj = projIssueLoggedObj.last()
				try:
					issue = reqObj.IssuesLogged
				except:
					issue = "0"
				if not graphData.objects.filter(Q(projectName__iexact=proj) & Q(plotDate__iexact=graphdate)):
					graphObj = graphData.objects.create(projectName = proj, plotDate = graphdate, issueLogged = issue, issueClosed = issueClo)
				else:
					qs = graphData.objects.get(Q(projectName__iexact=proj) & Q(plotDate__iexact=graphdate))
					if qs.issueClosed != issueClo:
						qs.issueClosed = issueClo
						qs.save();
					if qs.issueLogged != issue:
						qs.issueLogged = issue
						qs.save();
	else:
		print("No data")