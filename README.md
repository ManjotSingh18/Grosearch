# Grosearch
![Logo](Grosearch_Application/static/Grosearch.png)
# About
Searching for grocery across multiple websites has always been cumbersome due to redundant typing, and tabs cluttering the browser. Now is the time to simplify, and declutter. Welcome to Grosearch, a application with a powerful singular search able to traverse through several stores displaying popular products to users while focusing in on budgeting and low prices. Grosearch seeks to foster an enviornment where money and time is saved alongside stopping digital headaches. 

# Features
* Powerful singular search encompassing several retailers and products
* Easy to navigate graphical interface 
* Displays popular products sorted by lowest price by default
* Products formated graphically side-by-side emphasizing readability 
* Local host based only requiring outbound connections to authorized retailers

# Low Prices Guranteed
A glaring issue about the displayed products that may arise at first sight is the lack of personalized options for sorting. This was done by design as Grosearch seeks to focus on budgeting, and sorting features have been ommited as it is assumed users are seeking the lowest prices with less emphasis on other categories. Grosearch is catered towards students, and anyone else who is seeking to save money. 

# Partner Stores
The Stores have been selected based upon accessibility. The communications with Walamrt is established by uttilization of their Application Programming Interface. Alternatively the communications with Sprouts, CostCo, and Alberstons was established by scraping their publicly available data off their websites respectively. All rights are reserved to them, I do not seek personal monetary gain from this application. Links to retailer wesbites hosting the product have been provided if users are intrested in purchasing a displayed product.

# Requirements
* Python (Selenium, Requests, JSON, Flask) 
* Python Interpreter
* Network Connection
* Browser

# Installation
1. Download the repository in its entirety, it should be formatted as a zip file

3. Unzip the repository into your local users download folder, this is nessecary
4. Open the folder Grosearch_Application through your interpreter
5. Follow the user guide below

# User Guide
1. Within the Grosearch_Application folder open in interpreter find the app.py module
2. Assuming nessecary modules are installed (ex. pip install selenium, in command prompt) run app.py as a Python File
3. Within the respective console will display something simmilar to the image below
4. Open your browser, and visit your local host by searching http://127.0.0.1:5000
5. Ensure the program is still running as it will not work if running is paused or stopped within interpreter
6. The application should preseent a landing page at your local connection like the one below:
7. From here preform a search on the desired product, it may take anywhere from 40-70 seconds due to intensive nature of scraping many sites. Alterntively visit the links at the bottom of the page to learn more about the application, and development.
8. 
# Technology 
## Python
* Used to develop back-end of application providing a stable foundation for implementation of modules and future 
## HTML
* Provides foundation and structure for graphical interface of application displaying data via Jinja2 
## CSS
* Adds graphical, and themeatic accents upon html structures to make site more user-friendly
## Flask
* Creates a tether between Python and HTML/CSS allowing data to be registerd, interpreted and displayed
## Selenium
* Utilized as a versatile web scraper able to scrape several wesbites at an efficent rate mimicking scrolls, and clicks.


