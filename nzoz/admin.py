from django.contrib import admin
from .models import Clinic
from .models import Specialty
from .models import Day
from .models import Specialist
from .models import Schedule

admin.site.register(Clinic)
admin.site.register(Specialty)
admin.site.register(Day)
admin.site.register(Specialist)
admin.site.register(Schedule)


