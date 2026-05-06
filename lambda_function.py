import json
import urllib.parse

def lambda_handler(event, context):
    # Pega o nome do bucket e do arquivo do evento
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    print(f"Arquivo detectado: {key} no bucket: {bucket}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Automação executada com sucesso!')
    }