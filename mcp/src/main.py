from server import OpenstackMcpServer
from connection import OpenstackConnection
import argparse

#def build_server_from_args():
#    parser = argparse.ArgumentParser(description="Openstack MCP Server")
#    parser.add_argument("--url", type=str, required=True)
#    parser.add_argument("--credential", type=str, required=True)
#    parser.add_argument("--secret", type=str, required=True)
#    args = parser.parse_args()
#
#    return OpenstackMcpServer(
#        cloud_provider_url=args.url,
#        user_creds=args.credential,
#        user_pwd=args.secret
#    )
#
#
if __name__ == "__main__":
#    server = build_server_from_args()
    ocp = OpenstackMcpServer()
    ocp.run()

