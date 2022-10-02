## PlayList API local environment setup

## Setting up pipenv
1. confirm your pipenv install (by running 'pipenv'), or install it if you don't have it
2. activate virtual environment with '''pipenv shell'''
3. install all the required packages with '''pipenv install''' 
4. you can run the service with inside the virtual environment with '''pipenv run main.py'''   

## Setting postgres database
1. you need postgre database to support this API service
2. Update .env to match your database setting
3. Update alembic.ini for your database migration  