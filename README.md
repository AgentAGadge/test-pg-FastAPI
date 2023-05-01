# test-pg-FastAPI

This is a test project for a FastAPI app that showcases how to create a simple API as well as features such as asynchronous logging to file, unit test, CI for GitHub, etc.

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Usage

Start the FastAPI app with the following command:
```bash
uvicorn src.main:app --reload
```

The app will then be available at `http://localhost:8000/`.

# API

### `GET /`

Returns a welcome message.

#### Example Request

```http
GET http://localhost:8000/
```

#### Example Response

```json
{
    "message": "Welcome to the root of test-pg-FastAPI."
}
```


## Addition

### GET `/addition/addone/{addend}`

This route adds 1 to a float number provided in the URL parameter `addend`. 

#### Parameters

* `addend` (float): The number to which 1 should be added.
* `method` (string): The computation method to use. Can be either `python`, `numpy` or `tp_package`. (default: `python`)
**Query parameters:**

Parameter | Type | Description | Default
--------- | ---- | ----------- | -------
`addend` | float | A float value to which 1 should be added. | -
`method` | enum | A string value that specifies the method used to compute the addition. Possible values: `python`, `numpy`, `tp_package`. | `python`

**Response codes:**

Code | Description | Response
---- | ----------- | --------
200  | Success     | `{"sum": float}`
422  | Invalid parameters | `{"detail": str}`

#### Example

Request:
```
GET http://localhost:8000/addition/addone/42?method=numpy
```

Response:
```json
{
    "sum": 43.0
}
```

# Logging

This app uses a custom logger that is set up to be compatible with the asynchronous nature of FastAPI. By default, the logger will write logs to a file located at `logs/log.log`. The logs are also rotated daily.

To change the logger configuration, update the `config/logger_config.json` file. The app will use the `logger_config.json` file to configure the logger at startup.

# Continuous Integration

The CI includes two linters (pylint, flake8) and unit tests (pytest).
## Running the CI

To run the CI, run the following script:

```bash
    scripts/ci-on_pr_main.sh
```

## Github template

In the <code>.github</code> folder, several templates are pre-configured to ease contribution and reports in the repository:
- a pull request template, reminding the various step to ensure a qualitative request,
- issue templates, to guide reporters on how to write a useful issue. "User story" and "bug" template are availables.