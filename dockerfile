FROM python:3.8-slim 

COPY . /app

RUN pip3 install flask
RUN pip3 install pymysql
RUN pip3 install flask_cors


WORKDIR /app

CMD ["python", "app.py"]