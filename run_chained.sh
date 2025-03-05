#!/bin/bash

export PATH=$CMSSW_BASE/bin/slc7_amd64_gcc700:$PATH

echo "Starting cmsRun with test_cfg.py to produce NANOAOD.root..."
cmsRun -j FrameworkJobReport.xml -p test_cfg.py
if [ $? -ne 0 ]; then
    echo "cmsRun failed. Exiting."
    exit 1
fi

ls -l
echo "Running nano_postproc.py..."
nano_postproc.py $PWD NANOAOD.root --bi keep_and_drop.txt
if [ $? -ne 0 ]; then
    echo "nano_postproc.py failed. Exiting."
    exit 1
fi

echo "Chained job finished successfully."
