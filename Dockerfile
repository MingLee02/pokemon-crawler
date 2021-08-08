FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git ssh python3-pip python3-dev ffmpeg python3-tk libpq-dev
RUN mkdir -p /opt/app
WORKDIR /opt/app
ADD ./ /opt/app
RUN mkdir -p /opt/app/staticfiles
RUN pip3 install -r ./requirements.txt
# Set the locale
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/docker-entrypoint.sh"]