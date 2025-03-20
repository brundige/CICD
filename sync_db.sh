#!/bin/bash

# Define the URIs
DEV_URI="mongodb://localhost:27017/testdb"
STAGING_URI="mongodb://localhost:27017/stagingdb"
BACKUP_PATH="/path/to/backup"

# Dump the development database
mongodump --uri="$DEV_URI" --out="$BACKUP_PATH"

# Restore to the staging database
mongorestore --uri="$STAGING_URI" "$BACKUP_PATH/testdb"