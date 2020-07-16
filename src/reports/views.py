from django.shortcuts import render ,get_object_or_404 ,redirect
from django.utils import timezone
# from django.core.context_processors import csrf
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from reports.models import DailyReport  ,ReportActivity ,Account
from django.urls import reverse_lazy
from reports.forms import ReportActivityForm ,DailyReportForm 
from django.forms import inlineformset_factory ,modelformset_factory
import getpass

class DailyReportListView(ListView):
        model=DailyReport       
     

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["now"] = timezone.now()
          
            return context

def dailyreportlist(request):
    reports=DailyReport.objects.order_by('-id')
    activities=ReportActivity.objects.all()
    users=Account.objects.order_by('username')
    user_name=getpass.getuser()
    account=Account.objects.get(username=user_name)
    
    args={}
    args['reports']=reports
    args['activities']=activities
    args["users"]=users
    args['user_name']=user_name
    args['account_now']=account

    return render (request ,'reports/dailyreport_list.html',args)
class DailyReportUpdate(UpdateView):
    model=DailyReport
    fields='__all__'   

class CreateDailyReport(CreateView):
    model=DailyReport
    fields="__all__"
    
    
class DailyReportDelete(DeleteView):
    model=DailyReport
    success_url=reverse_lazy('dailyreport_list')

class DailyReportDetail(DetailView):
    model=DailyReport
    
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] =timezone.now() 
        return context

def report_detail(request,pk):
    report=DailyReport.objects.get(id = pk)
  
    account=Account.objects.get(id =report.created_by_id )

    activity=ReportActivity.objects.filter(reportnumber_id = pk)
  
    args={}
    args["report"]=report
    args['account']=account
    args['activities']=activity

    return render (request ,'reports/dailyreport_detail.html',args)
def insertreport(request,pk):
    ActivityFormSet=inlineformset_factory(DailyReport,ReportActivity,fields=('description',))
    activity_form=DailyReport.objects.get(id=pk)
    formset=ActivityFormSet(instance=activity_form)
    if request.method=="POST":
        report_form=DailyReportForm(request.POST)
        formset=ActivityFormSet(request.POST,instance=activity_form)
        # activity_form=ReportActivityForm(request.POST)
        # activity_form=DailyReport.objects.get(id=pk)
        # formset=ActivityFormSet(instance=activity_form)
        if report_form.is_valid() and formset.is_valid:
        # if report_form.is_valid() and activity_form.is_valid:
            activity=formset.save()
            report=report_form.save(False)
            
            report.activity=activity
            report.save()
            return redirect('dailyreport_list')
        

    else:
        report_form=DailyReportForm()
        # activity_form=ReportActivityForm() 
        formset=ReportActivityForm()       
    args={}
    # args.update(csrf(request))
    args['report_form']=report_form 
    # args['activity_form']=activity_form
    args['activity_form']=formset
    return render(request,'reports/insert.html',args)



def addreport(request):
    if request.method=="POST":
        report_form=DailyReportForm(request.POST)
        activity_form=ReportActivityForm(request.POST)
        if report_form.is_valid() and activity_form.is_valid:
            activity=activity_form.save(False)
            report=report_form.save(False)
            activity.reportnumber_id=report.id
          
            report.activity=activity
            report.save()
            activity.reportnumber_id=report.id
            activity.save()
            return redirect('dailyreport_list')
    else:
        report_form=DailyReportForm()
        activity_form=ReportActivityForm()       
    args={}
    args['report_form']=report_form 
    args['activity_form']=activity_form
    
    return render(request,'reports/addreport.html',args)

def insertmulti(request,id):
    report=DailyReport.objects.get(pk=id)
    activityformset=modelformset_factory(ReportActivity,fields=('activity','cp','area','description','remarks'))
    if request.method =="POST":
        formset=activityformset(request.POST ,queryset=ReportActivity.objects.filter(reportnumber=id))
        if formset.is_valid():
            instances=formset.save(commit=False)
            for instance in instances:
                instance.reportnumber_id=id
                instance.save()
            return redirect('newactivity',id=id)    

    formset=activityformset(queryset=ReportActivity.objects.filter(reportnumber=id))

    return render(request ,'reports/newactivity.html',{'formset':formset})





def newactivity(request,id):
   
    activityformset=modelformset_factory(ReportActivity,fields=('activity','cp','area','description','remarks'))
    if request.method =="POST":
        formset=activityformset(request.POST ,queryset=ReportActivity.objects.filter(reportnumber_id=id))
        if formset.is_valid():
            instances=formset.save(commit=False)
            for instance in instances:
                instance.reportnumber_id=id
                instance.save()
            return redirect('newactivity',id=id)    

    formset=activityformset(queryset=ReportActivity.objects.filter(reportnumber=id))

    return render(request ,'reports/newactivity.html',{'formset':formset})


def newreport(request):
   
    if request.method=="POST":
        report_form=DailyReportForm(request.POST)
        
        if report_form.is_valid():
            instance=report_form.save()
           
            return redirect('newactivity',id=instance.id)
    else:
        report_form=DailyReportForm()
          
    args={}
    user=getpass.getuser()
    account=Account.objects.get(username=user)
    args['form']=report_form 
    args['user']=account
    return render(request,'reports/newreport.html',args)    

def showall(request):
    args={}
    allreports=DailyReport.objects.all()
    for num in allreports:
        activities=ReportActivity.objects.filter(reportnumber_id=num.id)
        report={"reports":num}
        args["reports"]=num
        for act in activities:
             activity={"activities":act}
             args['activities'] =act
           
    return render(request ,'reports/all.html',args)



def dashboard(request):
  
    
    total=DailyReport.objects.count()
    totalactivities=ReportActivity.objects.count()
    

    context={}
    context['total']=total
    context['activities']= totalactivities
    template="reports/dashboard.html"
    return render(request ,template ,context)    
# Create your views here.
# class InsetReport(CreateView):
#     form_class = ReportMultiForm
#     success_url = reverse_lazy('dailyreport_list')

#     def form_valid(self, form):
#         # Save the user first, because the profile needs a user before it
#         # can be saved.
#         activity = form['activity'].save()
#         report = form['report'].save(commit=False)
#         report.activity = activity
#         report.save()
#         return redirect(self.get_success_url())
    
#     # form={}
#     # # instance=[get_object_or_404(Weather)]
#     # context={"form":form}
#     # template="reports/add.html"
#     # return render (request ,template,context)



