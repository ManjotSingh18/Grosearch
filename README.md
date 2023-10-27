![Logo](Grosearch_Application/static/Grosearch.png)
# About
Grosearch is here to streamline online grocery shopping experience. Bid farewell to repetitive typing, browser tab clutter, and digital headaches. With Grosearch, we provide a powerful single search that spans multiple online stores, presenting you with products. The focus is on helping you manage your budget and find the best prices, ensuring both time and money savings.

# Mission
Develop a singular search that encompasses multiple retailers, displaying their products for straightforward comparison, with a emphasis on budget-friendly options.

# Features
* Powerful single search across multiple retailers, simplifying shopping experience
* Easy to navigate graphical interface 
* Discover products, sorted by lowest price by default
* View products side-by-side in a visually friendly format for easy comparison
* Operates on your local host and only requires outbound connections to authorized retailers, ensuring your data remains secure

# Low Prices Guaranteed
At first glance, you might notice that Grosearch doesn't offer personalized sorting options for displayed products. This design choice aligns with the mission: to prioritize budgeting and provide the lowest of prices. We assume that our users, including students and budget shoppers, are primarily seeking cost-effective solutions. With Grosearch, savings are a priority.

# Partner Stores
The selection of partner stores is based on convenience. We've established communication with Walmart through their Application Programming Interface (API). In contrast, we've obtained data from Sprouts, Costco, and Albertsons by scraping publicly available information from their websites. It's important to note that all rights are reserved to these retailers, and this application is not intended for personal monetary gain. Links are included to the retailer websites where you can purchase any displayed product.

# Video Showcase
<a href="https://www.youtube.com/watch?v=YatHC76V7u4"><img src="https://img.youtube.com/vi/YatHC76V7u4/maxresdefault.jpg" width="100%" height="auto" style="border-radius:50%"></a>

# Requirements
* Python (Selenium, Requests, JSON, Flask) 
* Python Interpreter
* Network Connection
* Chrome 
* Chrome driver win32 (Match version of Chrome)

# Installation
1. Download the repository in zip format.
![Logo](Grosearch_Application/README_Images/Zip.png)
2. Unzip the repository and ensure it's placed in current users download folder. This step is essential for proper functioning.
![Logo](Grosearch_Application/README_Images/Extract.png)
3. Open the folder Grosearch_Application through your preferred interpreter
4. To ensure compatibility, find your current Chrome version. You can do this by clicking the three dots in the top right-hand corner, then selecting "Help," and finally clicking "About Google Chrome." Note the version number.
5. Visit ChromeDriver (https://chromedriver.chromium.org/downloads) and download the corresponding "win32" version of ChromeDriver. Ensure that ChromeDriver is downloaded and unzipped into the "downloads" folder, maintaining the file structure as follows: "downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe."
6. Follow the user guide below

# User Guide
1. Navigate to the Grosearch_Application in a terminal.
2. Assuming necessary modules are installed run app.py using command: python app.py (Install required libraries by opening the terminal navigating to Grosearch_Application and using the command, pip install -r requirements.txt).
3. The console will display something similar to the image below.
![Logo](Grosearch_Application/README_Images/Console.png)
4. Open your browser and visit your local host by searching http://127.0.0.1:5000.
5. The application should present a landing page at your local connection (http://127.0.0.1:5000) like the one below:
![Logo](Grosearch_Application/README_Images/Landing.png)
6. Now perform a search on the desired product, it may take anywhere from 40-70 seconds due to the intensive nature of scraping many sites.
7. After the search is complete a page will be displayed in a table format including stores logos on the top of each column with products underneath, scroll through comparing products and visit the retailer sites for the ones needed. Also from this search page further searches can be performed for products in the top-right-hand corner. The Grosearch logo will lead back to the landing page.
![Logo](Grosearch_Application/README_Images/Search.png)
8. Once done stop the process from the interpreter and the local host should be disengaged.

(If errors are occurring please check if you have a matching chrome driver with your Chrome version, and it is stored as downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe) 

# Technology 
## Python
* provides a stable foundation for module implementation and website development.
## HTML
* Forms the structure of graphical interface and is used in conjunction with Jinja2 to display data. 
## CSS
* Adds graphical styling to HTML structures.
## Flask
* Acts as the bridge between Python and HTML/CSS, enabling the registration, interpretation, and display of data.
## Selenium
* Serves as a web scraper, navigating websites by mimicking scrolls and clicks to gather the information needed.

# Contributions 
Grosearch is an open-source project and welcomes contribution. The process would include creating a branch from master and adding a new store module (ex. Target.py). Next the module requires one function, a scrape of any variety that is able to get products into an array format with each product being nested either as a dictionary or JSON (Price, Image, Retailer Link, Title). After that update, the app.py module catch() function's return statement needs to be modified as such: flask.render_template('search.html', (Insert Store Here)-data = (New Store).DataCapture(item), ...). Following that update Search.html and add a new table below the previous tables mimicking their structure, but with the new flask variables that hold the new product list. When the store is successfully incorporated and displaying products; ensure that the company's logo is displayed on the landing page, and credit is given. Thank you!

# Future
Grosearch will expand its scope through contributions encompassing more of the digital frontier. I am exploring the development of a lightweight graphical user interface (GUI) based on Python and the Qt package. This feature aims to streamline installation and usage, making it faster and more user-friendly (Project for Educational Purposes Only).


