FROM python:3-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache gcc\
                       musl-dev\
                       libffi-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 2002

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]