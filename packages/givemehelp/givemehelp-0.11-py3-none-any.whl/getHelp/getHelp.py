import sys
import json
import boto3
from getMessage import run_program

def gettingHelp():
    print("Wanna try get help")
    
def retreiveSecretKey():
    if len(sys.argv) != 3:
        print("Command to use: getHelp <path_to_program> <interpreter>")
    else:
        lambda_client = boto3.client('lambda', region_name='eu-west-2')
        function_name = 'secret-key-retrieval'
        payload = {'key': 'value'}
        response = lambda_client.invoke(
                FunctionName=function_name,
                InvocationType='RequestResponse',
                Payload=json.dumps(payload)
            )

        response_payload = response['Payload'].read().decode('utf-8')
        secretjson = json.loads(response_payload)
        secretjson = json.loads(secretjson)
        secret = secretjson["open AI API secret key"]
        run_program(sys.argv[1], sys.argv[2],secret)
