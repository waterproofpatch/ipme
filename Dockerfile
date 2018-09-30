from python

ADD . ipme
RUN pip install -r ipme/requirements.txt

CMD ["python", "ipme/ipme/main.py"]

