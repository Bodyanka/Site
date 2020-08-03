import os
import datetime
from .models import File
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView


class FileUpload(CreateView):
    model = File

    fields = ['hours_to_delete', 'minutes_to_delete', 'file_itself']


class FileDownload(generic.ListView):
    model = File
    template_name = 'sharingsite/download.html'
    context_object_name = 'all_files'

    def get_queryset(self, *args, **kwargs):
        mass = File.objects.filter(file_link=self.request.GET.get('file_link'))

        y = mass[0].cur_year
        mon = mass[0].cur_month
        d = mass[0].cur_day
        h = mass[0].hours_to_delete
        minutes = mass[0].minutes_to_delete

        cur_time = datetime.datetime.now()

        del_time = datetime.datetime(y, mon, d, h, minutes, 0)

        if len(mass) == 0 or (del_time - cur_time).days < 0:
            try:
                os.remove(os.path.join('media/', str(mass[0].file_itself)))
            except:
                pass
            raise Http404('Wrong/empty file link, or living time is expired')
        else:
            return mass


class Link(generic.DetailView):
    model = File
    template_name = 'sharingsite/link.html'
