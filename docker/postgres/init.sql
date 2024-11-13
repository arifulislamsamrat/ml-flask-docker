CREATE DATABASE mlflow;
\c mlflow;

CREATE TABLE IF NOT EXISTS experiments (
    experiment_id SERIAL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    artifact_location VARCHAR(256),
    lifecycle_stage VARCHAR(32)
);

CREATE TABLE IF NOT EXISTS runs (
    run_uuid VARCHAR(32) PRIMARY KEY,
    experiment_id INTEGER REFERENCES experiments(experiment_id),
    name VARCHAR(250),
    source_type VARCHAR(20),
    source_name VARCHAR(500),
    entry_point_name VARCHAR(50),
    start_time BIGINT,
    end_time BIGINT,
    source_version VARCHAR(50),
    lifecycle_stage VARCHAR(20),
    artifact_uri VARCHAR(200),
    status VARCHAR(20)
);