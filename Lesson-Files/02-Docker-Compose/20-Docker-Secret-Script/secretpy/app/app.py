#secretpy

import docker
import yaml
import random
import os
import secrets

client = docker.from_env()

with open(r'/home/ubuntu/environment/mtc-docker/Public/Lesson-Files/02-Docker-Compose/20-Docker-Secret-Script/docker-compose.yml') as file:
    secrets_list = yaml.load(file, Loader=yaml.FullLoader)


for i in secrets_list['secrets'].keys():
    try:
        secret = secrets.token_bytes(8)
        client.secrets.create(name=i,data=secret)
    except:
        pass
    

