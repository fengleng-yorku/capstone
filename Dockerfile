FROM python:3.11-slim

WORKDIR /app

# 复制所有文件
COPY . .

# 安装依赖
RUN pip install flask mysql-connector-python boto3 pymysql

# 下载 RDS SSL 证书
RUN apt-get update && apt-get install -y wget && \
    wget https://truststore.pki.rds.amazonaws.com/ca-central-1/ca-central-1-bundle.pem \
    -O /tmp/ca-central-1-bundle.pem

EXPOSE 5000

CMD ["python3", "Application.py"]