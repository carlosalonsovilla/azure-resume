# Carlos Villa Azure Cloud Resume Challenge
Live Site: https://www.carlosalonsovilla.com

## Prerequisites

- [GitHub account](https://github.com/join)
- [Azure account](https://azure.microsoft.com/en-us/free)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Python](https://learn.microsoft.com/en-us/azure/developer/python/)
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash#install-the-azure-functions-core-tools)
- [Visual Studio Code](https://code.visualstudio.com)
- [Visual Code Extensions](https://code.visualstudio.com/docs/introvideos/extend)
  - [Azure Functions Extensions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
  - [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Azure Storage Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestorage)

## Front-end resources

The front-end is a static website built with HTML, CSS, and JavaScript, deployed on Azure Blob Storage. It includes a visitor counter that is fetched via an API call to an Azure Function.

**Local Development**

- Clone the repository
- Update your HTML, CSS, and JavaScript files for your resume site
- The visitor counter is fetched using JavaScript via a call to the backend API

**Deploying the Frontend**

- Use the VS code extenstion to upload and deploy the frontend to Blob Storage


**Testing the Frontend**

- Implmenedted frontend testing using Selenium and Chromedriver. The test validates the page title and the visitor counter is present
- Run locally and ensure the page behaves as expected

  
## Back-end resources

The back-end is an HTTP-triggered Azure Function that connects to Cosmos DB. The function increments a visitor count each time it's triggered and returns the updated count.

**Azure Functions**

- Created a python-based Azure function, which connects to Cosmos DB using environment varialbes
- The function retrieves a document from Cosmos DB, increments the visitor counter, and writes it back to the database
- Ensure CORS is enabled in the Function API settings

**Environment Variables**

- Sensitive data such as Cosmos DB keys and connection strings are stored in environment variables. These are configured both locally (via .env files) and in Azure (via the Function App settings)

**Testing the Backend**

- Backend API testing was done using Python's unittest and requests modules. The test checks that the API responds with a 200 status code and that the response contains the expected count value
- Secure API testing is done by fetching the API URL and keys from environment variables instead of hardcoding them in the test scripts

## Testing Resources

Testing is crucial for ensuring the correctness of both the front-end and back-end.

**Frontend Testing**

- Selenium was used for automated testing. The test checks the correct title is displayed and the counter is present

**Backend Testing**

- Python's unittest was used to test the API. The test verifies a successful 200 response and the API returns a valid count from Cosmos DB

**Environment Variables**

- .env files store sensitive data such as API keys and URLS for both the backend and frontend
- The files are not pushed to GitHub
  
