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

We need to install PhysicsTools/NanoAOD and PhysicsTools/NanoAODTools.
```bash
cd $CMSSW_BASE/src
git cms-init
git cms-addpkg PhysicsTools/NanoAOD
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
scram b clean; scram b -j 8
```

## Adding custom variables
For example, if you want to change the electron varible, check `PhysicsTools/NanoAOD/python/electrons_cff.py`.


## Skimming
You can use `nano_postproc.py` to skim the nanoAOD files. Check the `keep_and_drop.txt` for the variables you want to keep or drop.
```bash
export PATH=$CMSSW_BASE/bin/slc7_amd64_gcc700:$PATH
nano_postproc.py $PWD NANOAOD.root -b keep_and_drop.txt 
```

## Submitting jobs to crab
