FROM redis:alpine
COPY ./docker/redis/sysctl.conf /etc/sysctl.conf
CMD redis-server --appendonly yes
