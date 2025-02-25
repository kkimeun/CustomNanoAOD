# CustomNanoAOD
---

## Enviroment setting
for RunII, should use CMSSW\_10\_6\_27.
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
scram p -n SKNanoMaker_CMSSW_10_6_27 CMSSW CMSSW_10_6_27
cd SKNanoMaker_CMSSW_10_6_27/src
cmsenv
```

## Adding custom variables
For example, if you want to change the electron varible, check `PhysicsTools/NanoAOD/python/electrons_cff.py`.
```bash
cd $CMSSW_BASE/src
git cms-init
git cms-merge-topic choij1589:from-CMSSW_10_6_27 # Run2
scram b clean; scram b -j 8
```

Get automized scripts:
```bash
mkdir -p Configuration && cd Configuration
git clone git@github.com:choij1589/CustomNanoAOD.git
```

## Runnin cmsDriver.py
```bash
./scripts/runCMSDriver.sh MC_2017 # or DATA_2016preVFP
```
It will create `configs/CustomNano_MC_2017_cfg.py`

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
