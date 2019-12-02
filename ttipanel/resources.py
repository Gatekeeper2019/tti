from import_export import resources
from.models import Paulapplication


class PaulapplicationResource(resources.ModelResource):

    class Meta:
        model = Paulapplication


class TimothyapplicationAdmin(resources.ModelResource):

    class Meta:
        model = Paulapplication
 
