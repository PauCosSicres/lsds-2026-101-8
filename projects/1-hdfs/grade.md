# LSDS Project 1 Grade


| Type      | % | Grade            |
|-----------|-----|----------------|
| Essential (^)     | 40%  | 10.0/10 |
| Nice-to-haves (^^)       | 30%  | 8.61/10 |
| Difficult (^^^)   | 30%  | 8.82/10 |
| **Subtotal**   | **100%**  | **92.0**/100 |
| Advanced (^^^^)   | +1.5/10  | 0.0/15 |
| **Total**   | **100% + 1.5**  | **9.0**/10 |

## Breakdown

### Essentials (^)

| Exercise | Test case | Description | Submitted | Max marks | Marks |
| -------- | --------- | ----------- | --------- | --------- | ----- |
| 1.2.1 | test_healthcheck_status | namenode /healthcheck must return status 200. | Yes | 1 | 1 |
| 1.2.1 | test_healthcheck_body | namenode /healthcheck must return {"status": "up"} | Yes | 1 | 1 |
| 1.2.2 | test_datanodes_status | /datanodes must respond with 200 OK. | Yes | 1 | 1 |
| 1.2.2 | test_datanodes_content | /datanodes must return the exact list of datanodes from settings.json. | Yes | 5 | 5 |
| 1.2.3 | test_create_file_200 | POST /files must return 200 OK when creating a new file. | Yes | 5 | 5 |
| 1.2.3 | test_create_file_duplicate | Creating a file twice must return 409. | Yes | 5 | 5 |
| 1.2.4 | test_get_file_status | GET /files/{filename} must return 200 for an existing file. | Yes | 5 | 5 |
| 1.2.4 | test_get_file_not_found | GET /files/{filename} for an unknown file must return 404. | Yes | 3 | 3 |
| 1.2.5 | test_add_block_200 | POST /files/{filename}/blocks should return 200 for valid file. | Yes | 5 | 5 |
| 1.2.5 | test_add_block_structure | After adding first block, it must appear in the file's block list. | Yes | 5 | 5 |
| 1.2.5 | test_add_block_missing_file | Adding a block to a non-existent file must return 404. | Yes | 1 | 1 |
| 1.2.5 | test_round_robin | Round-robin placement must rotate replicas across datanodes in order 1 → 2 → 3 → 1 → ... | Yes | 5 | 5 |
| 1.3.1 | test_datanode1_healthcheck | /healthcheck must return 200 OK and {"status": "up"} for DataNode 1. | Yes | 1 | 1 |
| 1.3.1 | test_datanode2_healthcheck | /healthcheck must return 200 OK and {"status": "up"} for DataNode 2. | Yes | 1 | 1 |
| 1.3.1 | test_datanode3_healthcheck | /healthcheck must return 200 OK and {"status": "up"} for DataNode 3. | Yes | 1 | 1 |
| 1.3.2 | test_write_block_datanode1 | PUT /files/{filename}/blocks/{block_number} must store the block on disk. | Yes | 5 | 5 |
| 1.3.3 | test_read_block_datanode1 | GET /files/{filename}/blocks/{block_number} must return the correct block content. | Yes | 5 | 5 |
| 1.3.3 | test_read_block_not_found | GET /files/{filename}/blocks/{block_number} must return 404 if block does not exist. | Yes | 1 | 1 |

### Nice to haves (^^)

| Exercise | Test case | Description | Submitted | Max marks | Marks |
| -------- | --------- | ----------- | --------- | --------- | ----- |
| 1.2.6 | test_delete_file_204 | DELETE /files/{filename} should return 204 for existing file. | Yes | 1 | 1 |
| 1.2.6 | test_delete_file_404 | DELETE /files/{filename} should return 404 after the file was already deleted. | Yes | 5 | 5 |
| 1.4.1 | test_client_list_datanodes | Client lists all datanodes correctly | Yes | 5 | 5 |
| 1.4.2 | test_client_upload_file | Client uploads a file correctly | Yes | 5 | 5 |
| 1.4.2 | test_client_upload_file_replicas | All datanodes have replicas of the blocks | Yes | 5 | 5 |
| 1.4.3 | test_client_download_file | Client downloads a file correctly | Yes | 10 | 10 |
| 1.4.4 | test_client_upload_download_failover | Client upload/download failover is implemented correctly. | Yes | 5 | 0 |

### Difficult (^^^)

| Exercise | Test case | Description | Submitted | Max marks | Marks |
| -------- | --------- | ----------- | --------- | --------- | ----- |
| 1.2.7 | test_journal | The journal must track namespace operations. | Yes | 7 | 5 |
| 1.3.4 | test_write_pipeline | DataNode must support write pipelines and forward blocks to the next DataNode. | Yes | 10 | 10 |

### Advanced (^^^^)

| Exercise | Test case | Description | Submitted | Max marks | Marks |
| -------- | --------- | ----------- | --------- | --------- | ----- |
| 1.3.5 | test_namenode_block_report_api | The NameNode exposes an API endpoint to receive block reports from DataNodes. | No | 5 | 0 |
| 1.3.5 | test_namenode_blocks_to_remove | The NameNode responds to block reports with a list of blocks that should be removed. | No | 10 | 0 |
| 1.3.5 | test_datanode_removes_blocks | A DataNode removes all blocks that have been indicated for deletion by the NameNode. | No | 5 | 0 |
| 1.3.6 | test_namenode_tracks_blocks_per_datanode | The NameNode keeps track of which blocks are stored in each DataNode. | No | 5 | 0 |
| 1.3.6 | test_underreplicated_blocks_added_to_queue | Underreplicated blocks are added to the replication queue by the NameNode. | No | 10 | 0 |
| 1.3.6 | test_namenode_instructs_replication_of_underreplicated_blocks | The NameNode instructs DataNodes to replicate underreplicated blocks they own to other DataNodes in the next block report response. | No | 10 | 0 |
| 1.3.7 | test_namenode_tracks_last_block_report | Check that the NameNode keeps track of the last time each DataNode sent a block report. | No | 5 | 0 |
| 1.3.7 | test_missing_blocks_added_to_replication_queue | Check that the NameNode adds missing blocks from a down DataNode to the replication queue. | No | 5 | 0 |

## Comments

Good work! The journal is a WAL, so you should append to it BEFORE updating the image.

