# server.py

from fastmcp import FastMCP
from loguru import logger
from openstack_builder import OpenstackBuilder
from constant import OPENSTACK_MCP_SERVER_VERSION
import uuid
import sys


class OpenstackMcpServer:

    def __init__(self):
        self.mcp = FastMCP(name="CtrlStack", host="127.0.0.1", port=8888)
        self.sessions = {}  # Armazena conexões autenticadas por session_id

        # Setup de logging
        logger.remove()
        logger.add("DEBUG")
        logger.add(sys.stdout, level="INFO")
        logger.add("mcp-server.log", level="DEBUG")
        self.logger = logger

        self._register_tools()

    def _register_tools(self):
        @self.mcp.tool(description="Realiza login no OpenStack e retorna um session_id")
        def login(cloud_provider_url: str, app_creds: str, app_secret: str, domain_name: str):
            self.logger.debug("Tentando conexão com as credenciais fornecidas")
            try:
                builder = OpenstackBuilder(cloud_provider_url, app_creds, app_secret, domain_name)
                session_id = str(uuid.uuid4())
                self.sessions[session_id] = builder
                self.logger.info(f"Login bem-sucedido. Sessão criada: {session_id}")
                return {"session_id": session_id}
            except Exception as e:
                self.logger.error(f"Erro no login: {e}")
                return {"error": f"Erro no login: {str(e)}"}

        @self.mcp.tool(description="Lista todas as máquinas virtuais do projeto para um session_id")
        def list_servers(session_id: str):
            builder = self._get_builder(session_id)
            if isinstance(builder, str):
                return {"error": builder}
            try:
                return builder.list_servers()
            except Exception as e:
                self.logger.error(f"Erro ao listar servidores: {e}")
                return {"error": str(e)}

        @self.mcp.tool(description="Lista os flavors disponíveis para um session_id")
        def list_flavors(session_id: str):
            builder = self._get_builder(session_id)
            if isinstance(builder, str):
                return {"error": builder}
            try:
                flavors =  builder.list_flavors()        
                return [
            {
                "name": flavor.name,
                "vcpus": flavor.vcpus,
                "ram": flavor.ram,
                "disk": flavor.disk
            }

            for flavor in flavors
        ]
            except Exception as e:
                self.logger.error(f"Erro ao listar flavors: {e}")
                return {"error": str(e)}

        @self.mcp.tool(description="Lista as imagens disponíveis para um session_id")
        def list_images(session_id: str):
            builder = self._get_builder(session_id)
            if isinstance(builder, str):
                return {"error": builder}
            try:
                return builder.list_images()
            except Exception as e:
                self.logger.error(f"Erro ao listar imagens: {e}")
                return {"error": str(e)}

        @self.mcp.tool(description="Finaliza uma sessão existente (logout)")
        def logout(session_id: str):
            if session_id in self.sessions:
                del self.sessions[session_id]
                self.logger.info(f"Sessão finalizada: {session_id}")
                return {"success": f"Sessão {session_id} encerrada com sucesso"}
            else:
                return {"error": "Sessão não encontrada"}

    def _get_builder(self, session_id: str):
        if session_id not in self.sessions:
            self.logger.warning(f"Acesso negado para sessão inválida: {session_id}")
            return "Sessão inválida ou expirada"
        return self.sessions[session_id]

    def run(self):
        try:
            self.logger.info(f"Starting Openstack MCP Server v{OPENSTACK_MCP_SERVER_VERSION}")
            self.mcp.run(transport="sse")
        except Exception as e:
            self.logger.error(f"Falha ao iniciar MCP Server: {e}")
