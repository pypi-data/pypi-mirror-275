# qcentroid-agent-cli

![deploy to pypi](https://github.com/QCentroid/qcentroid-agent-cli/actions/workflows/publish.yml/badge.svg)
[![Python](https://img.shields.io/pypi/pyversions/qcentroid-agent-cli.svg)](https://badge.fury.io/py/qcentroid-agent-cli)
[![PyPI](https://badge.fury.io/py/qcentroid-agent-cli.svg)](https://badge.fury.io/py/qcentroid-agent-cli)
 [![CodeFactor](https://www.codefactor.io/repository/github/qcentroid/qcentroid-agent-cli/badge)](https://www.codefactor.io/repository/github/qcentroid/qcentroid-agent-cli)
 
Client library to interact with QCentroid Agent API.



## Functions


Functions:
* obtain status, and context
* obtain input data 
* send output data
* set status
* send execution logs

## Install

```bash
pip install qcentroid-agent-cli
```


## Use

### Simple example

As easy as this:

```python
from qcentroid_agent_cli import QCentroidSolverClient
import logging

logging.basicConfig(level=logging.DEBUG)
API_BASE_URL="https://api.qcentroid.xyz"
SOLVER_API_KEY="1234-4567-8910"  # Get your solver API_KEY in the platform dashboard
SOLVER_ID="123"

def main():
    
    # Get the solver details
    solver = QCentroidSolverClient(API_BASE_URL, SOLVER_API_KEY, SOLVER_ID)

    print(f"currentVersion:{QCentroidSolverClient.getVersion()}")

    # Request a queued job
    job = solver.obtainJob()
    
    # Notify start of job execution
    job.start()
    
    # Retrieve the job input data
    input_data = job.obtainInputData()
    output_data = {} 

    #
    # TODO: Add your solver code here and generate output_data
    #

    # Send the solver output data and execution logs to the platform
    job.sendOutputData(output_data)
    job.sendExecutionLog(logs)

    # End of job execution
    
    
if __name__ == "__main__":
    main() 
```

### Basic example with env variables

You can use environment variables to pass the credentials:
```bash
export QCENTROID_PUBLIC_API="https://xxxx.xxx.xxx"
export QCENTROID_AGENT_API_TOKEN="xxxx-yyyy-zzzzz"
export QCENTROID_SOLVER_ID="KJHFDKSFDG"
python main.py
```

main.py python example with env variables:
```python
from qcentroid_agent_cli import QCentroidSolverClient
...
solver = QCentroidSolverClient() #No paramethers needed
...
```


### Dotenv Basic example

Also can be used dotenv to load properties:
```bash
pip install dot-env
```

.env:
```
QCENTROID_PUBLIC_API="https://xxxx.xxx.xxx"
QCENTROID_AGENT_API_TOKEN="xxxx-yyyy-zzzzz"
QCENTROID_SOLVER_ID="KJHFDKSFDG"
```

```python
from dotenv import load_dotenv
from qcentroid_agent_cli import QCentroidSolverClient
...
load_dotenv()
solver = QCentroidSolverClient() #No paramethers needed
```

#### Advanced Agent example

Simple all-in-one python example:
```python
import requests
from qcentroid_agent_cli import QCentroidSolverClient
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
API_BASE_URL="https://api.qcentroid.xyz"
SOLVER_API_KEY="1234-4567-8910"  # Get your solver API_KEY in the platform dashboard
SOLVER_ID="123"

def main():
    exit = False
    print("QCentroid Agent usage example")
    print("Starting...")
    
    # Initialize the agent and get the solver details and a valid access token
    solver = QCentroidSolverClient(API_BASE_URL, SOLVER_API_KEY, SOLVER_ID)

    print("Solver initialization successful.")

    # Loop to request queued jobs until any exit condition you want to set
    while not exit:
        try:
            print("Checking for pending jobs...")
            # Request a queued job (the oldest one will be returned)
            job = solver.obtainJob()

            if job :
                print("New job received.")
                # There is a job to be processed!
                try:
                    print("Processing job...")
                    # Notify the platform we're starting to process this job
                    job.start()
                    # Retrieve the input data
                    input_data = job.obtainInputData()
                    output_data = {} 
                    
                    #
                    # TODO: add your solver code here and generate output_data
                    #

                    print("Job processed successfully.")
                    # Send the solver output data to the platform
                    job.sendOutputData(output_data)
                    # Send the solver execution logs to check them thorugh the platform dashboard
                    # TODO: job.sendExecutionLog(logs)
                    
                    job.end()              
                except Exception as e:
                    # Job execution has failed, notify the platform about the error
                    print("Error during job execution.")
                    job.error(e)

            else:        
                # No queued jobs. Wait for 1 minute and check again
                print("No pending jobs. Waiting for 1 minute...")
                time.sleep(60)
            
        except requests.RequestException as e:
            # Error in an API request
            # Whether parameters are incorrect (URL, api-key or solver_id), or there are connectivity issues
            print(f"QCentroid Agent: API request failed: {e}")
            exit=True
            
        except Exception as e:
            # Any other errors
            print(f"QCentroid Agent error: {e}")
            exit=True
            
    print("End.")


if __name__ == "__main__":
    main()

```
### Own component development


## Versioning

Update manually on main the `pyproject.toml` the `version` field to match the next release tag. Launch a [new version on Releases](https://github.com/QCentroid/qcentroid-agent-cli/releases/new) section selecting a new tag matching the version. Create the release. The release will be published on pypi.org


## Debuging locally

```bash
pip install . #install the current version of the component

python main.py #run the client version that uses the package
```

## Commits


```bash
pip install pre-commit
pre-commit install # add pre-commit hook
... # modify the code
git add . #add modified files
git commit -m"some modifications" # pre-commit will be triggered to check code format
```

