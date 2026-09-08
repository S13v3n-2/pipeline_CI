docker build -t test-python:v2 .
docker run --rm test-python:v2 ls -la
docker run --rm test-python:v2 python3 app.py

docker run -d --name mysql-ephemere -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 mysql:5.7
docker exec -it mysql-ephemere mysql -u root -psecret

CREATE DATABASE test;
USE test;
CREATE TABLE customer (id INT, name VARCHAR(10));
EXIT;

docker rm -f mysql-ephemere

docker run -d --name mysql-ephemere-2 -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 mysql:5.7
docker exec -it mysql-ephemere-2 mysql -u root -psecret -e "SHOW DATABASES;"

docker run -d --name mysql-persistant -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 mysql:5.7
docker volume ls

docker exec -it mysql-persistant mysql -u root -p secret
CREATE DATABASE test;
USE test;
CREATE TABLE customer (id INT, name VARCHAR(10));
Exit;

docker rm -f mysql-persistant
docker run -d --name mysql-persistant-2 -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=secret -p 3306:3306 mysql:5.7
docker exec -it mysql-persistant-2 mysql -u root -psecret -e "SHOW DATABASES;"

Le volume était persistant, donc quand on remonte le conteneurs, on vois bien la databases creer.
