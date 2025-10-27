# Python Beyond Decorators

This repo is for deep understanding and leaning building restful apis using flask 

## Requirements

- Python `3.8+`, `virtualenv`
- Please refer `requirements.txt` for installed package information 

## Installation 

1. Clone the repository:

```sh
git clone https://github.com/jitendra01mishra/python_beyond_decorators.git
cd python_beyond_decorators
```

2. create a virtual environment, go to `python_beyond_decorators` and run the following command.

- **Windows**:
  ```sh
    py -m virtualenv .venv
  ```
- **macOS / Linux**:
    ```sh
        python3 -m virtualenv .venv
    ```

3. Before you can start intalling or using package in your virtual environment you'll need to activate it.

- **Windows**
    ```sh 
        .venv\Scripts\activate
    ```
- **macOS / Linux**:
    ```sh 
        source .venv/bin/activate 
    ```

4. Install the requirement dependencies using pip3:

```sh
    pip3 install -r requirements.txt
```

5. if you wish to switch the project or leave your virtual environment, deactivate the environment:
    ```sh
        deactivate
    ```

## Linting and Formatting 

refer `PIP8` for formatting and linting issues 

Run `flake8 --exclude=.venv` to verify the linting issues in your python code.

Run `.venv/bin/mdformat README.md` to automatically resolve most errors flagged by the linter in `README.md`.
