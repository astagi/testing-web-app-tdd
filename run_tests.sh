#!/bin/bash

gulp build
pytest --cov . --cov-report term-missing --driver Chrome
yarn test
