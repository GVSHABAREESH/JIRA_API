# import requests
# import json

# url = 'http://127.0.0.1:8000/projects/'
# res = requests.post(url)
# projects  = "http://127.0.0.1:8000/projects/"
# component = "http://127.0.0.1:8000/component/"
# issue     = "http://127.0.0.1:8000/issues/"
# sprint    = "http://127.0.0.1:8000/sprint/"
# subtask   = "http://127.0.0.1:8000/subtask/"
# comment   = "http://127.0.0.1:8000/comment/"




# payload_project= {'name': 'abcdef','key': 'AB','template_name': 'Bug tracking'}
# post = requests.post(projects, data=(payload_project))
# print post.text


# get = requests.get(projects)
# print get


# import json,requests
# component = "http://127.0.0.1:8000/component/"
# payload_component = ({"project": "AB","name":"Fourth_Component","description":"Adding Component","leadUserName":"Gelivi Mani","assigneeType":"PROJECT_LEAD","isAssigneeTypeValid":True})
# post = requests.post(component,data=(payload_component))
# print post.text



import requests
url = "http://127.0.0.1:8000/issues/"
payload_issues = ({'project':{'key':'AB'},'summary':'New issue from jira-python in easy','description':'Look into this one', 'issuetype':'Task','components': [{'name':'Fourth_Component'}]})
post1 = requests.post(url, data=(payload_issues))
print post1.text


# import requests
# import json
# subtask = 'http://127.0.0.1:8000/subtask/'
# given = requests.post(subtask,data=({"project":{"key":"SSP"},"summary": "New Sub_Task For SSP","description": "New SSP Description","issuetype": "Sub-task","parent":{"key":"SSP-10"},"labels": ["Automatable","Automation"]}))
# print given.text

# # payload_subtask = {"project":"SW","summary": "From Postman Creating a Sub-task ","description": "Post Man Sub-task creating ","issuetype": "Sub-task","parent":'{"key" : "SW-1"}',"labels":["Automatable","Automated"]}
# # postttt = requests.post(subtask,data={"project":"SW","parent":'{"key" : "SW-1"}',"summary": "From Script Creating a Sub-task ","description": "Script Sub-task creating ","issuetype": "Sub-task","labels":["Automatable","Automated"]})
 
# postttt = requests.post(subtask,project="SW",parent=("key""SW-1"),summary="From Script Creating a Sub-task",description= "Script Sub-task creating ",issuetype="Sub-task",labels=["Automatable","Automated"]
# print postttt.text



# import requests
# import json
# sprint  = "http://127.0.0.1:8000/sprint/"
# demo = requests.post(sprint,data={"name":"My First Sprint from Script","board_id": "2"})
# print demo.text

