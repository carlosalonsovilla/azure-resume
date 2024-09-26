# Your backend lives here

This folder contains the backend code for the resume counter, built using Azure Functions and CosmosDB. 

## Files:
- `api/`: Contains the main function app code, including the function app Python code, settings, and required files.
- `requirements.txt`: Lists the necessary dependencies for the Python app.
- `tests/`: Placeholder for any future tests.

## Setup

### Local Development

1. Clone the repository.
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. Install the required dependencies:
    ```bash
    pip install -r api/requirements.txt
    ```

### Deployment
- The Azure Functions app is configured to use environment variables for CosmosDB credentials and connection details. Be sure to set those correctly in your Azure portal.

## Environment Variables and Deployment

During the deployment process, I encountered issues with environment variables in the Azure Functions app. The resolution involved:

- Disabling Oryx remote builds in the Azure Function App by setting `scm-do-build-during-deployment: false` and `enable-oryx-build: false`.
- Packaged all Python dependencies locally using:
  ```bash
  pip install --target=".python_packages/lib/site-packages" -r requirements.txt



