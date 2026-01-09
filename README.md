# Multiplication Table Generator

A simple Flask web application that generates multiplication tables for any given number.

## Description

This application provides a user-friendly web interface where users can input a number and instantly view its multiplication table (from 1 to 10). Built with Flask and Python, it can be run locally or deployed using Docker.

## Features

- Web-based interface for generating multiplication tables
- Displays the multiplication table for any integer input
- Clean and simple UI
- Docker support for easy deployment

## Requirements

- Python 3.9+
- Flask

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akshattalwar001/test.git
cd test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running with Python

Start the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Running with Docker

1. Build the Docker image:
```bash
docker build -t multiplication-table-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 multiplication-table-app
```

The application will be available at `http://localhost:5000`

## How to Use

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter a number in the input field
3. Click the "Generate" button
4. View the multiplication table for your chosen number