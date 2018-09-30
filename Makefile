install:
	pip3 install -r requirements.txt

docker:
	docker build -t ipme .
