FROM python:3

RUN pip install flask flask_restful flask_pymongo pymongo

WORKDIR /app
COPY rest-api.py /app
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["rest-api.py"]