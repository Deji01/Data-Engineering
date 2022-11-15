from kaggle_secrets import UserSecretsClient

user_secrets = UserSecretsClient()

db_host = user_secrets.get_secret("DB_HOST")
db_name = user_secrets.get_secret("DB_NAME")
db_password = user_secrets.get_secret("DB_PASSWORD")
db_port = user_secrets.get_secret("DB_PORT")
db_user = user_secrets.get_secret("DB_USER")
