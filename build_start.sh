#!/usr/bin/env bash

cd build_migrator
make build
cd ../deploy_migrator
docker-compose stop && docker-compose up