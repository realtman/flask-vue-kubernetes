FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
    libpq-dev \
    python3 \
    python3-pip \
    python3-dev \
    subversion

RUN svn co https://projects.coin-or.org/svn/Cbc/stable/2.9 Cbc-2.9 && \
    mkdir Cbc-2.9/build &&\
    cd Cbc-2.9/build && \
    ../configure --enable-cbc-parallel --prefix=/usr/local && \
    make && \
    make install

ENV LD_LIBRARY_PATH="/usr/local/lib:${LD_LIBRARY_PATH}"

COPY . /queue
WORKDIR /queue

RUN pip3 install -r requirements.txt

CMD ["celery", "-A", "tasks", "worker", "--loglevel=debug", "--logfile=/var/log/celery.log"]