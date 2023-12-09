# OpenAI Chat CLI Project

This project is a simple command-line interface for having a conversation with OpenAI's GPT-4 model.

## Requirements

- Python 3.8 or higher
- (Optional) `virtualenv`

## Setup

1. Clone this repository or download the project files.
2. (Optional) Setup and activate your virtualenv

```
python -m venv venv
source venv/bin/activate
```

3. Install the required Python packages using pip:

```
pip install -r requirements.txt
```

4. Copy the `.env.template` file in the root of this repository and rename the copy to `.env`.
5. Place your OpenAI API key in the specified location of the `.env` file:

```bash
OPENAI_API_KEY="your-api-key-here"
```

## Running the Project

To start a conversation with the AI, run the `main.py` script:

```
python main.py
```

Type your messages into the CLI and receive responses from the AI. Type 'quit' to end the conversation.

## Running the Tests

To run the tests found in the `./test/` directory, run the following command:

```bash
PYTHONPATH=. pytest ./test/
```