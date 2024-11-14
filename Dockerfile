FROM spark:latest
RUN apt-get update && apt-get install -y iputils-ping
