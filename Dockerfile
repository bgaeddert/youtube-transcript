# use python:3
FROM python:3

# set working directory
WORKDIR /usr/src/app

# copy requirements.txt
COPY requirements.txt ./

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# run app
CMD [ "python", "./app.py" ]