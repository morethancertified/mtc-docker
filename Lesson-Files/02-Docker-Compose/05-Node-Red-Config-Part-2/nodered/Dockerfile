FROM nodered/node-red

COPY ./flows.json /data/flows.json

#WORKDIR /data

ENV API_URL="172.21.0.2"

#RUN sed -i "s/API_IP:API_PORT/${API_IP}:${API_PORT}/g" /data/flows.json 

