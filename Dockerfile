FROM python:bullseye

#dnsmasq
RUN apt update
RUN apt install dnsmasq dnsutils inotify-tools -y

#django part
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY lab /app/lab
COPY sslhomelab /app/sslhomelab
COPY manage.py /app/manage.py

COPY runserver.sh /app/runserver.sh
RUN chmod +x /app/runserver.sh

RUN python /app/manage.py migrate

EXPOSE 81 53

CMD ["/app/runserver.sh"]