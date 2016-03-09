# install linux
FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get upgrade -y

# install postgres
RUN apt-get update && apt-get install -y \
	postgresql \
	postgresql-contrib \
	libpq-dev

# install python
RUN apt-get update && apt-get install -y \
	build-essential \
	python-dev \
	python-pip

# install requirements
RUN pip install \
	Django==1.9 \
	psycopg2==2.6.1

# run container
ENV TERM xterm-color
COPY start.sh /
CMD bash /start.sh