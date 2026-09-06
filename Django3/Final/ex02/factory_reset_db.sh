#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

DB_NAME="djangotraining"
DB_USER="djangouser"

echo "=== WARNING: Wiping out database '$DB_NAME' ==="

# Terminate active connections and drop/recreate database using postgres superuser
sudo -u postgres psql <<EOF
-- Terminate open connections to prevent 'database is being accessed by other users' error
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = '$DB_NAME'
  AND pid <> pg_backend_pid();

-- Drop and recreate database
DROP DATABASE IF EXISTS $DB_NAME;
CREATE DATABASE $DB_NAME OWNER$DB_USER;
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO$DB_USER;
EOF

# Restore schema permissions
sudo -u postgres psql -d "$DB_NAME" <<EOF
GRANT ALL ON SCHEMA public TO $DB_USER;
ALTER SCHEMA public OWNER TO $DB_USER;
EOF

echo "=== Running Django Migrations from scratch ==="

if [ -f "manage.py" ]; then
    python manage.py migrate
else
    echo "Warning: manage.py not found. Skipping migrations."
fi

echo "=== Factory Reset Complete ==="
