FROM python:3.8

# ADD Book.py .

RUN pip install click
RUN pip install requests

WORKDIR /src  

COPY . .

CMD ["python", "./src/jokes.py"]


