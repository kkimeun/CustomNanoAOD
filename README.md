# CustomNanoAOD
---

## Enviroment setting
for RunII, use CMSSW\_10\_6\_27.
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
scram p -n SKNanoMaker_RunII_CMSSW_10_6_27 CMSSW CMSSW_10_6_27
cd SKNanoMaker_CMSSW_10_6_27/src
cmsenv
```

for Run3, use CMSSW\_13\_0\_10.
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=el8_amd64_gcc11
scram p -n SKNanoMaker_Run3_CMSSW_13_0_10 CMSSW CMSSW_13_0_10
cd SKNanoMaker_Run3_CMSSW_13_0_10/src
cmsenv
```

## Adding custom variables
For example, if you want to change the electron varible, check `PhysicsTools/NanoAOD/python/electrons_cff.py`.
```bash
cd $CMSSW_BASE/src
git cms-init
git cms-merge-topic choij1589:from-CMSSW_10_6_27 # Run2
git cms-merge-topic choij1589:from-CMSSW_13_0_10 # Run3
```
# for post process, not strictly needed
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools

# always clean and build
scram b clean; scram b -j 8
```

Get automized scripts:
```bash
mkdir -p Configuration
git clone git@github.com:choij1589/CustomNanoAOD.git Configuration/CustomNanoAOD
```

## Running cmsDriver.py
To process MiniAOD to NanoAOD, trun `cmsDriver.py`.
```bash
./scripts/runCMSDriver.sh $PREFIX # MC_2017 / DATA_2016preVFP
```
It will create `configs/CustomNano_$PREFIX_cfg.py`

## Preparing crab submission scripts
```bash
python3 prepare_crab_submission.py -i $DASFILENAME     # submitting single file
python3 prepare_crab_submission.py -l $FILELIST.txt    # submitting list of files, seperated by line
```
The command will print out submission commands. Follow the instructions to submit the crab jobs. Example of filelist can be found in `SampleLists/`

# Test
## Submitting jobs to crab
```bash
source /cvmfs/cms.cern.ch/crab3/crab.sh
python3 crab_config.py -i $DASFILENAME     # submitting single file
python3 crab_config.py -l $FILELIST.txt    # submitting list of files, seperated by name
```
See SampleLists for example

## Skimming
**Need Update**
You can use `nano_postproc.py` to skim the nanoAOD files. Check the `keep_and_drop.txt` for the variables you want to keep or drop.
```bash
export PATH=$CMSSW_BASE/bin/slc7_amd64_gcc700:$PATH
nano_postproc.py $PWD NANOAOD.root -b keep_and_drop.txt 
```

## Sources
- [2022\_MC](https://cms-pdmv-prod.web.cern.ch/mcm/requests?produce=%2FDYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8%2FRun3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2%2FNANOAODSIM&page=0&shown=127)
- [2022EE\ MC](https://cms-pdmv-prod.web.cern.ch/mcm/requests?produce=%2FDYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8%2FRun3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2%2FNANOAODSIM&page=0&shown=127)
- [2023\_MC](https://cms-pdmv-prod.web.cern.ch/mcm/requests?produce=%2FDYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8%2FRun3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3%2FNANOAODSIM&page=0&shown=127)
- [2023BPix\_MC](https://cms-pdmv-prod.web.cern.ch/mcm/requests?produce=%2FDYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8%2FRun3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1%2FNANOAODSIM&page=0&shown=127)
