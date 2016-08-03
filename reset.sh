#!/bin/bash
# This script is a convenience affording one-command brain erasure.
set -xe
docker-compose stop
docker-compose rm -f --all
docker-compose up -d
sleep 7
docker-compose exec database createdb -h localhost -U postgres timewebsite
docker-compose exec webapp python db_create.py
docker-compose exec webapp python test_data.py
