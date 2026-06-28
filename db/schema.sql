CREATE TABLE IF NOT EXISTS cache_entries (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  prompt_hash VARCHAR(64) NOT NULL,
  prompt_text TEXT NOT NULL,
  response_text LONGTEXT NOT NULL,
  model_name VARCHAR(128) NOT NULL,
  embedding_json JSON NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_accessed_at TIMESTAMP NULL,
  hit_count INT NOT NULL DEFAULT 0,
  INDEX idx_cache_model_hash (model_name, prompt_hash)
);

CREATE TABLE IF NOT EXISTS routing_rules (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(128) NOT NULL UNIQUE,
  match_type VARCHAR(64) NOT NULL,
  pattern VARCHAR(512) NOT NULL,
  target_model VARCHAR(128) NOT NULL,
  priority INT NOT NULL DEFAULT 0,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_routing_active_priority (active, priority)
);

CREATE TABLE IF NOT EXISTS request_logs (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  request_id VARCHAR(64) NOT NULL,
  prompt_hash VARCHAR(64) NOT NULL,
  model_name VARCHAR(128) NOT NULL,
  route_name VARCHAR(128) NOT NULL,
  cache_hit BOOLEAN NOT NULL,
  latency_ms DECIMAL(10, 2) NOT NULL,
  status_code INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_request_logs_created_at (created_at),
  INDEX idx_request_logs_route (route_name)
);
