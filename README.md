# Web Crawler Application

## Overview

The Web Crawler Application is a Flask-based web service that crawls a given root webpage up to a specified depth and returns the links found during the crawl process. This project is designed to help users extract hyperlinks from web pages and analyze website structures.

## Features

- **Crawl Web Pages:** The application can crawl a root URL and gather links up to a specified depth.
- **JSON Response:** Returns the crawled links in a structured JSON format.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Requests**: For making HTTP requests to crawl web pages.
- **BeautifulSoup**: For parsing HTML and extracting links.

## API Endpoint

### POST `/api/v1/crawl`

- **Request Body**: JSON object containing the following parameters:
  - `root_url`: The starting URL to crawl (string).
  - `max_depth`: The maximum depth to crawl (integer).

#### Example Request
```json
{
  "root_url": "https://github.com",
  "max_depth": 2
}


#### run using this:
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/v1/crawl" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"root_url": "https://github.com", "max_depth": 2}'
