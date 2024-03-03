# Python Web Scraping Project

This project demonstrates how to perform web scraping using Python, focusing on the `playwright` and `BeautifulSoup4` libraries. It covers scraping information from a job site and saving the collected data into a CSV file. Additionally, it briefly explores the feasibility of scraping Instagram and TikTok.

## Required Libraries

The main Python libraries required for this project are:

- `playwright`: A library for browser automation, useful for data collection on dynamic websites.
- `beautifulsoup4`: A library for extracting data from HTML and XML files.
- `pandas`: A library for data analysis and manipulation, used to save scraped data into CSV files.

## Installation

To install the necessary libraries for this project, use the following command:

```bash
pip install playwright beautifulsoup4 pandas
```

Before using `playwright`, you need to install the necessary browser drivers with:

```bash
playwright install
```

## Web Scraping Overview

The project follows these steps:

1. **Loading Web Pages**: Use `playwright` to load the web page and scroll to the section containing the desired data.
2. **Extracting Data**: Parse the page's HTML with `BeautifulSoup` and extract the needed data.
3. **Saving Data**: Use `pandas` to save the extracted data into a CSV file.

## Instagram and TikTok Scraping Test

Instagram and TikTok implement robust mechanisms to prevent scraping. This project briefly explores the possibility of scraping these platforms, but users must adhere to the platforms' terms of service.

## Project Structure

The project is structured as follows:

- `lecture_x.py`: Simple Syntax Explanation and Example Code.
- `scrape_x.py`: The main script file containing the web scraping logic.
- `jobs/`: A directory for storing scraped data.

## Usage Example

This README does not provide direct code examples but focuses on an overview of the project's purpose, technologies used, installation methods, and project structure. Detailed implementation can be found in the `scrape_x.py` file.

