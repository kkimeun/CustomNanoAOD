from CRABClient.UserUtilities import config, getUsername

config = config()
### General configuration
config.General.workArea        = "crab_projects"
config.General.requestName     = "MC_2017_TTToHcToWAToMuMu_MHc-100_MA-15_MultiLepFilter_TuneCP5_13TeV-madgraph-pythia8"
config.General.transferOutputs = True
config.General.transferLogs    = False

### JobType configuration
config.JobType.psetName        = "/d0/scratch/choij/SKNanoMaker_Run2_CMSSW_10_6_27/src/Configuration/CustomNanoAOD/configs/CustomNano_MC_2017_cfg.py"
config.JobType.pluginName      = 'Analysis'
config.JobType.allowUndistributedCMSSW = False

### Data configuration
config.Data.inputDataset       = "/TTToHcToWAToMuMu_MHc-100_MA-15_MultiLepFilter_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM"
config.Data.lumiMask           = ""
config.Data.inputDBS           = 'global'
config.Data.splitting          = 'FileBased'
config.Data.unitsPerJob        = 1
config.Data.outLFNDirBase      = "store/user/%s/SKNano" % getUsername()
config.Data.publication        = False

### Site configuration
config.Site.storageSite       = 'T3_KR_KNU'
