import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'kabreaziz60'
PASSWORD = 'Ouedraogo@6000'
DATABASE = 'Holliwode'
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password= PASSWORD, dbname = DATABASE)
