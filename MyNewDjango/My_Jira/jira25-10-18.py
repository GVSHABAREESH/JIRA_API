from jira.client import JIRA
from jira.client import GreenHopper
from jira.resources import GreenHopperResource
import time


class JIRAWrapper(object):
	def __init__(self):
		self.jira = self.__authenticate()



	def __authenticate(self):
		options = {'server': 'https://gelivimanindl.atlassian.net'}
		jira = JIRA(options, basic_auth=('gmani9052@gmail.com', '9494123456a!'))
		return jira




	def get_all_projects(self):
		projects = self.jira.projects()
		print projects
		for project in projects:
			print "id    - ", project.id
			print "Key   - ", project.key
			print "Name  - ", project.name
			print "------------------"		
		print 'List of the projects in JIRA----'




	def creating_project(self):

		project = self.jira.create_project(name='BaleBale',key='BB', template_name='com.pyxis.greenhopper.jira:gh-scrum-template')
		print "project is created"

	def Creating_Component(self):
		component_jira = self.jira.create_component(project='BB',name= "Second_Component",description="This is a JIRA component",assigneeType= "PROJECT_LEAD",leadUserName= "Gelivi Mani",isAssigneeTypeValid=True)
    	print 'Component Created----'




	def create_a_issue_in_scrum_in_backlog(self):
		Scrum_issue = {
			"project": {"key": "BB"},
			"summary": "New Scrum 1 ---- ",
			"description": "New Scrum Description 1 ----",
			"issuetype": {"name": "Task"},
			"components"= [{"name":"Second_Component"}],
		}
		new_issue = self.jira.create_issue(fields=Scrum_issue)
		print 'Scrum_issue Created----'




	def creating_an_issue_in_easy_way(self):
		new_issue = self.jira.create_issue(project='BB',summary='New issue from jira-python in easy',description='Look into this one', issuetype={'name': 'Bug'},components= [{"name":"First_Component"},{"name":"Second_Component"}])
		print 'Issue is created in Easy way from api-----'





	def create_a_issue_in_scrum1_in_backlog(self):
		Scrum_issue = {
			"project": {"key": "MFJP"},
			"summary": "New Issue Created from api 2---- ",
			"description": "New Description Created from api 2----",
			"issuetype": {"name": "Story"},

		}
		new_issue = self.jira.create_issue(fields=Scrum_issue)
		print 'new issue is created'

		comment = self.jira.add_comment(issue='MFJP-15',body='added my first comment from api',visibility=None)
		print 'Comment Added----'




	def creating_an_issue_Bug(self):
		First_Bug = {
			"components": [{"name":"Verify_admin"}],
			"project": {"key": "STP"},
			"summary": "verify_login_credentials ",
			"description": "New Bug Description 1 ----",
			"issuetype": {"name": "Task"},	
			}
		new_issue = self.jira.create_issue(fields=First_Bug)
		print 'Task Created----'
		


	

	def creating_an_issue_Task(self):
		First_Task = {
			"project": {"key": "MSP"},
			"summary": "New Task 1 ---- ",
			"description": "New Task Description 1 ----",
			"issuetype": {"name": "Story"},
			"Sprint":{""}
		}
		new_issue = self.jira.create_issue(fields=First_Task)
		print 'Task Created----'

	
	


	def creating_an_sub_task(self):  #we can create for both scrum and bug tracking
		
		Sub_task = {
		    "project":{"key":"STP"},
		    "summary": "New Sub_Task For MNP-----",
		    "description": "New MNP Description",
		    "issuetype": "Sub-task",
	   	    "parent" : { "key" : "STP-5"}	   	    
		}
		new_issue = self.jira.create_issue(fields=Sub_task)
		print " Sub_Task Has Been Created-----"




	def creating_multiple_tasks(self):
		issue_list = [
		{
		    'project': {'id': 10019},
		    'summary': 'First issue of many',
		    'description': 'Look into this one',
		    'issuetype': {'name': 'Story'},
		},
		{
		    'project': {'key': 'MSP'},
		    'summary': 'Second issue',
		    'description': 'Second one',
		    'issuetype': {'name': 'Bug'},
		},
		{
		    'project': {'key': 'MSP'},
		    'summary': 'Third issue',
		    'description': 'Third one',
		    'issuetype': {'name': 'Task'},
		},
		]
		issues = self.jira.create_issues(field_list=issue_list)
		print 'Multiple tasks have been Created----'




	def create_sprint1(self):
		Sprint = self.jira.create_sprint(name='sruthi', board_id=2, startDate=None, endDate=None)
		print 'Sprint is Created---'





	def updating_a_sprint(self):
		update_sprint = self.jira.update_sprint(id=10, name='MFJP', startDate=None, endDate=None)
		print 'Sprint is Updated---'




	def boards(self):
		board=self.jira.boards()
		print board

		


	def deleting_board(self):
		deleting = self.jira.delete_board(id=11)
		print 'Board Was deleted----'





	def deleting_project(self):
		deleting = self.jira.delete_project(pid=10023)
		print 'Project Was deleted----'




	def adding_comment(self):
		comment = self.jira.add_comment(issue='SSP-2',body='adding my first comment',visibility=None)
		print 'comment is added----'





	def get_subtask_data_and_updating_and_adding_comment_and_component(self):
		data = self.jira.issue(10028)
		print data
		data.update(summary='New Summary For 10160_id', description='New Summary Was Added 10160_id')
		comment = self.jira.add_comment(issue='MNB-12',body='adding my first comment',visibility=None)
		component = self.jira.create_component(name = 'GV Shabareesh', project='MNB', description='Matter Created from Api',leadUserName='G V Shabareesh')
		print 'Subtask or Task and adding_comment and adding_component [Summary and Description and comment]-----'
		print 'updated from api---'




	def simple_issue(self):
		i = self.jira.search_issues('issuetype=Bug')
		print i




	def get_all_sub_tasks(self):
		sub_task = self.jira.search_issues('issuetype=Bug')
		print sub_task




	def get_testcases_from_suite(self):
		project_issues=self.jira.search_issues('issuetype=Bug')
		# print project_issues
		testcases_list=[]
		for issue in project_issues:
			if len(issue.fields.subtasks)>0:
				testcases_list.append(issue.fields.subtasks)
        	print testcases_list



	def get_project_components(self):
		projectComponents=self.jira.project_components('SW')
		print projectComponents




	def get_sprints(self):
		sprints_list = self.jira.sprints(board_id=2)
		print sprints_list




	def get_issues_from_sprint(self):
		sprintlist=self.jira.search_issues('issuetype=Story')
		sprint_info =[]
		for each in sprintlist:
			sprint_info.append({'sprintid':each.id,'Story_key':each.key})
		print sprint_info



	def moving_issues_to_backlog(self):
		import pdb; pdb.set_trace()
		s_issues = self.jira.move_to_backlog(issue_keys="SSP-24")
		print s_issues



	def adding_issues_to_sprint(self):
		a_issues = self.jira.add_issues_to_sprint(sprint_id=10,issue_keys='SSP-25')
		print 'Response'






	# def get_project(self):
	# 	pro = self.jira.projects()
	# 	print pro
	# 	for each in pro:
	# 		print 'name  - ',each.name
	# 		print 'key   - ',each.key
	# 		print "id    - ",each.id
	# 		print '---'*10





