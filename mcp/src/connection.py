# connection.py

from openstack import connection
from openstack import connect
from keystoneauth1.identity import v3
import urllib.parse


class OpenstackConnection:
    def __init__(
        self,
        host: str,                     # Ex: "cloud6.lsd.ufcg.edu.br"
        app_creds: str,
        app_secret: str,
        domain_name: str,
        use_tls: bool = True,
        use_file: bool = False
    ):
        # Monta URL corretamente
        self.protocol = "https" if use_tls else "http"
        self.base_url = f"{self.protocol}://{host}:5000/v3"  # ← ajustado para garantir /v3

        self.identity = app_creds
        self.secrets = app_secret
        self.domain = domain_name
        self.conn = None

        if use_file:
            self.conn = self.establish_connection_from_file()
        else:
            self.conn = self.establish_connection_from_args()

    def get_conn(self, use_file: bool = False):
        if use_file:
            return self.establish_connection_from_file()
        return self.establish_connection_from_args()

    def establish_connection_from_file(self):
        conn = connection.from_config()
        self.check_connection(conn)
        return conn

    def establish_connection_from_args(self):
        self.conn = connect(
            auth_url=self.base_url,
            application_credential_id=self.identity,
            application_credential_secret=self.secrets,
            user_domain_name=self.domain,
            auth_type="v3applicationcredential"
        )
        self.check_connection(self.conn)
        return self.conn

    def check_connection(self, conn):
        try:
            # Simples tentativa de listar usuários para verificar login
            conn.identity.users()
            return True
        except Exception as e:
            raise ConnectionError("Failed to establish connection with OpenStack") from e

