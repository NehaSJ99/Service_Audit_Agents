from crewai import Crew, Agent, Task
import yaml
import os
from tools.custom_tool import csv_tool

def load_yaml_config(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

# Load agent and task configs
agents_config = load_yaml_config("config/agents.yaml")
tasks_config = load_yaml_config("config/tasks.yaml")

# Load agents from YAML
suggestion_cfg = agents_config['suggestion_generation_agent']
reporting_cfg = agents_config['reporting_agent']
chart_cfg = agents_config['chart_generation_agent']

suggestion_generation_agent = Agent(
    role=suggestion_cfg['role'],
    goal=suggestion_cfg['goal'],
    backstory=suggestion_cfg['backstory'],
    allow_delegation=suggestion_cfg.get('allow_delegation', True),
    verbose=suggestion_cfg.get('verbose', False)
)

reporting_agent = Agent(
    role=reporting_cfg['role'],
    goal=reporting_cfg['goal'],
    backstory=reporting_cfg['backstory'],
    allow_delegation=reporting_cfg.get('allow_delegation', True),
    verbose=reporting_cfg.get('verbose', False)
)

chart_generation_agent = Agent(
    role=chart_cfg['role'],
    goal=chart_cfg['goal'],
    backstory=chart_cfg['backstory'],
    allow_delegation=chart_cfg.get('allow_delegation', True),
    verbose=chart_cfg.get('verbose', False),
    allow_code_execution=False
)


# Create Tasks
# Unpack all tasks from YAML
suggestion_cfg = tasks_config['suggestion_generation']
table_cfg = tasks_config['table_generation']
chart_cfg = tasks_config['chart_generation']
final_cfg = tasks_config['final_report_assembly']

suggestion_generation = Task(
    description=suggestion_cfg['description'],
    expected_output=suggestion_cfg['expected_output'],
    agent=suggestion_generation_agent,
    tools=[csv_tool]
)

table_generation = Task(
    description=table_cfg['description'],
    expected_output=table_cfg['expected_output'],
    agent=reporting_agent,
    tools=[csv_tool]
)

chart_generation = Task(
    description=chart_cfg['description'],
    expected_output=chart_cfg['expected_output'],
    agent=chart_generation_agent,
)

final_report_assembly = Task(
    description=final_cfg['description'],
    expected_output=final_cfg['expected_output'],
    agent=reporting_agent,
    context=[
        suggestion_generation,
        table_generation,
        chart_generation
    ]
)


# Create Crew
def build_crew():
    support_report_crew = Crew(
        agents=[
            suggestion_generation_agent,
            reporting_agent,
            chart_generation_agent
        ],
        tasks=[
            suggestion_generation,
            table_generation,
            chart_generation,
            final_report_assembly
        ],
        verbose=True,
        memory=True
    )
    return support_report_crew