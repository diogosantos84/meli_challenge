FROM python:3

RUN pip install pymongo

WORKDIR /app

COPY files/ /app/

#CMD python3 /app/app.py

ENTRYPOINT ["python3"]
CMD ["rest-api.py"]