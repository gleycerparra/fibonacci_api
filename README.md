# Fibonacci REST API

This project is a simple REST API built with Python's FastAPI framework. The API has a single endpoint that returns the nth Fibonacci number when provided with an index `n`.

## API Endpoint

- `GET /fibonacci/{n}`: Returns the nth Fibonacci number.

## Setup and Installation

To setup and install the project, follow these steps:

1. Clone the repository.

```bash
git clone https://github.com/gleycerparra/fibonacci_api
```

2. Navigate to the project directory.

```bash
cd fibonacci_api
```

3. Create and activate a virtual environment.

```bash
python -m venv fib_api_env
source fib_api_env/bin/activate  # On Windows, use `activate while being in the project folder`
```

4. Install the requirements.

```bash
pip install -r requirements.txt
```

5. Run the server.

```bash
uvicorn main:app --reload
```

The API is now up and running at `http://localhost:8000`.

## Usage

To get the nth Fibonacci number, send a GET request to `http://localhost:8000/fibonacci/{n}` where `{n}` is the index of the Fibonacci number you want to get.

## Implementation

The Fibonacci sequence is implemented using a simple recursive function. The base cases are when `n` is 0 or 1, in which case the function returns `n`. For any other `n`, the function calls itself twice: once with `n - 1` and once with `n - 2`, and adds the results.

## Future Optimizations

This Fibonacci function is not optimized for large inputs because it uses a simple recursive implementation. This leads to a lot of repeated computation when calculating larger Fibonacci numbers. In future versions, this could be improved by implementing memoization or an iterative solution.

---

Feel free to modify this README as necessary to fit the specifics of your project. Remember, a good README should provide all the necessary information someone would need to understand your project and get it running on their own system.