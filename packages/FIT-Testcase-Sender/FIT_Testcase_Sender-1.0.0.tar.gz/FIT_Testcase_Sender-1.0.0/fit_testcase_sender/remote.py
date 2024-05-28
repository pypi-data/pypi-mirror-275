import socket
import json

class FIT_Remote:
    def __init__(self, ip_address: str, port: int) -> None:
        self.ip_address = ip_address
        self.port = port
    
    # 시나리오 넘버를 리스트로 받아 TC 실행합니다.
    def excute_testcase(self, scenario_number: list) -> dict:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            scenario_number = {"ScenarioNo": scenario_number}
            sock.connect((self.ip_address, self.port))
            sock.sendall(json.dumps(scenario_number).encode('utf-8') + b'\n')
            return json.loads(sock.recv(1024).decode('utf-8'))       
    
    # TC 실행 결과가 Complete 인지 확인합니다.
    def is_testcase_complete(self, scenario_response: dict) -> bool:
        return scenario_response['Result'] == 'Complete'

