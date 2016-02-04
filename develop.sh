#!/bin/bash

# update requirements in Dockerfile
requirements='RUN pip install'
while read line || [[ -n $line ]]
do
  requirements=$requirements$' \\\\\\n\\t'$line
done < requirements.txt
sed -i -e '/RUN pip install \\/,/^$/c'"$requirements"'\n' ./containers/Dockerfile

# stop and remove container
sudo docker stop bmanners
sudo docker rm bmanners

# build image
sudo docker build -t bmanners ./containers

# run container
sudo docker run -it --rm \
	-v $PWD:/application \
	--name bmanners \
	-h bmanners \
	-p 80:8000 \
	bmanners