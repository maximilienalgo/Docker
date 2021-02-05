FROM alpine

EXPOSE 4000:8080

RUN apk add --update-cache \
    python3 \
    py3-pip \
    vim \
    && rm -rf /var/cache/apk/*

COPY requirements.txt /app/
RUN pip install --requirement /app/requirements.txt
COPY . /app/

CMD ["/app/app_test.py"]
CMD python /app/app_test.py
ENTRYPOINT ["python3"]
