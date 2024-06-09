# ChromeBMS

## Description

This is a Python utility that reads your Chrome bookmarks and saves them locally as PDF files. The project is designed to be simple and efficient, leveraging the power of `pyppeteer` to generate PDFs from your bookmarks.

## Features

- Reads Chrome bookmarks.
- Saves bookmarks as PDF files locally.
- Easy setup and installation.

## Requirements

- Python 3.6 or higher
- Google Chrome browser

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GMichetti/ChromeBMS.git
    cd ChromeBMS
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure your virtual environment is activated:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Run the script:
    ```bash
    python chromeBMS.py
    ```

## Troubleshooting

- **`pyppeteer` Issues**: If `pyppeteer` fails to install or run properly, you might need to follow the specific instructions in the comment within the code. This typically involves manual installation steps.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to contact me at [gius.michetti@gmail.com](mailto:gius.michetti@gmail.com).
