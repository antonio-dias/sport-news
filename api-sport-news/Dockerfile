FROM khipu/openjdk17-alpine@sha256:d0345d07b837f214b934afa3dbb94f076530a22e03bd2db64aefee2743e1d6a2

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
