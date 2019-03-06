lambda.docker.build:
	@echo "---- Create amazon linux image base ----"
	@docker build -t amazon-linux-python36 .

lambda.docker.pkgcreate:
	@echo "---- Create Lambda Package using amazon linux image base ----"
	@docker run --rm -u `id -u` \
		-v ~/.aws/:/home/lambda/.aws/ \
		-v `pwd`:/app \
		-e "HOME=/home/lambda" \
		amazon-linux-python36 pip3.6 install -r requirements.txt -t .

deploy:
	# Rodar migração do Postgres de prod
	flask db migrate
	flask db upgrade
	# Rodar o zappa
	zappa deploy dev

run.local:
	docker-compose up -d

test:
	docker-compose exec flask python -m unittest app