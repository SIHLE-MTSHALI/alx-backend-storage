# 0x02. Redis Basic

This project focuses on using Redis for basic operations and as a simple cache. It includes implementations of various Redis functionalities using Python.

## Files:
- `exercise.py`: Contains the main Cache class and related methods
- `web.py`: Implements an expiring web cache and tracker
- `main.py`: Test files for each task

## Requirements:
- Ubuntu 18.04 LTS
- Python 3.7
- Redis server
- `redis` Python client

## Setup:
1. Install Redis:

sudo apt-get -y install redis-server
Copy2. Install Redis Python client:
pip3 install redis
Copy3. Configure Redis to accept connections from localhost:
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