# JIRAWrapper().get_all_projects()
# JIRAWrapper().creating_project()
# JIRAWrapper().create_a_issue_in_scrum()
JIRAWrapper().creating_an_issue_in_easy_way()
# JIRAWrapper().create_a_issue_in_scrum1_in_backlog()
# JIRAWrapper().creating_an_issue_Bug()
# JIRAWrapper().creating_an_issue_Task()
# JIRAWrapper().creating_an_sub_task()
# JIRAWrapper().creating_multiple_tasks()
# JIRAWrapper().create_sprint1()
# JIRAWrapper().create_sprint2()
# JIRAWrapper().updating_a_sprint()
# JIRAWrapper().boards()
# JIRAWrapper().creating_component()	
# JIRAWrapper().deleting_board()
# JIRAWrapper().deleting_project()
# JIRAWrapper().adding_comment()
# JIRAWrapper().get_subtask_data_and_updating_and_adding_comment_and_component()
# JIRAWrapper().simple_issue()
# JIRAWrapper().get_all_sub_tasks()
# JIRAWrapper().get_testcases_from_suite()
# JIRAWrapper().get_project_components()
# JIRAWrapper().get_sprints()
# JIRAWrapper().get_issues_from_sprint()
# JIRAWrapper().Creating_Component()
# JIRAWrapper().moving_issues_to_backlog()
# JIRAWrapper().adding_issues_to_sprint()
# JIRAWrapper().get_project()
