# Tunnel to Jupyter Notebook running on remote server e.g. AWS EC2
## Assumes notebook server is running on default settings e.g. --port=8888
ssh -i key.pem ec2-user@ec2-12-34-45-67.compute-1.amazonaws.com -D -L localhost:8888:localhost:8888
