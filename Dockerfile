FROM python:3.7-alpine

COPY bots/twitter-api-bot.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "twitter-api-bot.py"]