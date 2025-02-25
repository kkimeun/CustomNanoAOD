#!/bin/bash
# Read input, for example MC_2017, DATA_2018
input=$1

# Get globalTag and eraString, which is stored in scripts/${input}.txt
globalTag=$(sed -n '1p' "scripts/${input}.txt")
eraString=$(sed -n '2p' "scripts/${input}.txt")
echo "globalTag: $globalTag"
echo "eraString: $eraString"

# Validate globalTag and eraString were found
if [[ -z "$globalTag" || -z "$eraString" ]]; then
    echo "Configuration not found for $prefix $era"
    exit 1
fi

if [[ "$input" == DATA* ]]; then
    cmsDriver.py --eventcontent NANOAOD --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000" \
    --datatier NANOAOD --conditions ${globalTag} --step NANO --era ${eraString} --python_filename configs/CustomNano_${input}_cfg.py \
    --filein "file:dummy.root" \
    --fileout "file:NANOAOD.root" --no_exec --data -n -1 || exit $? ;
elif [[ "$input" == MC* ]]; then
    cmsDriver.py --eventcontent NANOAODSIM --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000" \
    --datatier NANOAODSIM --conditions ${globalTag} --step NANO --era ${eraString} --python_filename configs/CustomNano_${input}_cfg.py \
    --filein "file:dummy.root" \
    --fileout "file:NANOAOD.root" --no_exec --mc -n -1 || exit $? ;
fi

# Remove "file:dummy.root" from the config
sed -i "s/'file:dummy.root'//g" configs/CustomNano_${input}_cfg.py
