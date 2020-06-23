import json

import numpy as np
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .apps import RecipientFinderConfig

# list of required attribute
required_features = [
    'to_office_id', 'to_office_unit_id', 'to_officer_id', 'to_officer_designation_id',
    'from_officer_id', 'from_officer_designation_id', 'from_office_id', 'from_office_unit_id',
]


@csrf_exempt
def call_model(request):
    if request.method == 'POST':
        json_data = request.body

        # Check required json data as keyword argument
        try:
            dic_data = json.loads(json_data)
        except:
            res = {"Required": "json data"}
            return JsonResponse(res)

        # Check Required attribute of training model
        try:
            # canpuring data in list
            input_feature_list = [int(dic_data[feature]) for feature in required_features]
        except KeyError as key_error:
            res = {"Required": str(key_error)}
            return JsonResponse(res)

        # Convert feature list to numpy array
        arr = np.array(input_feature_list)
        arr = arr.reshape(1, -1)

        # Find prediction
        prediction = RecipientFinderConfig.model_.predict(arr)

        # Return response user id
        json_formate = {'user_id': int(prediction[0])}
        return JsonResponse(json_formate)


    if request.method == 'GET':
        res = {"Required": "post request"}
        return JsonResponse(res)