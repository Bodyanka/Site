# python manage.py makemigrations
# python manage.py migrate

import datetime
import random
from django.db import models
from django.urls import reverse


class File(models.Model):
    file_link = models.CharField(max_length=200)
    file_itself = models.FileField()

    cur_year = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    cur_month = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    cur_day = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    hours_to_delete = models.DecimalField(max_digits=2, decimal_places=0, default=1)
    minutes_to_delete = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def get_absolute_url(self):

        def gen_link(my_id):
            link = ''
            links = []
            my = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

            for i in File.objects.all():
                links.append(i.file_link)

            curfile = File.objects.get(pk=my_id)

            for i in range(30):
                link += random.choice(my)

            if link not in links:
                curfile.file_link = link
                curfile.save()
            else:
                gen_link(my_id)
            return curfile

        time_file = File.objects.get(pk=self.pk)

        ct = datetime.datetime.now()

        del_time = datetime.datetime(ct.year, ct.month, ct.day, ct.hour,
                                     ct.minute) + datetime.timedelta(hours=int(time_file.hours_to_delete),
                                                                     minutes=int(time_file.minutes_to_delete))

        time_file.cur_year = del_time.year
        time_file.cur_month = del_time.month
        time_file.cur_day = del_time.day
        time_file.hours_to_delete = del_time.hour
        time_file.minutes_to_delete = del_time.minute

        time_file.save()

        return reverse('sharingsite:link', kwargs={'pk': gen_link(self.pk).pk})

    def __str__(self):
        return '----------Primary Key: ' + str(self.pk) + \
               '\n----------Hours to delete: ' + str(self.hours_to_delete) + \
               '\n----------Minutes to delete: ' + str(self.minutes_to_delete) + \
               '\n----------File Name: ' + str(self.file_itself) + \
               '\n----------File Link: ' + str(self.file_link)
