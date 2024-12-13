# Contributing

If you think there's a bug or a feature that might be useful to add, we're pleased to accept any contribution!

Probably you've never made a commit before, so here's a quick guide of how we manage the repository. 

## How to contribute

### Setting up the work environment

First of all, it is good practice to properly set up your workspace. To download and edit the code, follow these steps:

1. Fork the repository:
    - To the top right of the project's main page, you can fork the project. This will create an exact copy of the project in your account. 
    - you can download the fork directly from your account as a zip, extract it and cd through your Powershell/Bash to the directory of the extracted folder. 
2. Set up the virtual environment: We advise against using your global python environment, for there might be some packages that don't work with the project's dependencies. To prevent conflicts, we reccoment using a virtual environment to keep dependencies organized and prevent conflicts. 
    1. Create the virtual environment, in Windows or Linux:
    ```bash
    python -m venv venv
    ```
    2. Activate the Virtual Environment: you will find a (venv) on the left of the shell prompt.
    ```bash
    venv\Scripts\activate
    ```

    3. Install the required Dependencies: We listed all required dependencies in the requirement text file. On the shell in the project's directory, type:
     ```bash
    pip install -r requirements.txt
    ```

    4. Install the package in Editable Mode: to actually install the package, you can install it in editable mode by typing in the prompt (remember to be in the project's folder):
     ```bash
    pip install -e .
    ```

## Code documentation and Pull requests.

### Add new features

If you want to propose a new feature or work on one proposed idea, comment or create an issue on the issues section of the main project's page. The owner or a moderator will then assign to you the project.

To document a new feature, use type hints and docstrings below the function where you explain briefly what the functions do, which parameters the function takes and the expected output. see the filter negative in filters.py to have an example. 

After you saved and commited , you can request a PR (Pull Request) to request that your code is included in the main codebase. If the requirements are met, the request will be approved and merged. 

### Add Tests
Coming soon

### Add Examples
Coming soon





