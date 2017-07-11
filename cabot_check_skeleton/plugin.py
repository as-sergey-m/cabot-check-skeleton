from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from cabot.cabotapp.modelcategories.common import StatusCheck
from cabot.cabotapp.modelcategories.common import StatusCheckResult
from os import environ as env
from cabot.cabotapp.views import CheckCreateView
from cabot.cabotapp.views import CheckUpdateView
from cabot.cabotapp.views import StatusCheckForm

class SkeletonStatusCheck(StatusCheck):
    edit_url_name = 'update-skeleton-check'
    duplicate_url_name = 'duplicate-skeleton-check'
    class Meta(StatusCheck.Meta):
        proxy = True

    check_name = 'skeleton'

    def run(self):

        print ('running skeleton check')
        result = StatusCheckResult(status_check=self)
        result.success = True
        return result


    def description(self, check):
        return '%s in list of bones.' % check.bone_name

class SkeletonStatusCheckForm(StatusCheckForm):

    class Meta:
        model = SkeletonStatusCheck
        fields = (
            'name',
            'metric',
            'check_type',
            'value',
            'frequency',
            'active',
            'importance',
            'expected_num_hosts',
            'allowed_num_failures',
            'debounce',
        )

class SkeletonCheckCreateView(CheckCreateView):
    model = SkeletonStatusCheck
    form_class = SkeletonStatusCheckForm

class SkeletonCheckUpdateView(CheckUpdateView):
    model = SkeletonStatusCheck
    form_class = SkeletonStatusCheckForm

def duplicate_check(request, pk):
    pc = StatusCheck.objects.get(pk=pk)
    npk = pc.duplicate()
    return HttpResponseRedirect(reverse('update-skeleton-check', kwargs={'pk': npk}))
