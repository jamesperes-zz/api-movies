lambda.docker.build:
	@echo "---- Create amazon linux image base ----"
	@docker build -t amazon-linux-python36 .

deploy:
	@docker run --rm \
		-v ~/.aws/:/home/lambda/.aws/ \
		-v `pwd`:/app \
		-e "HOME=/home/lambda" \
		-e "LC_ALL=en_US.UTF-8" \
		-e "FLASK_APP=run" \
		-e "APP_DATABASE_URL=postgresql://telecine:telecine123@telecine.csjpxownrgww.eu-west-1.rds.amazonaws.com:5432/telecine" \
		amazon-linux-python36 /bin/bash -c "pip install -r requirements.txt && flask db upgrade && flask db migrate && zappa deploy dev"

run.local:
	docker-compose up -d 

test:
	docker-compose exec flask python -m unittest app