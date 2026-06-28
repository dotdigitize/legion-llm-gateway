INSERT INTO routing_rules (name, match_type, pattern, target_model, priority, active)
VALUES
  ('code-prompts', 'keyword', 'python,typescript,javascript,sql,function,class,bug,stack trace,api', 'codellama', 100, TRUE),
  ('general-prompts', 'fallback', '*', 'llama3.1', 10, TRUE)
ON DUPLICATE KEY UPDATE
  match_type = VALUES(match_type),
  pattern = VALUES(pattern),
  target_model = VALUES(target_model),
  priority = VALUES(priority),
  active = VALUES(active);

INSERT INTO cache_entries (prompt_hash, prompt_text, response_text, model_name, embedding_json, hit_count)
VALUES
  (
    'b2b3d86f6bde7ed41d8a4dc6f9b450cc4b631fc196ef98ad48e4fdff59f9c7df',
    'Summarize semantic caching for local inference gateways.',
    'Semantic caching reuses responses for closely related prompts after vector similarity matching.',
    'llama3.1',
    JSON_ARRAY(0.12, 0.04, -0.09, 0.21),
    3
  );
