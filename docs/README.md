![Smolink Logo](../react-client/public/smolink.png)

# Smolink: A URL Shortener

Smolink is a simple URL shortener application built with Flask (backend) and React (frontend).

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
  - [Server Installation](#server-installation)
  - [Client Installation](#client-installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## Features

- Shorten long URLs into short, easy-to-share links
- Simple minimalistic user interface
- Copy button to save you a couple of seconds of work

## Tech Stack

- **Backend**: Flask & SQLite
- **Frontend**: React

## Installation

### Server Installation

To install and run the Smolink server (Flask) locally, follow these steps:

1. Clone this repository:

    ```
    git clone https://github.com/mespino4/smolink.git
    ```

2. Navigate to the `flask-server` directory:

    ```
    cd flask-server
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the Flask server:

    ```
    python run.py
    ```

### Client Installation

To install and run the Smolink client (React) locally, follow these steps:

1. Navigate to the `react-client` directory:

    ```
    cd react-client
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

![Screenshot 1](screenshots/ss1.png)
*This is the application on startup*

![Screenshot 2](screenshots/ss2.png)
*paste a long URL, click the Shorten button and a short URL will be generated*

## License

This project is licensed under the [MIT License](LICENSE).
