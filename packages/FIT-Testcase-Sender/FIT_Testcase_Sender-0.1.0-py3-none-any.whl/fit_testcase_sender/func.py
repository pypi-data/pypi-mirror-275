import socket
import json

class FIT_Remote:
    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
    
    def excute_testcase(self, scenario_number: list) -> dict:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.ip_address, self.port))
            sock.sendall(json.dumps(scenario_number).encode('utf-8') + b'\n')
            return json.loads(sock.recv(1024).decode('utf-8'))       
    
    def is_testcase_result(scenario_response: dict) -> bool:
        return scenario_response['Result'] == 'Complete'

