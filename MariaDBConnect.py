import mysql.connector
import configparser
import boto3
import json

class MariaDBConnect:

    def createConnection(self):
        # 从 Secrets Manager 获取真实凭证
        client = boto3.client("secretsmanager", region_name="ca-central-1")
        secret = client.get_secret_value(
            SecretId="rds!db-6241b0fb-377d-475b-80f9-2bcdb7f55ff0"
        )
        creds = json.loads(secret["SecretString"])

        # 读取 ini 文件（只取 database 名和 port）
        config = configparser.ConfigParser()
        config.read('./connection.ini')

        port = config.getint('Database', 'port')
        database = config.get('Database', 'database')

        # 创建带 SSL 的连接
        try:
            conn = mysql.connector.connect(
                host="capstone-db.cteiqwqowf2a.ca-central-1.rds.amazonaws.com",
                port=port,
                user=creds["username"],
                password=creds["password"],
                database=database,
                ssl_ca="/tmp/ca-central-1-bundle.pem",
                ssl_verify_cert=True
            )

            if conn.is_connected():
                print("Connected to MariaDB on remote server")

        except mysql.connector.Error as e:
            print(f"Error connecting to MariaDB: {e}")

        return conn