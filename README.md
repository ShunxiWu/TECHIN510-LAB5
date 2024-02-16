# Seattle Events Web App

https://wushunxilab5.azurewebsites.net/

## Main Features:
1. **Visualize Data**: The web app displays visualizations of Seattle events data, including the most common event categories, events distribution by month, and events distribution by day of the week.
2. **Data Filtering**: Users can filter the data by selecting specific event categories from a dropdown menu, as well as choosing date ranges and locations using selectors.
3. **Map Display**: The web app shows the distribution of event venues on a map, which dynamically updates based on the selected event category and date range.

## File Descriptions:
1. **app.py**: This is the main Streamlit application file. It contains the frontend display and interaction logic of the web page, as well as interaction with the database.
2. **db.py**: This file contains the database connection and configuration information. It is used to establish a connection with the PostgreSQL database.
3. **scraper.py**: This file is used to scrape website data and store it in the database. Similar to db.py, it interacts with the database but is primarily used for data retrieval and updating.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
