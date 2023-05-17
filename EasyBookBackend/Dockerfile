FROM python:3.8-bullseye
WORKDIR /data
COPY my-app/requirements.txt /data
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY my-app/ /data
EXPOSE 8001