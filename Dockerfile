from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip --ignore-installed -r requirements1.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]


