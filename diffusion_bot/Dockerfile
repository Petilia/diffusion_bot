FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y  \
    git wget sudo build-essential \
    python3 python3-setuptools python3-pip python3-dev python3-tk \
    ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6

RUN ln -svf /usr/bin/python3 /usr/bin/python
RUN python -m pip install --upgrade --force pip

COPY requirements.txt . 
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y telnet
RUN pip install python-dotenv

#### ADD USER WITH DEFAULT PW
ARG USER=docker_current
ARG UID=1000
ARG GID=1000
ARG PW=user

RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PW}" | chpasswd && adduser ${USER} sudo
WORKDIR /home/${USER}
COPY . . 
RUN chown -R ${UID}:${GID} /home/${USER}
USER ${UID}:${GID}