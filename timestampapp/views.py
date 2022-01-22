from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from .models import UuidTimeStamp
import uuid
from collections import OrderedDict


# Create your views here.


@csrf_exempt
@require_GET
def uuid_timestamp_view(request):
    # create uuid4 code
    # create UuidTimeStamp object
    # call save method to ensure the backend save override runs
    uuid_code = uuid.uuid4()
    uuid_timestamp = UuidTimeStamp.objects.create(uuid_code=uuid_code)
    uuid_timestamp.save()

    # get value list of objects in database
    values_list = UuidTimeStamp.objects.values_list(
        "timestamp_str", 
        "uuid_code"
    )

    # create an ordered dict using values
    ordered_dict = OrderedDict(values_list)
    
    # return Json response.
    return JsonResponse(ordered_dict)