![Smolink Logo](../react-client/public/smolinkShadowBg.png)

# Smolink: A URL Shortener
Born from the fusion of the words 'smol' and 'link. Smolink is URL shortening tool, crafted with a minimalistic user interface. Its clean UI was designed to reflect how it transforms ugly, long and cluttered URLs into URLs that are short, clean and visually appealing.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Server Installation](#server-installation)
  - [Client Installation](#client-installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Demo](#demo)
- [License](#license)

## Features

- Shorten long URLs into short, easy-to-share links
- Simple minimalistic user interface
- Copy button for easy sharing

## Tech Stack

- **Backend**: Flask & PostgreSQL
- **Frontend**: React
- **Containerization**: Docker

## Installation

### Server Installation

To install and run the Smolink server (Flask) locally, follow these steps:

1. Clone this repository:

    ```
    git clone https://github.com/mespino4/smolink.git
    ```

2. Navigate to the `flask-server` directory:

    ```
    cd smolink/flask-server
    ```

3. Create a Python virtual environment:
   Windows
    ```
    python -m venv <env_name>
    ```
  Linux
    ```
    python3 -m venv <env_name>
    ```
4. Activate the Python virtual environment:
   Windows
    ```
    <env_name>\Scripts\activate
    ```
  Linux
    ```
    source <env_name>/bin/activate
    ```

5. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Run the Flask server:

   Windows
    ```
    python run.py
    ```
  Linux
    ```
    python3 run.py
    ```

### Client Installation

To install and run the Smolink client (React) locally, follow these steps:

1. In a second terminal navigate to the `react-client` directory:

    ```
    cd smolink/react-client
    ```

2. Install dependencies:

    ```
    npm install
    ```

3. Run the React development server:

    ```
    npm run dev
    ```

4. Access Smolink in your web browser, usually at `http://localhost:5173/`.

## Usage

To shorten a URL, follow these steps:

1. Open Smolink in your web browser.
2. Enter the long URL you want to shorten in the input field.
3. Click the "Shorten" button.
4. Copy the generated short link and share it with others.

## Screenshots

![Homepage](screenshots/ss1.png)

*Homepage of the Smolink application*

![Shorten URL](screenshots/ss2.png)

*Shorten a URL with Smolink*

## Demo

![Demo](smolink_demo.gif)

*A demonstration of how Smolink works.*

## License

This project is licensed under the [MIT License](LICENSE).
