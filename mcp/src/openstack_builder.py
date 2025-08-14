# openstack_builder.py

import openstack
import sys
from connection import OpenstackConnection

class OpenstackBuilder:
    def __init__(
        self,
        url: str,
        app_creds: str,
        app_secret: str,
        domain_name: str,
        log_path: str = "/home/igorkso/openstack-mcpserver.log"
    ):
        """
        Inicializa a conexão com a cloud OpenStack.

        Parâmetros:
            - url: endpoint do Keystone (ex: cloud6.lsd.ufcg.edu.br)
            - app_creds: application credential ID
            - app_secret: application credential secret
            - domain_name: domínio do usuário (ex: 'lsd')
            - log_path: caminho para salvar logs detalhados da SDK
        """
        # Habilita logging da SDK OpenStack
        openstack.enable_logging(debug=True, path=log_path, stream=sys.stdout)

        # Conexão
        self.connection = OpenstackConnection(
            host=url,
            app_creds=app_creds,
            app_secret=app_secret,
            domain_name=domain_name
        ).get_conn()

    def list_servers(self):
        """Retorna lista de servidores (instâncias)"""
        return list(self.connection.compute.servers())

    def list_images(self):
        """Retorna lista de imagens disponíveis"""
        return list(self.connection.compute.images())

    def list_flavors(self):
        """Retorna lista de flavors disponíveis"""
        return list(self.connection.compute.flavors())

