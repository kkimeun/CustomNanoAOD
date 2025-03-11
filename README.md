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

# To do
- [ ] Automatically check crab status and resubmit failed jobs

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
