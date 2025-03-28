#!/bin/bash

while read task; do
  echo "===== Status for $task ====="
  cat $task/crab_status.log
  echo ""
done < unfinished_tasks.txt
