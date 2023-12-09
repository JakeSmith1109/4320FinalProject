#use an officeial pyhton image
FROM python:3.8-slim-buster

#set the working directory in the container
WORKDIR /app

#copy tje contents from the current directory
COPY . /app/

#upgrade pip
RUN pip install --upgrade pip

#install any dependents
RUN pip install --no-cache-dir -r requirements.txt

#set the default commands
CMD ["python","app.py"]