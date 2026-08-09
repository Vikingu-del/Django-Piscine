#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

# Configuration variables (matching settings.py)
DB_NAME="djangotraining"
DB_USER="djangouser"
DB_PASS="secret"

echo "=== Setting up PostgreSQL Database and User ==="

# Execute SQL commands using the default 'postgres' superuser
sudo -u postgres psql <<EOF
-- Create user if it does not exist
DO \$$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = '$DB_USER') THEN
        CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
    ELSE
        ALTER USER $DB_USER WITH PASSWORD '$DB_PASS';
    END IF;
END
\$$;

-- Create database if it does not exist
SELECT 'CREATE DATABASE $DB_NAME OWNER $DB_USER'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$DB_NAME')\gexec

-- Grant privileges on database
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

echo "=== Ensuring public schema permissions ==="

# Grant permissions on the public schema (required for newer PostgreSQL versions)
sudo -u postgres psql -d "$DB_NAME" <<EOF
GRANT ALL ON SCHEMA public TO $DB_USER;
ALTER SCHEMA public OWNER TO $DB_USER;
EOF

echo "=== Running Django Migrations ==="

# Check if manage.py exists in current directory before migrating
if [ -f "manage.py" ]; then
    python manage.py migrate
else
    echo "Warning: manage.py not found in current directory. Skipping migrations."
fi

echo "=== Database Initialization Complete ==="
