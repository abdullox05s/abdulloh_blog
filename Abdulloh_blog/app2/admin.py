from django.contrib import admin

from .models import *

admin.site.register([Home,About_me,My_life,My_achchivements,
                     My_status_for_future,Surprising_situations,My_portfolio, My_images])
