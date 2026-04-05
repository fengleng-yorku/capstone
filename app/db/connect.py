import json
import configparser

import boto3
import mysql.connector


class MariaDBConnect:

    def createConnection(self):
        # Fetch credentials from AWS Secrets Manager
        client = boto3.client("secretsmanager", region_name="ca-central-1")
        secret = client.get_secret_value(
            SecretId="rds!db-6241b0fb-377d-475b-80f9-2bcdb7f55ff0"
        )
        creds = json.loads(secret["SecretString"])

        # Read non-secret config from file
        config = configparser.ConfigParser()
        config.read('./config/connection.ini')

        port = config.getint('Database', 'port')
        database = config.get('Database', 'database')

        try:
            conn = mysql.connector.connect(
                host="capstone-db.cteiqwqowf2a.ca-central-1.rds.amazonaws.com",
                port=port,
                user=creds["username"],
                password=creds["password"],
                database=database,
                ssl_ca="/tmp/ca-central-1-bundle.pem",
                ssl_verify_cert=True,
            )
            if conn.is_connected():
                print("Connected to MariaDB on remote server")
        except mysql.connector.Error as e:
            print(f"Error connecting to MariaDB: {e}")

        return conn
