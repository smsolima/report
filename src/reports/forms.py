from django.forms import ModelForm ,Textarea
from reports.models import DailyReport ,ReportActivity
from django import forms
class ReportActivityForm(ModelForm):

    class Meta:
            model=ReportActivity
            fields=['activity','cp','area','description','remarks']
            # widgets={
            #     'description':Textarea(attrs={'cols':100 ,'rows':3 }),
            #     'remarks':Textarea(attrs={'cols':100 ,'rows':3}),
            # }



    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['description'].widget.attrs.update({'class':'description'})


class DailyReportForm(ModelForm):

    class Meta:
        model=DailyReport
        fields='__all__'
       




