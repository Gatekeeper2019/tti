from django.contrib import admin
#from rangefilter.filter import  DateTimeRangeFilter
from import_export.admin import ImportExportModelAdmin
from import_export import resources
#from ttipanel.resources import PaulapplicationResources
from .models import Paulapplication
from .models import Timothyapplication
from .models import Quarterly_Church_Planting_Update_Form
# Register your models here.



class PaulapplicationAdmin(ImportExportModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'date_joined', )
    list_filter = ('date_joined',

    )
    search_fields= ('id', 'first_name', 'last_name', 'title', 'date_joined','country_of_Citizenship','state','district', 'pin_code', )
    list_per_page = 10
    date_hierarchy ='date_joined'

#fields = (('title','first_name','last_name'), ('summary','profile_pic'),'join_date','country','state','district', 'pin_code',  )


#class PaulapplicationAdmin(ImportExportModelAdmin):

    #readonly_fields = [..., "headshot_image"]

    #def headshot_image(self, obj):
        #return mark_safe('<img src="{media/profile_pic/}" width="{100}" height={100} />'.format(
            #url = obj.headshot.url,
            #width=obj.headshot.width,
            #height=obj.headshot.height,
            #)
    #)


admin.site.register(Paulapplication, PaulapplicationAdmin)


class TimothyapplicationAdmin(ImportExportModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'date_joined', )
    list_filter = ('date_joined', )
        #search_fields= ('id', 'first_name', 'last_name', 'title', 'join_date','country','state','district', 'pin_code', )
    search_fields= ('id', 'first_name', 'last_name', 'title', 'date_joined','country_of_Citizenship','state','district', 'pin_code', )
    list_per_page = 10
    date_hierarchy ='date_joined'

admin.site.register(Timothyapplication, TimothyapplicationAdmin)



class Quarterly_Church_Planting_Update_FormAdmin(ImportExportModelAdmin):
    list_display=('id', 'National_Regional_Director_Name',  'DATE_OF_REPORTING', )
    list_filter = ('DATE_OF_REPORTING', )
    #search_fields= ('id', 'first_name', 'last_name', 'title', 'join_date','country','state','district', 'pin_code', )
    search_fields= ('id', 'Paul_Name', 'Mobile_Numbers', 'National_Regional_Director_Name', 'DATE_OF_REPORTING','Country','District', 'Email', )
    list_per_page = 10
    date_hierarchy ='DATE_OF_REPORTING'

admin.site.register(Quarterly_Church_Planting_Update_Form, Quarterly_Church_Planting_Update_FormAdmin)
