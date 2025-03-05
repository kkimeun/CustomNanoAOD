from CRABClient.UserUtilities import config, getUsername

config = config()
### General configuration
config.General.workArea        = 'crab_projects'
config.General.requestName     = 'PostProcTest'
config.General.transferOutputs = True
config.General.transferLogs    = False

### JobType configuration
config.JobType.psetName        = 'test_cfg.py'
config.JobType.scriptExe       = 'run_chained.sh'
config.JobType.scriptArgs      = []
config.JobType.inputFiles      = ['run_chained.sh', 'test_cfg.py', 'keep_and_drop.txt']
config.JobType.outputFiles     = ['NANOAOD_Skim.root']
config.JobType.pluginName      = 'Analysis'
config.JobType.allowUndistributedCMSSW = False

### Data configuration
config.Data.inputDataset       = '/TTToHcToWAToMuMu_MHc-100_MA-15_MultiLepFilter_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM'
config.Data.lumiMask           = ''
config.Data.inputDBS           = 'global'
config.Data.splitting          = 'FileBased'
config.Data.unitsPerJob        = 1
config.Data.outLFNDirBase      = 'store/user/%s/SKNano_PostProcessTest' % getUsername()
config.Data.publication        = False

### Site configuration
config.Site.storageSite       = 'T3_KR_KNU'
