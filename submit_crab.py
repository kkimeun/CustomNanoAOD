import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inputDataset", "-i", type=str, default="", help="input dataset as DBS name")
parser.add_argument("--inputList", "-l", type=str, default="", help="list of input dataset list, in textfile")
parser.add_argument("--workArea", "-a", type=str, default="crab_projects", help="name of crab work area")
parser.add_argument("--pilot", action="store_true", default=False)
args = parser.parse_args()

## Check if arguments are valid
if args.inputDataset and args.inputList:
    raise ValueError("Both inputDataset and inputList are given. Please choose one")
elif args.inputDataset:
    print(f"Running on dataset: {args.inputDataset}")
elif args.inputList:
    print(f"Running on dataset list: {args.inputList}")
else:
    raise ValueError("No input dataset is given")

def parseDatasetList(inputList):
    with open(inputList, 'r') as f:
        datasets = f.readlines()
    datasets = [d.strip() for d in datasets]
    datasets = [d for d in datasets if d] # Remove empty lines
    datasets = [d for d in datasets if not d.startswith("#")] # Remove comments
    return datasets

def getRequestInfoFrom(dataset):
    prefix = ""
    lumiMask = ""
    if "RunIISummer20UL16MiniAODAPVv2" in dataset:
        prefix = "MC_2016preVFP"
    elif "RunIISummer20UL16MiniAODv2" in dataset:
        prefix = "MC_2016postVFP"
    elif "RunIISummer20UL17MiniAODv2" in dataset:
        prefix = "MC_2017"
    elif "RunIISummer20UL18MiniAODv2" in dataset:
        prefix = "MC_2018"
    elif "HIPM_UL2016_MiniAODv2" in dataset:
        prefix = "DATA_2016preVFP"
        lumiMask = "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16.json"
    elif "UL2016_MiniAODv2" in dataset:
        prefix = "DATA_2016postVFP"
        lumiMask = "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16.json"
    elif "UL2017_MiniAODv2" in dataset:
        prefix = "DATA_2017"
        lumiMask = "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.json"
    elif "UL2018_MiniAODv2" in dataset:
        prefix = "DATA_2018"
        lumiMask = "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.json"
    else:
        raise ValueError(f"Cannot parse era from dataset: {dataset}")
    
    if "MC" in prefix:
        request_name = f"{prefix}_{dataset.split('/')[1]}"
    else:
        info = dataset.split('/')
        request_name = f"{prefix}_{info[1]}_{info[2].split('-')[0]}"
    print("Dataset:", dataset)
    print("prefix:", prefix)
    print("lumiMask:", lumiMask)
    print("Request name:", request_name)
    return prefix, lumiMask, request_name


if args.inputDataset:
    # Create project directory and copy the crab configuration file
    print("Submitting CRAB job for dataset:", args.inputDataset)
    prefix, lumiMask, request_name = getRequestInfoFrom(args.inputDataset)
    if lumiMask is None:
        lumiMask = ""
    BASEDIR = os.getcwd()
    WORKDIR = f"{BASEDIR}/CRAB/{request_name}"
    os.makedirs(WORKDIR, exist_ok=True)
    os.chdir(WORKDIR)

    with open(f"{BASEDIR}/templates/crab_config.py", "r") as f:
        template = f.read()
    template = template.replace("[WORKAREA]", "crab_projects")
    template = template.replace("[REQUESTNAME]", request_name)
    template = template.replace("[PSETNAME]", f"{BASEDIR}/configs/CustomNano_{prefix}_cfg.py")
    template = template.replace("[INPUTDATASET]", args.inputDataset)
    template = template.replace("[LUMIMASK]", lumiMask)
    
    with open(f"{WORKDIR}/crab_config.py", "w") as f:
        f.write(template)

    os.system("crab submit -c crab_config.py")



exit()

if args.inputDataset:
    print("Submitting CRAB job for dataset:", args.inputDataset)
    prefix, lumiMask, request_name = getRequestInfoFrom(args.inputDataset)
    config.General.requestName = request_name
    config.JobType.psetName = f"configs/CustomNano_{prefix}_cfg.py"
    config.Data.inputDataset = args.inputDataset
    config.Data.lumiMask = lumiMask
    print(config)
    crabCommand('submit', config=config)

if args.inputList:
    datasets = parseDatasetList(args.inputList)
    if args.pilot:
        datasets = datasets[:1]
    for dataset in datasets:
        print("Submitting CRAB job for dataset:", dataset)
        prefix, lumiMask, request_name = getRequestInfoFrom(dataset)
        config.General.requestName = request_name
        config.JobType.psetName = f"configs/CustomNano_{prefix}_cfg.py"
        config.Data.inputDataset = dataset
        config.Data.lumiMask = lumiMask
        crabCommand('submit', config=config)
