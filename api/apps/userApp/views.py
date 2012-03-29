from django.http import HttpResponse
import json
#from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
def register(request):
    return HttpResponse(json.dumps({"email":request.POST['email']}))

