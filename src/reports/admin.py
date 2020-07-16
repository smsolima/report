from django.contrib import admin
from reports.models import DailyReport ,Cp ,Weather,Wind ,Activity ,Area ,ReportActivity
from account.models import Account ,Discipline
# Register your models here.

admin.site.register(Weather)
admin.site.register(Wind)
admin.site.register(Cp)
admin.site.register(Account)
admin.site.register(Discipline)
admin.site.register(DailyReport)
admin.site.register(Activity)
admin.site.register(Area)
admin.site.register(ReportActivity)