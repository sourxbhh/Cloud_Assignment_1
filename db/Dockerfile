# Use the official PostgreSQL 16 image [cite: 66]
FROM postgres:16

# Copy the initialization script to the entrypoint directory [cite: 67]
# Any .sql files in this directory are automatically executed when the container first starts[cite: 64, 97].
COPY init.sql /docker-entrypoint-initdb.d/