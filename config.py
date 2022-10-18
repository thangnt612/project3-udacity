import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="udacity-3.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="thangadmin" #TODO: Update value
    POSTGRES_PW="aA@32967083"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'zqCxSNJawcAmfmcd/67C0Ewl6/YDaSMO1jCjiLXV4iY='
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://notification003.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=lJkAym5tEZf4WyCfe73DeKLPrf/wEiYtKYrRx9pk9oE=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='myqueue'
    ADMIN_EMAIL_ADDRESS = 'thangnt612@gmail.com'
    SENDGRID_API_KEY = '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' 

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False