FROM --platform=linux/amd64 python:slim-bullseye 
# FROM  python:3.10-slim

WORKDIR /app
  
# commons start 
RUN apt-get update \
    && apt-get install -y libpq-dev gcc openssl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip 

COPY commons commons 
RUN  pip install --no-cache-dir -r commons/requirements.txt
COPY commons/start-reload.sh start-reload.sh
RUN chmod +x ./start-reload.sh 
# commons end 


# app requirements


COPY rag_app/app/requirements.txt app/requirements.txt 

RUN  pip install --no-cache-dir -r app/requirements.txt
# app requirements
 

COPY rag_app/app app

ENTRYPOINT ["sh", "./start-reload.sh"]