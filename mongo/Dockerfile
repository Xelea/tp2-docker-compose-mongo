FROM mongodb/mongodb-community-server:8.0-ubi8-slim

USER root

RUN chown -R 184:0 /data/db && chmod -R g+w /data/db


COPY blog-db.js /docker-entrypoint-initdb.d/

USER 184