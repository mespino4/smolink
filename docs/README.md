![Logo](../react-client/public/smolink.png)
# Smolink: A URL Shortener

Smolink is a URL shortener

## Features

- Shorten long URLs into short, easy-to-share links
- Simple minimalistic user interface
- Copy button to save you a couple of seconds of work

## Tech Stack
- **Backend**: Flask & SQLite
- **Frontend**: React

## Installation

## Server Installation
To install and run the Smolink server (Flask) locally, follow these steps:
1. Clone this repository:
 ```
 https://github.com/mespino4/smolink
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

5. Access Smolink in your web browser at `http://localhost:5000`.

## Client Installation

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

## Usage

To shorten a URL, follow these steps:

1. Open Smolink in your web browser.
2. Enter the long URL you want to shorten in the input field.
3. Click the "Shorten" button.
4. Copy the generated short link and share it with others.
