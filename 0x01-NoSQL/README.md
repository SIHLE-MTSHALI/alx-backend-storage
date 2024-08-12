# 0x01. NoSQL

This project focuses on working with NoSQL databases, specifically MongoDB. It covers various operations such as querying, inserting, updating, and deleting documents using both MongoDB shell commands and Python with PyMongo.

## Requirements

- MongoDB 4.2
- Python 3.7
- PyMongo 3.10

## Installation

1. Install MongoDB 4.2:
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org

2. Install PyMongo:
pip3 install pymongo

## Files

- `0-list_databases`: Lists all databases in MongoDB
- `1-use_or_create_database`: Creates or uses a database
- `2-insert`: Inserts a document in a collection
- `3-all`: Lists all documents in a collection
- `4-match`: Lists all documents with a specific name in a collection
- `5-count`: Displays the number of documents in a collection
- `6-update`: Adds a new attribute to a document
- `7-delete`: Deletes all documents with a specific name
- `8-all.py`: Python function to list all documents in a collection
- `9-insert_school.py`: Python function to insert a new document in a collection
- `10-update_topics.py`: Python function to change all topics of a school document
- `11-schools_by_topic.py`: Python function to return the list of schools having a specific topic
- `12-log_stats.py`: Python script to provide stats about Nginx logs stored in MongoDB

## Advanced Tasks

- `100-find`: Lists all documents with name starting by Holberton in the collection school
- `101-students.py`: Python function that returns all students sorted by average score
- `102-log_stats.py`: Improved version of 12-log_stats.py with top 10 most present IPs
