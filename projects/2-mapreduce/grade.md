# LSDS Project 2 Grade


| Type      | % | Grade            |
|-----------|-----|----------------|
| Essential (^)     | 60%  | 6.13/10 |
| Nice-to-haves (^^)       | 20%  | 6.13/10 |
| Difficult (^^^)   | 20%  | 7.0/10 |
| **Total**   | **100%**  | **63.0/100** |

## Breakdown

### Essentials (^)

| Exercise | Test case | Description | Submitted | Max marks | Marks | Notes |
| -------- | --------- | ----------- | --------- | --------- | ----- | ----- |
| 2.1.1 | test_worker1_healthcheck | /healthcheck must return 200 OK and {'status': 'up'} for Worker 1. | Yes | 1 | 1 |  |
| 2.1.1 | test_worker2_healthcheck | /healthcheck must return 200 OK and {'status': 'up'} for Worker 2. | Yes | 1 | 1 |  |
| 2.1.1 | test_worker3_healthcheck | /healthcheck must return 200 OK and {'status': 'up'} for Worker 3. | Yes | 1 | 1 |  |
| 2.1.1 | test_worker4_healthcheck | /healthcheck must return 200 OK and {'status': 'up'} for Worker 4. | Yes | 1 | 1 |  |
| 2.1.1 | test_worker5_healthcheck | /healthcheck must return 200 OK and {'status': 'up'} for Worker 5. | Yes | 1 | 1 |  |
| 2.1.2 | test_map_endpoint | POST /map returns 2XX and {'status':'in-progress'}. | Yes | 5 | 5 |  |
| 2.1.3 | test_map_output_structure | GET /map-output returns mapped values grouped by key. | Yes | 10 | 0 | [logs](#test_map_output_structure-logs) |
| 2.1.4 | test_reduce_endpoint | POST /reduce returns 2XX and {'status':'in-progress'}. | Yes | 5 | 5 |  |
| 2.1.4 | test_reduce_endpoint_output | After POST /reduce worker creates output file with expected results. | Yes | 10 | 0 | [logs](#test_reduce_endpoint_output-logs) |
| 2.2.1 | test_master_healthcheck | Master /healthcheck must return 200 and {'status':'up'}. | Yes | 1 | 1 |  |
| 2.2.2 | test_create_job | POST /jobs must create job and return valid structure. | Yes | 3 | 1 |  |
| 2.2.2 | test_create_job_response_body | POST /jobs must return valid body. | Yes | 1 | 0 | [logs](#test_create_job_response_body-logs) |
| 2.2.2 | test_create_job_idle_reducers | POST /jobs must show reducers are idle and without an assigned worker after creation | Yes | 1 | 1 |  |
| 2.2.2 | test_create_job_invalid_data_path | POST /jobs with invalid data path must return 400-class error. | Yes | 5 | 0 | [logs](#test_create_job_invalid_data_path-logs) |
| 2.2.2 | test_create_job_mismatched_map_partitions | POST /jobs with mismatched map partitions must return 400-class error. | Yes | 5 | 0 | [logs](#test_create_job_mismatched_map_partitions-logs) |
| 2.2.3 | test_get_job | GET /jobs/{job_id} must return 200 | Yes | 3 | 0 | [logs](#test_get_job-logs) |
| 2.2.3 | test_get_job_body | GET /jobs/{job_id} must return the job information in the right structure | Yes | 2 | 2 |  |
| 2.2.3 | test_get_unknown_job | GET unknown job must return 404. | Yes | 5 | 5 |  |
| 2.2.3 | test_word_count_small_job | word_count job (small-text, 1 map partition, 1 reduce partition) completes end-to-end | Yes | 5 | 5 |  |
| 2.2.3 | test_word_count_medium_job | word_count job (medium-text, 4 map partitions, 2 reduce partitions) completes end-to-end | Yes | 5 | 5 |  |
| 2.2.4 | test_word_count_small_mappers_completed | word_count small-text: all 1 mapper(s) marked as completed | Yes | 5 | 5 |  |
| 2.2.4 | test_word_count_medium_mappers_completed | word_count medium-text: all 4 mapper(s) marked as completed | Yes | 5 | 5 |  |
| 2.2.5 | test_reduce_completion_conflict_when_maps_pending | POST reduce completion must return 409 if maps still pending | Yes | 5 | 0 | [logs](#test_reduce_completion_conflict_when_maps_pending-logs) |
| 2.2.5 | test_word_count_small_reducers_completed | word_count small-text: all 1 reducer(s) marked as completed | Yes | 5 | 5 |  |
| 2.2.5 | test_word_count_small_output | word_count small-text: output matches expected snapshot (1 partition) | Yes | 5 | 5 |  |
| 2.2.5 | test_word_count_medium_reducers_completed | word_count medium-text: all 2 reducer(s) marked as completed | Yes | 5 | 5 |  |
| 2.2.5 | test_word_count_medium_output | word_count medium-text: output matches expected snapshots (2 partitions) | Yes | 5 | 5 |  |

### Nice to haves (^^)

| Exercise | Test case | Description | Submitted | Max marks | Marks | Notes |
| -------- | --------- | ----------- | --------- | --------- | ----- | ----- |
| 2.2.6 | test_client_word_count_small_run | Client script - run and job_id format (small-text) | Yes | 4 | 0 |  |
| 2.2.6 | test_client_word_count_small_completed_message | Client script - completed message (small-text) | Yes | 3 | 3 |  |
| 2.2.6 | test_client_word_count_small_progress_messages | Client script - progress messages (small-text) | Yes | 4 | 4 |  |
| 2.2.6 | test_client_word_count_small_results_directory | Client script - results directory (small-text) | Yes | 3 | 3 |  |
| 2.2.6 | test_client_word_count_small_job_completed | Client script - job completes successfully (small-text) | Yes | 2 | 2 |  |
| 2.2.6 | test_client_word_count_medium_run | Client script - run and job_id format (medium-text) | Yes | 4 | 4 |  |
| 2.2.6 | test_client_word_count_medium_completed_message | Client script - completed message (medium-text) | Yes | 3 | 3 |  |
| 2.2.6 | test_client_word_count_medium_progress_messages | Client script - progress messages (medium-text) | Yes | 4 | 4 |  |
| 2.2.6 | test_client_word_count_medium_results_directory | Client script - results directory (medium-text) | Yes | 3 | 3 |  |
| 2.2.6 | test_client_word_count_medium_job_completed | Client script - job completes successfully (medium-text) | Yes | 2 | 2 |  |
| 2.3.1 | test_modified_word_count_app | modified_word_count must count words starting with 't' and length > 3. | Yes | 10 | 10 | [logs](#test_modified_word_count_app-logs) |
| 2.3.2 | test_links_app | links app must count requests per user agent. | Yes | 10 | 0 | [logs](#test_links_app-logs) |
| 2.3.3 | test_bigrams_app | bigrams app must count bigrams appearing more than once. | Yes | 10 | 0 | [logs](#test_bigrams_app-logs) |

### Difficult (^^^)

| Exercise | Test case | Description | Submitted | Max marks | Marks | Notes |
| -------- | --------- | ----------- | --------- | --------- | ----- | ----- |
| 2.2.7 | test_worker_failure_handling | Master must detect worker failure and reassign tasks. | Yes | 10 | 4 |  |
| 2.2.8 | test_worker_balancing_work | Workers must handle at most one task at a time. | Yes | 10 | 10 |  |

## Comments

Docked marks in the client and master because of not up to spec data path handling - see fixes I applied

Docked marks in the healthcheck because:
- You don't check for non 200 status
- You have a bug where you don't add tasks to the queue if all workers are dead

## Debug Information

### test_map_output_structure-logs

**Error:**

```
worker1_url = 'http://localhost:8001'

    @essential
    @marks(10)
    @exercise("2.1.3")
    @description("GET /map-output returns mapped values grouped by key.")
    @pytest.mark.order(120)
    def test_map_output_structure(worker1_url):
        params = {
            "job_id": job_id,
            "map_partition": 0,
            "reduce_partition": 0
        }
        time.sleep(2)  # Wait until POST /map is complete
    
        resp = httpx.get(f"{worker1_url}/map-output", params=params)
>       assert resp.status_code == 200
E       assert 422 == 200
E        +  where 422 = <Response [422 Unprocessable Entity]>.status_code

tests/test_worker.py:117: AssertionError
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8001/map-output?job_id=605e80a4-5aa2-450e-927e-11a30d8e5236&map_partition=0&reduce_partition=0 "HTTP/1.1 422 Unprocessable Entity"
```

**Container Logs:**

```
Found 7 running containers: client, worker4, worker3, worker1, master, worker5, worker2

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.1:53678 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:48488 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.4:45666 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:34302 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:52022 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.1:43750 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:40278 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:40286 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.1:40296 - "GET /map-output?job_id=605e80a4-5aa2-450e-927e-11a30d8e5236&map_partition=0&reduce_partition=0 HTTP/1.1" 422 Unprocessable Entity
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:40270 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.1:37940 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:60912 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.4:45206 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:42908 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:58230 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

```

### test_reduce_endpoint_output-logs

**Error:**

```
@essential
    @marks(10)
    @exercise("2.1.4")
    @description("After POST /reduce worker creates output file with expected results.")
    @pytest.mark.order(131)
    def test_reduce_endpoint_output():
        # Wait up to 5 seconds for the results folder to be created
        result_path = os.path.join(SOLUTION_PATH, 'results', job_id, '0')
        expected_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_worker', '0')
    
        timeout = 5.0
        start_time = time.time()
        while time.time() - start_time < timeout:
            if os.path.isfile(result_path):
                break
            time.sleep(0.5)
        else:
            raise AssertionError(f"Results file not found at {result_path} after {timeout} seconds")
    
>       compare_out_file(result_path, expected_path)

tests/test_worker.py:190: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

result_path = './../projects/2-mapreduce/results/605e80a4-5aa2-450e-927e-11a30d8e5236/0'
expected_path = '/home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_worker/0'

    def compare_out_file(result_path, expected_path) -> bool:
        with open(result_path, "r") as f1, open(expected_path, "r") as f2:
            lines1 = sorted(line.strip() for line in f1 if line.strip())
            lines2 = sorted(line.strip() for line in f2 if line.strip())
            if lines1 != lines2:
                missing = set(lines2) - set(lines1)
                extra = set(lines1) - set(lines2)
                error_msg = f"Output mismatch between {result_path} and {expected_path}\n"
                error_msg += f"Expected {len(lines2)} lines, got {len(lines1)} lines\n"
                if missing:
                    error_msg += f"Missing {len(missing)} lines: {missing}\n"
                if extra:
                    error_msg += f"Extra {len(extra)} lines: {extra}"
>               raise AssertionError(error_msg)
E               AssertionError: Output mismatch between ./../projects/2-mapreduce/results/605e80a4-5aa2-450e-927e-11a30d8e5236/0 and /home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_worker/0
E               Expected 27 lines, got 0 lines
E               Missing 27 lines: {'brown 2', 'dog 1', 'all 1', 'but 1', 'one 1', "don't 1", 'they 1', 'jumps 1', 'thinking 1', 'fox 3', 'not 1', 'lazy 2', 'quick 5', 'the 4', 'jump; 1', 'is 1', 'dogs 1', 'day 1', 'helps 1', 'nap 1', 'this 1', 'was! 1', 'foxes 1', 'escape 1', 'over 1', 'are 1', 'always 1'}

tests/utils.py:76: AssertionError
```

**Container Logs:**

```
Found 7 running containers: client, worker4, worker3, worker1, master, worker5, worker2

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.1:53678 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:48488 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.4:45666 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:34302 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:52022 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.1:43750 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:40278 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:40286 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.1:40296 - "GET /map-output?job_id=605e80a4-5aa2-450e-927e-11a30d8e5236&map_partition=0&reduce_partition=0 HTTP/1.1" 422 Unprocessable Entity
INFO:     172.18.0.1:40302 - "POST /reduce HTTP/1.1" 200 OK
INFO:     172.18.0.6:37872 - "GET /map-output?job_id=605e80a4-5aa2-450e-927e-11a30d8e5236&map_partition=0&reduce_partition=0 HTTP/1.1" 422 Unprocessable Entity
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:40270 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.6:59032 - "POST /jobs/605e80a4-5aa2-450e-927e-11a30d8e5236/reduce/0/completed HTTP/1.1" 404 Not Found
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.1:37940 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:60912 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.4:45206 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:42908 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:58230 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

```

### test_create_job_response_body-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @essential
    @marks(1)
    @exercise("2.2.2")
    @description("POST /jobs must return valid body.")
    @pytest.mark.order(211)
    def test_create_job_response_body(master_url):
        body = master_test_job_body
    
        assert "job_id" in body
        parsed_uuid = uuid.UUID(body["job_id"])
        assert parsed_uuid.version == 4
        assert body["app_name"] == "word_count"
        assert body["data_path"] == "./data/small-text"
        assert body["map_partitions"] == 1
        assert body["reduce_partitions"] == 1
>       assert body["status"] == "in-progress"
E       AssertionError: assert 'mapping' == 'in-progress'
E         
E         [0m[91m- in-progress[39;49;00m[90m[39;49;00m
E         [92m+ mapping[39;49;00m[90m[39;49;00m

tests/test_master.py:71: AssertionError
```

**Container Logs:**

```
Found 7 running containers: client, worker4, worker3, worker5, worker1, worker2, master

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.5:54968 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36108 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.5:43222 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:37182 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.5:46258 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:48814 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.5:40936 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:58406 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48362 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.5:38122 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:38162 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:39714 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36874 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36876 - "POST /jobs HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```

### test_create_job_invalid_data_path-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @essential
    @marks(5)
    @exercise("2.2.2")
    @description("POST /jobs with invalid data path must return 400-class error.")
    @pytest.mark.order(215)
    def test_create_job_invalid_data_path(master_url):
        payload = {
            "app_name": "word_count",
            "data_path": "./data/nonexistent-path",
            "map_partitions": 1,
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
>       assert 400 <= resp.status_code < 500, f"Expected 4xx error for invalid data path, got {resp.status_code}"
E       AssertionError: Expected 4xx error for invalid data path, got 200
E       assert 400 <= 200
E        +  where 200 = <Response [200 OK]>.status_code

tests/test_master.py:100: AssertionError
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: POST http://localhost:8000/jobs "HTTP/1.1 200 OK"
```

**Container Logs:**

```
Found 7 running containers: client, worker4, worker3, worker5, worker1, worker2, master

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.5:54968 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36108 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.5:43222 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:37182 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.5:46258 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:48814 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.5:40936 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:58406 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48362 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.5:38122 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:38162 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:55734 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:39714 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36874 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36876 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36880 - "POST /jobs HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```

### test_create_job_mismatched_map_partitions-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @essential
    @marks(5)
    @exercise("2.2.2")
    @description("POST /jobs with mismatched map partitions must return 400-class error.")
    @pytest.mark.order(216)
    def test_create_job_mismatched_map_partitions(master_url):
        payload = {
            "app_name": "word_count",
            "data_path": "./data/small-text",
            "map_partitions": 5,  # small-text only has 1 partition
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
>       assert 400 <= resp.status_code < 500, f"Expected 4xx error for mismatched map partitions, got {resp.status_code}"
E       AssertionError: Expected 4xx error for mismatched map partitions, got 200
E       assert 400 <= 200
E        +  where 200 = <Response [200 OK]>.status_code

tests/test_master.py:116: AssertionError
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: POST http://localhost:8000/jobs "HTTP/1.1 200 OK"
```

**Container Logs:**

```
Found 7 running containers: client, worker4, worker3, worker5, worker1, worker2, master

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.5:54968 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36108 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:34660 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.5:43222 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:37182 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:53096 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.5:46258 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:48814 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48906 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.5:40936 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:58406 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48362 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.5:38122 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:38162 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:55734 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:39714 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36874 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36876 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36880 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36884 - "POST /jobs HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```

### test_get_job-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @essential
    @marks(3)
    @exercise("2.2.3")
    @description("GET /jobs/{job_id} must return 200")
    @pytest.mark.order(220)
    def test_get_job(master_url):
        resp = httpx.get(f"{master_url}/jobs/{master_test_job_id}")
        assert resp.status_code == 200
    
        body = resp.json()
        global retrieved_job_body
        retrieved_job_body = body
    
        assert "job_id" in body
>       assert body["status"] == "in-progress" or body["status"] == "completed"
E       AssertionError: assert ('mapping' == 'in-progress'
E         
E         [0m[91m- in-progress[39;49;00m[90m[39;49;00m
E         [92m+ mapping[39;49;00m[90m[39;49;00m or 'mapping' == 'completed'
E         
E         [0m[91m- completed[39;49;00m[90m[39;49;00m
E         [92m+ mapping[39;49;00m[90m[39;49;00m)

tests/test_master.py:139: AssertionError
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/c4bf707b-7013-4723-b022-d6f2c2be8591 "HTTP/1.1 200 OK"
```

**Container Logs:**

```
Found 7 running containers: client, worker4, worker3, worker5, worker1, worker2, master

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.5:54968 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36108 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:34660 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.5:43222 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:37182 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:53096 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.5:46258 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:48814 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48906 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.5:40936 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:58406 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48362 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.5:38122 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:38162 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:55734 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:39714 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36874 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36876 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36880 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36884 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36898 - "GET /jobs/c4bf707b-7013-4723-b022-d6f2c2be8591 HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```

### test_reduce_completion_conflict_when_maps_pending-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @essential
    @marks(5)
    @exercise("2.2.5")
    @description("POST reduce completion must return 409 if maps still pending")
    @pytest.mark.order(250)
    def test_reduce_completion_conflict_when_maps_pending(master_url):
        # Create a new job with small-text (1 partition)
        payload = {
            "app_name": "word_count",
            "data_path": "./data/small-text",
            "map_partitions": 1,
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
        assert resp.status_code in [200, 201]
        job = resp.json()
        job_id = job["job_id"]
    
        # Get the job immediately and check if mapper is still pending
        resp = httpx.get(f"{master_url}/jobs/{job_id}")
        assert resp.status_code == 200
        job = resp.json()
    
        # If mapper is still pending, try to mark reducer complete -> expect 409
        if any(m.get("status") != "completed" for m in job["mappers"]):
            reducer_partition = job["reducers"][0]["partition"]
            resp = httpx.post(f"{master_url}/jobs/{job_id}/reduce/{reducer_partition}/completed")
>           assert resp.status_code == 409
E           assert 200 == 409
E            +  where 200 = <Response [200 OK]>.status_code

tests/test_master.py:193: AssertionError
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: POST http://localhost:8000/jobs "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/75c1207f-af8f-49a1-9e9b-c317321e3091 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: POST http://localhost:8000/jobs/75c1207f-af8f-49a1-9e9b-c317321e3091/reduce/0/completed "HTTP/1.1 200 OK"
```

**Container Logs:**

```
Found 7 running containers: client, worker4, worker3, worker5, worker1, worker2, master

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.5:54968 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36108 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:34660 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.5:43222 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:37182 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:53096 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.5:46258 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:48814 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48906 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.5:40936 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:58406 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:48362 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.5:38122 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:38162 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.5:55734 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:39714 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36874 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:36876 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36880 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36884 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36898 - "GET /jobs/c4bf707b-7013-4723-b022-d6f2c2be8591 HTTP/1.1" 200 OK
INFO:     172.18.0.1:36914 - "GET /jobs/46a61c91-7247-4b47-810a-5a48af003264 HTTP/1.1" 404 Not Found
INFO:     172.18.0.1:36924 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:36926 - "GET /jobs/75c1207f-af8f-49a1-9e9b-c317321e3091 HTTP/1.1" 200 OK
INFO:     172.18.0.1:36930 - "POST /jobs/75c1207f-af8f-49a1-9e9b-c317321e3091/reduce/0/completed HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

```

### test_modified_word_count_app-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @nice_to_have
    @marks(10)
    @exercise("2.3.1")
    @description("modified_word_count must count words starting with 't' and length > 3.")
    @pytest.mark.order(300)
    def test_modified_word_count_app(master_url):
        # Create job via API
        payload = {
            "app_name": "modified_word_count",
            "data_path": "./data/medium-text",
            "map_partitions": 4,
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
        assert resp.status_code in [200, 201]
        job = resp.json()
        job_id = job["job_id"]
    
        # Wait for job completion
        timeout = 100.0
        start_time = time.time()
        completed = False
    
        while time.time() - start_time < timeout:
            resp = httpx.get(f"{master_url}/jobs/{job_id}")
            assert resp.status_code == 200
            job = resp.json()
    
            if job["status"] == "completed":
                completed = True
                break
    
            time.sleep(1)
    
        assert completed, f"Job {job_id} did not complete within {timeout} seconds"
    
        result_path = os.path.join(SOLUTION_PATH, 'results', job_id, '0')
        expected_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'modified_word_count', '0')
        expected_alt_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'modified_word_count_alt', '0')
    
        # Try comparing with the primary snapshot
        try:
>           compare_out_file(result_path, expected_path)

tests/test_mapred_apps.py:63: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

result_path = './../projects/2-mapreduce/results/ec6f6524-62db-45d3-83cb-175ec950189c/0'
expected_path = '/home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/modified_word_count/0'

    def compare_out_file(result_path, expected_path) -> bool:
        with open(result_path, "r") as f1, open(expected_path, "r") as f2:
            lines1 = sorted(line.strip() for line in f1 if line.strip())
            lines2 = sorted(line.strip() for line in f2 if line.strip())
            if lines1 != lines2:
                missing = set(lines2) - set(lines1)
                extra = set(lines1) - set(lines2)
                error_msg = f"Output mismatch between {result_path} and {expected_path}\n"
                error_msg += f"Expected {len(lines2)} lines, got {len(lines1)} lines\n"
                if missing:
                    error_msg += f"Missing {len(missing)} lines: {missing}\n"
                if extra:
                    error_msg += f"Extra {len(extra)} lines: {extra}"
>               raise AssertionError(error_msg)
E               AssertionError: Output mismatch between ./../projects/2-mapreduce/results/ec6f6524-62db-45d3-83cb-175ec950189c/0 and /home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/modified_word_count/0
E               Expected 1 lines, got 1 lines
E               Missing 1 lines: {'num_t_words 9'}
E               Extra 1 lines: {'total 9'}

tests/utils.py:76: AssertionError

During handling of the above exception, another exception occurred:

master_url = 'http://localhost:8000'

    @nice_to_have
    @marks(10)
    @exercise("2.3.1")
    @description("modified_word_count must count words starting with 't' and length > 3.")
    @pytest.mark.order(300)
    def test_modified_word_count_app(master_url):
        # Create job via API
        payload = {
            "app_name": "modified_word_count",
            "data_path": "./data/medium-text",
            "map_partitions": 4,
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
        assert resp.status_code in [200, 201]
        job = resp.json()
        job_id = job["job_id"]
    
        # Wait for job completion
        timeout = 100.0
        start_time = time.time()
        completed = False
    
        while time.time() - start_time < timeout:
            resp = httpx.get(f"{master_url}/jobs/{job_id}")
            assert resp.status_code == 200
            job = resp.json()
    
            if job["status"] == "completed":
                completed = True
                break
    
            time.sleep(1)
    
        assert completed, f"Job {job_id} did not complete within {timeout} seconds"
    
        result_path = os.path.join(SOLUTION_PATH, 'results', job_id, '0')
        expected_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'modified_word_count', '0')
        expected_alt_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'modified_word_count_alt', '0')
    
        # Try comparing with the primary snapshot
        try:
            compare_out_file(result_path, expected_path)
        except AssertionError:
>           compare_out_file(result_path, expected_alt_path)

tests/test_mapred_apps.py:65: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

result_path = './../projects/2-mapreduce/results/ec6f6524-62db-45d3-83cb-175ec950189c/0'
expected_path = '/home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/modified_word_count_alt/0'

    def compare_out_file(result_path, expected_path) -> bool:
        with open(result_path, "r") as f1, open(expected_path, "r") as f2:
            lines1 = sorted(line.strip() for line in f1 if line.strip())
            lines2 = sorted(line.strip() for line in f2 if line.strip())
            if lines1 != lines2:
                missing = set(lines2) - set(lines1)
                extra = set(lines1) - set(lines2)
                error_msg = f"Output mismatch between {result_path} and {expected_path}\n"
                error_msg += f"Expected {len(lines2)} lines, got {len(lines1)} lines\n"
                if missing:
                    error_msg += f"Missing {len(missing)} lines: {missing}\n"
                if extra:
                    error_msg += f"Extra {len(extra)} lines: {extra}"
>               raise AssertionError(error_msg)
E               AssertionError: Output mismatch between ./../projects/2-mapreduce/results/ec6f6524-62db-45d3-83cb-175ec950189c/0 and /home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/modified_word_count_alt/0
E               Expected 8 lines, got 1 lines
E               Missing 8 lines: {'tales 1', 'their 2', 'tires 1', 'this 1', 'they 1', 'trees 1', 'that 1', 'town 1'}
E               Extra 1 lines: {'total 9'}

tests/utils.py:76: AssertionError
```

**CAPTURED STDOUT SETUP Logs:**

```
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
#0 building with "default" instance using docker driver

#1 [worker4 internal] load build definition from Dockerfile
#1 transferring dockerfile: 201B 0.0s done
#1 DONE 0.0s

#2 [worker2 internal] load build definition from Dockerfile
#2 transferring dockerfile: 201B 0.0s done
#2 DONE 0.0s

#3 [worker5 internal] load build definition from Dockerfile
#3 transferring dockerfile: 201B done
#3 DONE 0.0s

#4 [worker3 internal] load build definition from Dockerfile
#4 transferring dockerfile: 201B done
#4 DONE 0.0s

#5 [master internal] load build definition from Dockerfile
#5 transferring dockerfile: 205B done
#5 DONE 0.0s

#6 [worker1 internal] load build definition from Dockerfile
#6 transferring dockerfile: 201B done
#6 DONE 0.0s

#7 [worker1 internal] load metadata for docker.io/library/python:3.11-slim
#7 DONE 0.4s

#8 [worker4 internal] load .dockerignore
#8 transferring context: 2B done
#8 DONE 0.0s

#9 [worker3 internal] load .dockerignore
#9 transferring context: 2B done
#9 DONE 0.0s

#10 [worker2 internal] load .dockerignore
#10 transferring context: 2B done
#10 DONE 0.0s

#11 [master internal] load .dockerignore
#11 transferring context: 2B done
#11 DONE 0.0s

#12 [worker1 internal] load .dockerignore
#12 transferring context: 2B done
#12 DONE 0.0s

#13 [worker5 1/4] FROM docker.io/library/python:3.11-slim@sha256:0b23cfb7425d065008b778022a17b1551c82f8b4866ee5a7a200084b7e2eafbf
#13 resolve docker.io/library/python:3.11-slim@sha256:0b23cfb7425d065008b778022a17b1551c82f8b4866ee5a7a200084b7e2eafbf 0.0s done
#13 DONE 0.0s

#14 [worker5 internal] load .dockerignore
#14 transferring context: 2B done
#14 DONE 0.1s

#15 [worker3 internal] load build context
#15 transferring context: 59B done
#15 DONE 0.0s

#16 [worker4 internal] load build context
#16 transferring context: 59B done
#16 DONE 0.0s

#17 [master internal] load build context
#17 transferring context: 59B done
#17 DONE 0.0s

#18 [worker2 internal] load build context
#18 transferring context: 59B done
#18 DONE 0.0s

#19 [worker1 internal] load build context
#19 transferring context: 59B done
#19 DONE 0.0s

#20 [worker1 2/4] WORKDIR /code
#20 CACHED

#21 [worker1 3/4] RUN pip install fastapi uvicorn httpx
#21 CACHED

#22 [worker1 4/4] COPY . .
#22 CACHED

#23 [master 4/4] COPY . .
#23 CACHED

#24 [worker5 internal] load build context
#24 transferring context: 59B done
#24 DONE 0.0s

#25 [master] exporting to image
#25 exporting layers
#25 ...

#21 [worker5 3/4] RUN pip install fastapi uvicorn httpx
#21 CACHED

#20 [worker5 2/4] WORKDIR /code
#20 CACHED

#22 [worker5 4/4] COPY . .
#22 CACHED

#25 [master] exporting to image
#25 exporting layers done
#25 exporting manifest sha256:c932bc9bdf583d50133241cf247d0a6f2eedac57ceaccfae461a77b71f436703 done
#25 exporting config sha256:3889619dd8026b19b47d4ae71ba82806a9b849cc419077f36d64d9d13529268f done
#25 exporting attestation manifest sha256:c0243113c4c5874a93bcc76c8f1de23e8fe54260b0277f1e273535c91093fe99
#25 exporting attestation manifest sha256:c0243113c4c5874a93bcc76c8f1de23e8fe54260b0277f1e273535c91093fe99 0.1s done
#25 exporting manifest list sha256:8e5349f256d0008826624e0d85a45c5fe8f5619e12a3c2154e03dc2582e34ed4
#25 exporting manifest list sha256:8e5349f256d0008826624e0d85a45c5fe8f5619e12a3c2154e03dc2582e34ed4 0.1s done
#25 naming to docker.io/library/2-mapreduce-master:latest 0.0s done
#25 unpacking to docker.io/library/2-mapreduce-master:latest 0.0s done
#25 DONE 0.3s

#26 [worker4] exporting to image
#26 exporting layers done
#26 exporting manifest sha256:083acea3972255cae7cf8c8b2b6f1349a5773127e759886915ae9c3de0dead5e done
#26 exporting config sha256:fe0f49fa6c7fa7c7b87db9be12e54343cd11c3f71695131536d8f90d6b137360 done
#26 exporting attestation manifest sha256:2907a00172f64e93997764f3ccf6e6918de95f908f2ee433e63fd68f0c98fdbd 0.1s done
#26 exporting manifest list sha256:b5d965b38e8d8d32a939d7613bf7f67f0cdeedaf818e1e5272c7183232608db6 0.0s done
#26 naming to docker.io/library/2-mapreduce-worker4:latest 0.0s done
#26 unpacking to docker.io/library/2-mapreduce-worker4:latest 0.0s done
#26 DONE 0.3s

#27 [worker3] exporting to image
#27 exporting layers done
#27 exporting manifest sha256:abe211f4022437e59aae363511dff65883cdc328cd4c46fee8cd9a9eb86073a8 done
#27 exporting config sha256:cd2881806369ab88b92cb552d3143650af5f1bd334a1363a1c214d21eee7cf73 done
#27 exporting attestation manifest sha256:90cd9112f5217db326345127349259f17e7583e8e075d7f89a56a4b71d18e1e8 0.1s done
#27 exporting manifest list sha256:d3f5fed3bbb3c7ead41c313728190a848cd4ce3832e6f3f70432447c27acde26 0.0s done
#27 naming to docker.io/library/2-mapreduce-worker3:latest 0.0s done
#27 unpacking to docker.io/library/2-mapreduce-worker3:latest 0.0s done
#27 DONE 0.3s

#28 [worker2] exporting to image
#28 exporting layers done
#28 exporting manifest sha256:7bf0c1208ff62a28f017c4582f75ecef7538bf685745332bcef950244e22215d done
#28 exporting config sha256:c57d06e765fd7ce144285095d133d91a5fcd271027bc326881b48538f938174c done
#28 exporting attestation manifest sha256:6de98bdaa29082bd60d9103ce54c8c7a9852e1a355a1500f765e795a55a20057 0.1s done
#28 exporting manifest list sha256:29709c8735bc7cfd2fded1c47dd7e9fc8315c299484262a604fc2d6e61990719 0.0s done
#28 naming to docker.io/library/2-mapreduce-worker2:latest 0.0s done
#28 unpacking to docker.io/library/2-mapreduce-worker2:latest 0.0s done
#28 DONE 0.3s

#29 [worker1] exporting to image
#29 exporting layers done
#29 exporting manifest sha256:9bb53c8e682d57ce2ca09cdfe659d099e9bd2a2ff58d5fe1dcae6ee33ced55aa done
#29 exporting config sha256:bcd4584418c15974b867f26e8df4232a0e32d8fbffb0cea2ca82f7e317acae2b 0.0s done
#29 exporting attestation manifest sha256:a73d962ef41b5223b2610c22cddeeb13e0a495c8059244f5b9e3e88d55ad7add 0.1s done
#29 exporting manifest list sha256:7300a9a812ec863ed78e094c4950b420678aacf157a663f9601bf45b0367e406 0.0s done
#29 naming to docker.io/library/2-mapreduce-worker1:latest 0.0s done
#29 unpacking to docker.io/library/2-mapreduce-worker1:latest 0.0s done
#29 DONE 0.3s

#30 [worker5] exporting to image
#30 exporting layers done
#30 exporting manifest sha256:6c73ef2ba924a37677b1b230118caeb923eba91a5372eadcfe354004a34944f9 0.0s done
#30 exporting config sha256:383e8b23665772f7e95bf0594623181bfd955ee0e2eac110b95d63bc0119106d 0.0s done
#30 exporting attestation manifest sha256:46e3f6ec18980f419fe81f11949995ac55cbc67811c017ce9c2d2c10c781b9e0 0.1s done
#30 exporting manifest list sha256:d98a22897d31417b603f6c5633851d735d18b7c075dd171e1ed2bffcd5e1abaf 0.0s done
#30 naming to docker.io/library/2-mapreduce-worker5:latest done
#30 unpacking to docker.io/library/2-mapreduce-worker5:latest 0.0s done
#30 DONE 0.3s

#31 [worker4] resolving provenance for metadata file
#31 DONE 0.2s

#32 [worker3] resolving provenance for metadata file
#32 DONE 0.1s

#33 [master] resolving provenance for metadata file
#33 DONE 0.0s

#34 [worker1] resolving provenance for metadata file
#34 DONE 0.1s

#35 [worker2] resolving provenance for metadata file
#35 DONE 0.2s

#36 [worker5] resolving provenance for metadata file
#36 DONE 0.0s

#37 [client internal] load build definition from Dockerfile
#37 transferring dockerfile: 145B done
#37 DONE 0.0s

#7 [client internal] load metadata for docker.io/library/python:3.11-slim
#7 DONE 0.6s

#38 [client internal] load .dockerignore
#38 transferring context: 2B done
#38 DONE 0.0s

#39 [client internal] load build context
#39 transferring context: 92B done
#39 DONE 0.0s

#13 [client 1/4] FROM docker.io/library/python:3.11-slim@sha256:0b23cfb7425d065008b778022a17b1551c82f8b4866ee5a7a200084b7e2eafbf
#13 resolve docker.io/library/python:3.11-slim@sha256:0b23cfb7425d065008b778022a17b1551c82f8b4866ee5a7a200084b7e2eafbf 0.0s done
#13 DONE 0.1s

#40 [client 3/4] RUN pip install httpx
#40 CACHED

#41 [client 2/4] WORKDIR /client
#41 CACHED

#42 [client 4/4] COPY . .
#42 CACHED

#43 [client] exporting to image
#43 exporting layers done
#43 exporting manifest sha256:ac4685d3c0daa20ad79222b9fff6beea4fbe03f96ae7743f3eb38ba2dc5d0e7a done
#43 exporting config sha256:2e664db5590c6faafad334605e97d275508504389ed8e3dad3be554b302b6d88 done
#43 exporting attestation manifest sha256:b469989c2ed8123a51f0e28432762eeacdd5d5ec4f11c8c5387e1e5394074d65 0.0s done
#43 exporting manifest list sha256:528d6f4c227b405d91d5b955a2e725ea76176e38134d3117785a6cf6f4c37902 0.0s done
#43 naming to docker.io/library/2-mapreduce-client:latest done
#43 unpacking to docker.io/library/2-mapreduce-client:latest
#43 unpacking to docker.io/library/2-mapreduce-client:latest done
#43 DONE 0.1s

#44 [client] resolving provenance for metadata file
#44 DONE 0.0s

```

**CAPTURED STDERR SETUP Logs:**

```
 client  Built
 master  Built
 worker1  Built
 worker2  Built
 worker3  Built
 worker4  Built
 worker5  Built
 Network 2-mapreduce_mapreduce  Creating
 Network 2-mapreduce_mapreduce  Created
 Container worker4  Creating
 Container worker5  Creating
 Container worker3  Creating
 Container worker2  Creating
 Container master  Creating
 Container worker1  Creating
 Container worker4  Created
 Container master  Created
 Container client  Creating
 Container worker2  Created
 Container worker3  Created
 Container worker5  Created
 Container worker1  Created
 Container client  Created
 Container worker5  Starting
 Container worker1  Starting
 Container worker2  Starting
 Container worker3  Starting
 Container master  Starting
 Container worker4  Starting
 Container master  Started
 Container client  Starting
 Container worker2  Started
 Container worker1  Started
 Container worker3  Started
 Container worker5  Started
 Container worker4  Started
 Container client  Started

```

**CAPTURED LOG SETUP Logs:**

```
[32mINFO    [0m root:conftest.py:86 Using docker compose file at: ./../projects/2-mapreduce/docker-compose.yml
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/healthcheck "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8001/healthcheck "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8002/healthcheck "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8003/healthcheck "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8004/healthcheck "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8005/healthcheck "HTTP/1.1 200 OK"
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: POST http://localhost:8000/jobs "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/ec6f6524-62db-45d3-83cb-175ec950189c "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/ec6f6524-62db-45d3-83cb-175ec950189c "HTTP/1.1 200 OK"
```

**Container Logs:**

```
Found 7 running containers: client, worker1, worker5, worker2, worker3, master, worker4

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.1:42668 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.1:56122 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.3:45200 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:42516 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:55778 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:55782 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:55794 - "POST /reduce HTTP/1.1" 200 OK
INFO:     172.18.0.4:36612 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=0&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.4:36618 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=2&partition=0 HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.3:32830 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:44640 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:47388 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:47404 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.4:33576 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=1&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.4:33590 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=3&partition=0 HTTP/1.1" 404 Not Found
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:53888 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:35330 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:35342 - "GET /jobs/ec6f6524-62db-45d3-83cb-175ec950189c HTTP/1.1" 200 OK
INFO:     172.18.0.2:37494 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/1/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41178 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41192 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/2/completed HTTP/1.1" 200 OK
INFO:     172.18.0.2:37504 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/3/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41196 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/reduce/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:35344 - "GET /jobs/ec6f6524-62db-45d3-83cb-175ec950189c HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.1:51118 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

```

### test_links_app-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @nice_to_have
    @marks(10)
    @exercise("2.3.2")
    @description("links app must count requests per user agent.")
    @pytest.mark.order(310)
    def test_links_app(master_url):
        # Create job via API
        payload = {
            "app_name": "links",
            "data_path": "./data/small-logs",
            "map_partitions": 1,
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
        assert resp.status_code in [200, 201]
        job = resp.json()
        job_id = job["job_id"]
    
        # Wait for job completion
        timeout = 100.0
        start_time = time.time()
        completed = False
    
        while time.time() - start_time < timeout:
            resp = httpx.get(f"{master_url}/jobs/{job_id}")
            assert resp.status_code == 200
            job = resp.json()
    
            if job["status"] == "completed":
                completed = True
                break
    
            time.sleep(1)
    
        assert completed, f"Job {job_id} did not complete within {timeout} seconds"
    
        result_path = os.path.join(SOLUTION_PATH, 'results', job_id, '0')
        expected_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'links', '0')
    
>       compare_out_file(result_path, expected_path)

tests/test_mapred_apps.py:111: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

result_path = './../projects/2-mapreduce/results/3b289295-39ae-45e6-a65c-b9a0da1b5bc1/0'
expected_path = '/home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/links/0'

    def compare_out_file(result_path, expected_path) -> bool:
        with open(result_path, "r") as f1, open(expected_path, "r") as f2:
            lines1 = sorted(line.strip() for line in f1 if line.strip())
            lines2 = sorted(line.strip() for line in f2 if line.strip())
            if lines1 != lines2:
                missing = set(lines2) - set(lines1)
                extra = set(lines1) - set(lines2)
                error_msg = f"Output mismatch between {result_path} and {expected_path}\n"
                error_msg += f"Expected {len(lines2)} lines, got {len(lines1)} lines\n"
                if missing:
                    error_msg += f"Missing {len(missing)} lines: {missing}\n"
                if extra:
                    error_msg += f"Extra {len(extra)} lines: {extra}"
>               raise AssertionError(error_msg)
E               AssertionError: Output mismatch between ./../projects/2-mapreduce/results/3b289295-39ae-45e6-a65c-b9a0da1b5bc1/0 and /home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/links/0
E               Expected 3 lines, got 0 lines
E               Missing 3 lines: {'curl 4', 'Mozilla 13', 'PostmanRuntime 4'}

tests/utils.py:76: AssertionError
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: POST http://localhost:8000/jobs "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1 "HTTP/1.1 200 OK"
```

**Container Logs:**

```
Found 7 running containers: client, worker1, worker5, worker2, worker3, master, worker4

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.1:42668 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.1:56122 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.3:45200 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:42516 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:55778 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:55782 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:55794 - "POST /reduce HTTP/1.1" 200 OK
INFO:     172.18.0.4:36612 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=0&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.4:36618 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=2&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.3:55796 - "POST /reduce HTTP/1.1" 200 OK
INFO:     172.18.0.4:36624 - "GET /map-output?job_id=3b289295-39ae-45e6-a65c-b9a0da1b5bc1&map_partition=0&partition=0 HTTP/1.1" 404 Not Found
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.3:32830 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:44640 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:47388 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:47404 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.4:33576 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=1&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.4:33590 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=3&partition=0 HTTP/1.1" 404 Not Found
INFO:     172.18.0.3:47408 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:53888 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:35330 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:35342 - "GET /jobs/ec6f6524-62db-45d3-83cb-175ec950189c HTTP/1.1" 200 OK
INFO:     172.18.0.2:37494 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/1/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41178 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41192 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/2/completed HTTP/1.1" 200 OK
INFO:     172.18.0.2:37504 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/3/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41196 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/reduce/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:35344 - "GET /jobs/ec6f6524-62db-45d3-83cb-175ec950189c HTTP/1.1" 200 OK
INFO:     172.18.0.1:35356 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.2:37514 - "POST /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1/map/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:35368 - "GET /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1 HTTP/1.1" 200 OK
INFO:     172.18.0.4:41212 - "POST /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1/reduce/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:35376 - "GET /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1 HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.1:51118 - "GET /healthcheck HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

```

### test_bigrams_app-logs

**Error:**

```
master_url = 'http://localhost:8000'

    @nice_to_have
    @marks(10)
    @exercise("2.3.3")
    @description("bigrams app must count bigrams appearing more than once.")
    @pytest.mark.order(320)
    def test_bigrams_app(master_url):
        # Create job via API
        payload = {
            "app_name": "bigrams",
            "data_path": "./data/medium-text",
            "map_partitions": 4,
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
        assert resp.status_code in [200, 201]
        job = resp.json()
        job_id = job["job_id"]
    
        # Wait for job completion
        timeout = 100.0
        start_time = time.time()
        completed = False
    
        while time.time() - start_time < timeout:
            resp = httpx.get(f"{master_url}/jobs/{job_id}")
            assert resp.status_code == 200
            job = resp.json()
    
            if job["status"] == "completed":
                completed = True
                break
    
            time.sleep(1)
    
        assert completed, f"Job {job_id} did not complete within {timeout} seconds"
    
        result_path = os.path.join(SOLUTION_PATH, 'results', job_id, '0')
        expected_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'bigrams', '0')
        expected_alt_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'bigrams_alt', '0')
    
        # Try comparing with the primary snapshot
        try:
>           compare_out_file(result_path, expected_path)

tests/test_mapred_apps.py:160: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

result_path = './../projects/2-mapreduce/results/1c46b1cf-42c2-4f41-9be1-bada8beb0825/0'
expected_path = '/home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/bigrams/0'

    def compare_out_file(result_path, expected_path) -> bool:
        with open(result_path, "r") as f1, open(expected_path, "r") as f2:
            lines1 = sorted(line.strip() for line in f1 if line.strip())
            lines2 = sorted(line.strip() for line in f2 if line.strip())
            if lines1 != lines2:
                missing = set(lines2) - set(lines1)
                extra = set(lines1) - set(lines2)
                error_msg = f"Output mismatch between {result_path} and {expected_path}\n"
                error_msg += f"Expected {len(lines2)} lines, got {len(lines1)} lines\n"
                if missing:
                    error_msg += f"Missing {len(missing)} lines: {missing}\n"
                if extra:
                    error_msg += f"Extra {len(extra)} lines: {extra}"
>               raise AssertionError(error_msg)
E               AssertionError: Output mismatch between ./../projects/2-mapreduce/results/1c46b1cf-42c2-4f41-9be1-bada8beb0825/0 and /home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/bigrams/0
E               Expected 6 lines, got 0 lines
E               Missing 6 lines: {'is the 2', 'and the 3', 'the fox 9', 'again the 2', 'the wolves 2', 'at the 2'}

tests/utils.py:76: AssertionError

During handling of the above exception, another exception occurred:

master_url = 'http://localhost:8000'

    @nice_to_have
    @marks(10)
    @exercise("2.3.3")
    @description("bigrams app must count bigrams appearing more than once.")
    @pytest.mark.order(320)
    def test_bigrams_app(master_url):
        # Create job via API
        payload = {
            "app_name": "bigrams",
            "data_path": "./data/medium-text",
            "map_partitions": 4,
            "reduce_partitions": 1
        }
        resp = httpx.post(f"{master_url}/jobs", json=payload)
        assert resp.status_code in [200, 201]
        job = resp.json()
        job_id = job["job_id"]
    
        # Wait for job completion
        timeout = 100.0
        start_time = time.time()
        completed = False
    
        while time.time() - start_time < timeout:
            resp = httpx.get(f"{master_url}/jobs/{job_id}")
            assert resp.status_code == 200
            job = resp.json()
    
            if job["status"] == "completed":
                completed = True
                break
    
            time.sleep(1)
    
        assert completed, f"Job {job_id} did not complete within {timeout} seconds"
    
        result_path = os.path.join(SOLUTION_PATH, 'results', job_id, '0')
        expected_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'bigrams', '0')
        expected_alt_path = os.path.join(os.path.dirname(__file__), 'snapshot', 'test_mapred_apps', 'bigrams_alt', '0')
    
        # Try comparing with the primary snapshot
        try:
            compare_out_file(result_path, expected_path)
            return
        except AssertionError:
>           compare_out_file(result_path, expected_alt_path)

tests/test_mapred_apps.py:163: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

result_path = './../projects/2-mapreduce/results/1c46b1cf-42c2-4f41-9be1-bada8beb0825/0'
expected_path = '/home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/bigrams_alt/0'

    def compare_out_file(result_path, expected_path) -> bool:
        with open(result_path, "r") as f1, open(expected_path, "r") as f2:
            lines1 = sorted(line.strip() for line in f1 if line.strip())
            lines2 = sorted(line.strip() for line in f2 if line.strip())
            if lines1 != lines2:
                missing = set(lines2) - set(lines1)
                extra = set(lines1) - set(lines2)
                error_msg = f"Output mismatch between {result_path} and {expected_path}\n"
                error_msg += f"Expected {len(lines2)} lines, got {len(lines1)} lines\n"
                if missing:
                    error_msg += f"Missing {len(missing)} lines: {missing}\n"
                if extra:
                    error_msg += f"Extra {len(extra)} lines: {extra}"
>               raise AssertionError(error_msg)
E               AssertionError: Output mismatch between ./../projects/2-mapreduce/results/1c46b1cf-42c2-4f41-9be1-bada8beb0825/0 and /home/miquelvir/tmpmr/lsds-2026-101-8/lsds-2026-mapreduce-solutions/tests/snapshot/test_mapred_apps/bigrams_alt/0
E               Expected 7 lines, got 0 lines
E               Missing 7 lines: {'is the 2', 'and the 3', 'again the 2', 'the wolves 2', 'fox — 2', 'the fox 9', 'at the 2'}

tests/utils.py:76: AssertionError
```

**CAPTURED LOG CALL Logs:**

```
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: POST http://localhost:8000/jobs "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
[32mINFO    [0m httpx:_client.py:1025 HTTP Request: GET http://localhost:8000/jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 "HTTP/1.1 200 OK"
```

**Container Logs:**

```
Found 7 running containers: client, worker1, worker5, worker2, worker3, master, worker4

============================================================
CLIENT (last 50 lines)
============================================================
(no output)

============================================================
WORKER1 (last 50 lines)
============================================================
INFO:     172.18.0.1:42668 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:48118 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:48122 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER5 (last 50 lines)
============================================================
INFO:     172.18.0.1:56122 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:41082 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:41084 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER2 (last 50 lines)
============================================================
INFO:     172.18.0.3:45200 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:42516 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:55778 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:55782 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:55794 - "POST /reduce HTTP/1.1" 200 OK
INFO:     172.18.0.4:36612 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=0&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.4:36618 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=2&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.3:55796 - "POST /reduce HTTP/1.1" 200 OK
INFO:     172.18.0.4:36624 - "GET /map-output?job_id=3b289295-39ae-45e6-a65c-b9a0da1b5bc1&map_partition=0&partition=0 HTTP/1.1" 404 Not Found
INFO:     172.18.0.3:39026 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:39032 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:39048 - "POST /reduce HTTP/1.1" 200 OK
INFO:     172.18.0.4:38092 - "GET /map-output?job_id=1c46b1cf-42c2-4f41-9be1-bada8beb0825&map_partition=0&partition=0 HTTP/1.1" 404 Not Found
INFO:     172.18.0.4:38104 - "GET /map-output?job_id=1c46b1cf-42c2-4f41-9be1-bada8beb0825&map_partition=2&partition=0 HTTP/1.1" 404 Not Found
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
WORKER3 (last 50 lines)
============================================================
INFO:     172.18.0.3:32830 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:44640 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:47388 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:47404 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.4:33576 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=1&partition=0 HTTP/1.1" 200 OK
INFO:     172.18.0.4:33590 - "GET /map-output?job_id=ec6f6524-62db-45d3-83cb-175ec950189c&map_partition=3&partition=0 HTTP/1.1" 404 Not Found
INFO:     172.18.0.3:47408 - "POST /map HTTP/1.1" 200 OK
INFO:     172.18.0.3:47040 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.4:37162 - "GET /map-output?job_id=1c46b1cf-42c2-4f41-9be1-bada8beb0825&map_partition=1&partition=0 HTTP/1.1" 404 Not Found
INFO:     172.18.0.4:37176 - "GET /map-output?job_id=1c46b1cf-42c2-4f41-9be1-bada8beb0825&map_partition=3&partition=0 HTTP/1.1" 404 Not Found
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)


============================================================
MASTER (last 50 lines)
============================================================
INFO:     172.18.0.1:53888 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.1:35330 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:35342 - "GET /jobs/ec6f6524-62db-45d3-83cb-175ec950189c HTTP/1.1" 200 OK
INFO:     172.18.0.2:37494 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/1/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41178 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41192 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/2/completed HTTP/1.1" 200 OK
INFO:     172.18.0.2:37504 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/map/3/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:41196 - "POST /jobs/ec6f6524-62db-45d3-83cb-175ec950189c/reduce/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:35344 - "GET /jobs/ec6f6524-62db-45d3-83cb-175ec950189c HTTP/1.1" 200 OK
INFO:     172.18.0.1:35356 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.2:37514 - "POST /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1/map/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:35368 - "GET /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1 HTTP/1.1" 200 OK
INFO:     172.18.0.4:41212 - "POST /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1/reduce/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:35376 - "GET /jobs/3b289295-39ae-45e6-a65c-b9a0da1b5bc1 HTTP/1.1" 200 OK
INFO:     172.18.0.1:35382 - "POST /jobs HTTP/1.1" 200 OK
INFO:     172.18.0.1:35388 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:35390 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46036 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46048 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46062 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46076 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46090 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46098 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46102 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46108 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46112 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:46118 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:42656 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:42658 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:42670 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.1:42674 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
INFO:     172.18.0.6:57160 - "POST /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825/map/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.7:50428 - "POST /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825/map/1/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:57274 - "POST /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825/map/3/completed HTTP/1.1" 200 OK
INFO:     172.18.0.5:57114 - "POST /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825/map/2/completed HTTP/1.1" 200 OK
INFO:     172.18.0.4:57288 - "POST /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825/reduce/0/completed HTTP/1.1" 200 OK
INFO:     172.18.0.1:42676 - "GET /jobs/1c46b1cf-42c2-4f41-9be1-bada8beb0825 HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


============================================================
WORKER4 (last 50 lines)
============================================================
INFO:     172.18.0.1:51118 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:49678 - "GET /healthcheck HTTP/1.1" 200 OK
INFO:     172.18.0.3:49684 - "POST /map HTTP/1.1" 200 OK
[STDERR] INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)

```

