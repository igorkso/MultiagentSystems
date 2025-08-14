from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import MCPServerAdapter

@CrewBase
class CrewStack():

    agents_config = "config/agents.yaml"
    tasks_config  = "config/tasks.yaml"

    mcp_server_params = {
        "url": "http://localhost:8888/sse",
        "transport": "sse"
    }

    def get_mcp_tools(self):
        return MCPServerAdapter.from_url(**self.mcp_server_params).tools()

    # Agentes
    @agent
    def UserInterface(self) -> Agent:
        return Agent(
            config=self.agents_config["UserInterface"],
            verbose=True,
            tools=self.get_mcp_tools()
        )

    @agent
    def Validator(self) -> Agent:
        return Agent(
            config=self.agents_config["Validator"],
            verbose=True,
            tools=self.get_mcp_tools()
        )

    @agent
    def Deployment(self) -> Agent:
        return Agent(
            config=self.agents_config["Deployment"],
            verbose=True,
            tools=self.get_mcp_tools()
        )

    @agent
    def Teste(self) -> Agent:
        return Agent(
            config=self.agents_config["Teste"],
            verbose=True,
            tools=self.get_mcp_tools()
        )

    # Tasks carregadas do YAML
    @task
    def start_conversation(self) -> Task:
        return Task(config=self.tasks_config["start_conversation"])

    @task
    def login_to_cloud(self) -> Task:
        return Task(config=self.tasks_config["login_to_cloud"])

    @task
    def list_flavors(self) -> Task:
        return Task(config=self.tasks_config["list_flavors"])

    @task
    def formatar_flavors_para_usuario(self) -> Task:
        return Task(config=self.tasks_config["formatar_flavors_para_usuario"])


    # Execução principal da crew
    @crew
    def start_team(self) -> Crew:
        return Crew(
            agents=[
                self.UserInterface(),
                self.Validator(),
                self.Deployment()
            ],
            tasks=[
                self.login_to_cloud(),
                self.list_flavors(),
                self.formatar_flavors_para_usuario()
            ],
            process=Process.sequential
        )

