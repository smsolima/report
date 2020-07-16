

from django.urls import path ,include
from reports.views import CreateDailyReport,showall ,DailyReportListView ,DailyReportUpdate ,DailyReportDetail ,insertreport ,addreport ,report_detail ,newreport,newactivity ,dailyreportlist ,dashboard

urlpatterns = [
   
    path('',dailyreportlist,name="dailyreport_list"),
    path('dashboard',dashboard,name='dashboard'),
    path('insert/<int:pk>',insertreport, name="create_report"),
    path('new/',newreport ,name="newreport") ,
    path('new/<int:id>',newactivity ,name="newactivity") ,
    path('add/',addreport ,name="addreport") ,
    path('<int:pk>/',report_detail ,name="report_detail"),
    path('edit/<int:pk>/',DailyReportUpdate.as_view() ,name="update_report"),
    path('show/',showall,name="showall"),

]