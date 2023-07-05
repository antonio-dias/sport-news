#!/bin/sh

while ! nc -z container-mongodb 27017 ; do
	echo "##########################################"
	echo "###### Aguardando container-mongodb ######"
	echo "##########################################"
	sleep 30
done

java -jar -Dspring.profiles.active=${PROFILE} target/api-sport-news.jar