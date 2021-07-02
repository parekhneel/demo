import subprocess

def fetch_version_hash() -> str:
	'''
	Get the current commit version of the current branch being used. 

	Returns
	-------
	commit_hash: str
	'''
	commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf8").strip("\n")
	return commit_hash

