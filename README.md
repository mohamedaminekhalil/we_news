# We News(Web App with flask)
A Flask-based web application that retrieves and displays news articles using an external API. 
Users can filter news by category, save articles to favorites, and access archived articles by date.

## Features
- Displays the latest news articles on today page.
- Category filtering to refine news topics.
- Add articles to favorites or mark them for reading later.
- Archive feature that saves articles by the day.
- SQLite3 for local data storage.
- 
## Requirements
- Python 3.x
- Flask
- Requests (for API calls)
- SQLite3 (included with standard Python installations)

## API Instructions
The application fetches news articles from [News API](https://newsapi.org/). You will need an API key to access the news articles.
1. Sign up at [News API](https://newsapi.org/) to obtain your API key.
2. Add your API key to the application configuration in api.py.

## How to Use
1. Clone the repository.
2. Install the required packages: 
```bash
pip install -r requirements.txt
python main.py
Open your browser and navigate to http://127.0.0.1:2000
You can also use other devices that connects to same network open your browser and navigate to http://192.168.10.180:2000
```

## Usage Instructions
- Upon opening the app, you will see the latest news articles.
- Use the category navigation to go from category to another.
- Click the 'book_icon' button on any article to save it for later.
- Click the 'save_icon' button on any article to save it for later.
- Access saved articles in the 'Saved' section.
- Access later articles in the 'later' section.
- Navigate to the 'Archive' to view articles saved by date.

## Database Setup
The application uses SQLite3 for storing user preferences and archived articles. The database will be automatically created upon the first run.
Using one table to store data about article with 2 extra columns for saved and later takes boolean as a value 0 or 1

## Acknowledgments
- News articles sourced from [News API](https://newsapi.org/).
