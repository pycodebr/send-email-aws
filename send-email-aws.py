import boto3

# Cria o serviço com as suas credenciais da AWS #
ses = boto3.client(
    service_name='ses',
    region_name='***REGIÃO DO SEU BUCKET***', 
    aws_access_key_id='***SUA ACCESS_KEY***', 
    aws_secret_access_key='***SUA SECRET_KEY***'
)

# Envia o email através do serviço SES da AWS #
ses.send_email(
    Destination={
        'ToAddresses': [
            '***EMAIL QUE VAI RECEBER***', # Email que vai receber
        ],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'utf-8',
                'Data': 'Olá Pycodebr!', # Texto do Email
            },
        },
        'Subject': {
            'Charset': 'utf-8',
            'Data': 'Enviando email pela AWS', # Assunto do Email
        },
    },
    Source='***SEU EMAIL PARA ENVIO***' # Email que vai fazer o envio
)



