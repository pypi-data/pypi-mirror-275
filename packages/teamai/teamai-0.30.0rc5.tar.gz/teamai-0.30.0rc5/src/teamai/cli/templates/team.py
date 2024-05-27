from teamai import Agent, Process, Task, Team
from teamai.project import TeamBase, agent, task, team

# Uncomment the following line to use an example of a custom tool
# from {{folder_name}}.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from teamai_tools import SerperDevTool

@TeamBase
class {{team_name}}Team():
	"""{{team_name}} team"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher()
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.reporting_analyst(),
			output_file='report.md'
		)

	@team
	def team(self) -> Team:
		"""Creates the {{team_name}} team"""
		return Team(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.teamai.dev/how-to/Hierarchical/
		)
