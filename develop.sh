#!/bin/bash

# update requirements in Dockerfile
requirements='RUN pip install'
while read line || [[ -n $line ]]
do
  requirements=$requirements$' \\\\\\n\\t'$line
done < requirements.txt
sed -i -e '/RUN pip install \\/,/^$/c'"$requirements"'\n' ./containers/Dockerfile

# stop and remove container
docker stop boringmanclan
docker rm boringmanclan

# build image
docker build -t boringmanclan ./containers

# run container
docker run -it --rm \
	-v $PWD:/application \
	--name boringmanclan \
	-h boringmanclan \
	-p 80:8000 \
	boringmanclan
