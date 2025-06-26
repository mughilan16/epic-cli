from core.cli.args import Args

args = [
    # Args("-h", "--help", "help", "List and provider description for all the command"), 
    Args("-p", "--prefix", "Prefix of the project", required=True),
    Args("-j", "--jobno", "Job Number of the project", required=True),
    Args("-u", "--upload",  "Upload", "bool", default=True),
    Args("-f", "--filecollection", "File Collection", "bool"), 
]

