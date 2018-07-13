from django.contrib import admin
from .models import DailyStatusQC, DailyStatusAuto, ProjectQC, ProjectAuto, ProjectPq, DailyStatusPQ, UpcomingProj, logging, graphData

# Register your models here.
myModels = [DailyStatusAuto, DailyStatusQC, ProjectQC, ProjectAuto, ProjectPq, DailyStatusPQ, UpcomingProj, logging, graphData]
admin.site.register(myModels)