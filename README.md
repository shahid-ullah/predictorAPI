
## To clone this project you must have git LFS installed. 

See post on [git lfs](https://mydeveloperplanet.com/2018/10/31/git-lfs-why-and-how-to-use/) for details.


## An Example of API Call using python Requests module
```
>>> import requests
>>> import json
>>> import time
```


```
>>> dic = {'from_office_id': 28, 'from_office_unit_id': 4643,
		   'from_officer_id': 77162, 'from_officer_designation_id': 2088,
		   'to_office_id': 2088, 'to_office_unit_id': 10456,
		   'to_officer_id': 86, 'to_officer_designation_id': 4486
       	}
```

```
>>> json_data = json.dumps(dic)
>>> payload = {'data': json_data}
```

```
>>> response = requests.get("http://localhost:8000/api/", params=payload)
>>> response_text = response.text
>>> user_id = json.loads(response_text)

>>> user_id
{'user_id': 11783}


```
