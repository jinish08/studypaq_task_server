import requests

def striped_data():
    req =  requests.get("https://www.reddit.com/r/images/new.json?limit=30")
    data =  req.json()
    # print(data)
    # print(req.status_code)
    if req.status_code == 200 and "data" in data:
        actual_data = data['data']
        data_dict = {"data": []}
        if "children" in actual_data:
            for i in range(0, len(actual_data['children'])):
                if "preview" in actual_data['children'][i]["data"]:
                    data_dict['data'].append(actual_data['children'][i]["data"]["preview"]["images"][0]["source"]["url"])
        return data_dict
    else:
        content = {'message': 'Something went wrong'}
        return content, req.status_code


def verify_user(info):
    if(info['username'] == "test" and info['password'] == "test"):
        return True
    else:
        return False
    
