FROM mcr.microsoft.com/devcontainers/base:bullseye

COPY daemon.json /etc/docker/daemon.json

RUN apt-get update && \
    apt-get upgrade

RUN apt-get install -y \
    python3 python3-pip \
    libcairo2 python3-dev libffi-dev \
    gzip icnsutils

RUN pip3 install \
    cairosvg \
    pillow