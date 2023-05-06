#!/bin/bash

python /app/manage.py runserver 0.0.0.0:81 &

dnsmasq

while true;
do
    inotifywait --event modify /etc/dnsmasq.conf && kill $(pidof dnsmasq) && dnsmasq
done