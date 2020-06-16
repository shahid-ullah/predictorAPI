import json

import numpy as np
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .apps import RecipientFinderConfig

# list of required attribute
required_features= [
    'to_office_id', 'to_office_unit_id', 'to_officer_id', 'to_officer_designation_id',
    'from_officer_id', 'from_officer_designation_id', 'from_office_id', 'from_office_unit_id',
]

def http_method_list(methods):
    def http_methods_decorator(func):
        def function_wrapper(self, request, **kwargs):
            methods = [method.upper() for method in methods]
            if not request.method.upper() in methods:
                return HttpResponse(status=405) # not allowed

            return func(self, request, **kwargs)
        return function_wrapper
    return http_methods_decorator


def preprocess_requested_data(json_data):
    try:
        # convert json data in python dictionary
        dic_data = json.loads(json_data)
    except:
        return HttpResponse("Provide json data in right format")

    try:
    # canpuring data in list
        input_feature_list = [int(dic_data[feature]) for feature in required_features]
        # print(f"input feature list: {input_feature_list}")
    except KeyError as key_error:
        return HttpResponse(f"please provide {key_error} ID")
    arr = np.array(input_feature_list)
    arr = arr.reshape(1, -1)

    return arr




# @http_method_list(['GET'])
def call_model(request):
    if request.method == 'POST':
        return HttpResponse('Call prediction api with get method')

    if request.method == 'GET':
        try:
            json_data = request.GET['data'] # get the json data
            # return HttpResponse(json_data)
        except KeyError:
            return HttpResponse("Provide 'data' as a key in request method")

        arr = preprocess_requested_data(json_data)
        prediction = RecipientFinderConfig.model_.predict(arr)
        # return HttpResponse(arr)
        json_formate = {'user_id': str(prediction[0])}
        return JsonResponse(json_formate)
