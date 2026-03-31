FROM debian:stable-slim
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -qyf \
    curl jq make git \
    python3-pygments gnuplot \
    texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended \
    texlive-xetex texlive-lang-chinese texlive-fonts-extra \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]
