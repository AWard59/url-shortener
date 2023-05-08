The URL Shortener project is a simple web application that allows users to enter a long URL and generates a short URL for it. The generated short URL can then be used to access the original long URL. This project is implemented using Python or NodeJS, Flask, SQLite, and the py shorteners logic.

The URL shortener project consists of one module that works together to create a web application that shortens long URLs. The main file, app, defines the application and its routes for handling incoming requests, while the database handles the interaction between the application and the database where URLs and their shortened versions are stored. Shortener generates unique shortened URLs from the long URLs and checks if a generated URL already exists in the database. The HTML templates, home.html and result.html, define the structure and layout of the home page and the result page where users can input URLs for shortening and see the shortened version respectively.

Task 1:
You are tasked with creating a web application using Flask or NodeJS that displays a homepage. The page should be designed using HTML and CSS and should include the following elements:

Design a form that includes an input field and a button to submit the form.
The input field should have a name attribute set to "url". 
When the form is submitted, it should send a POST request to the endpoint "/shorten".

Task 2:
You have been assigned to develop a URL-shortening service in Python or NodeJS. Your task is to implement a web application with the following functionality:

Create a route /shorten that handles POST requests. The route should accept a form input with a name attribute set to "url". The URL provided in the form should be passed to a shorten() function.
Implement a shorten() function that generates a shortened URL using a random combination of 7 letters and digits, and inserts the original and shortened URLs into a database. If the generated short URL already exists, it should generate a new one. This function should return the shortened URL.
Implement a generate_short_url() function that generates a random combination of 7 letters and digits for the shortened URL.
Use the render_template() function to display the shortened URL to the user in a separate template called "result.html".
To accomplish this, you should use the request object to get the URL from the form, pass it to the shorten() function, and return the shortened URL to the result.html template. The shorten() function should generate a unique shortened URL, insert it into a database, and return it to the calling function.

Task 3:
You are tasked with developing a URL-shortening service in Python or NodeJS. Your task is to implement a function that redirects users to the original URL when they enter the shortened URL in their browser.

Create a route /short_url that accepts the shortened URL as an argument.
Implement a redirect_to_url() function that takes the short_url as an argument, looks up the original URL in a database, and redirects the user to the original URL using the redirect() function if the URL is found in the database.
Implement a get_url() function that retrieves the original URL from a database using the short_url as a parameter. If the short_url is found in the database, the function returns the corresponding original URL. Otherwise, it returns None.
To accomplish this, you should create a route /short_url that accepts the shortened URL as a parameter. Then, use the get_url() function to retrieve the original URL from a database. If the URL is found in the database, redirect the user to the original URL using the redirect() function. If the URL is not found in the database, display a message indicating that the URL was not found.