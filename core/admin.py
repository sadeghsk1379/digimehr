from django.contrib import admin

from .models import Institute, Payment, Plan, UserPlan

# Register your models here.


admin.site.register(Institute)
admin.site.register(Plan)
admin.site.register(UserPlan)
admin.site.register(Payment)
