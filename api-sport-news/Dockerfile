FROM khipu/openjdk17-alpine

RUN apk update && apk add netcat-openbsd

ENV PROFILE="default"

WORKDIR /api

COPY .mvn/ /api/.mvn
COPY mvnw /api/mvnw
COPY pom.xml /api/pom.xml
COPY src /api/src
COPY entrypoint.sh /opt/bin/entrypoint.sh

RUN sh -c '/api/mvnw clean package -Dspring-boot.run.profiles=$PROFILE'

EXPOSE 8081
