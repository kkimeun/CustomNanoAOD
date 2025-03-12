#!/bin/bash
cmsDriver.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step NANO --scenario pp --era Run3_2023 --python_filename test_cfg.py  --filein "file:00016e4c-72ec-40bc-9cf3-33dc1afe5c8a.root" --fileout "file:NANOAOD.root" --no_exec --mc -n 100
