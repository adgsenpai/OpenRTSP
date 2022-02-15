FROM python:3.10.2
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" , "server.py" ]
