-- Create application user with limited permissions
CREATE USER app_user WITH PASSWORD '${POSTGRES_APP_PASSWORD}';

-- Grant necessary permissions
GRANT CONNECT ON DATABASE ${POSTGRES_DB} TO app_user;

-- Connect to the database
\c ${POSTGRES_DB};

-- Grant permissions on existing tables
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- Grant permissions for future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON SEQUENCES TO app_user;