import sys
from flask import Flask, render_template, redirect, request
from shortener import Shortener

app = Flask(__name__, template_folder="")

# Initialize an instance of the Shortener class
shortener1 = Shortener()

# Define a route for the homepage
@app.route('/')
def home():
    """Renders the homepage template."""
    return render_template('home.html')

# Define a route to handle form submission and display shortened URL
@app.route('/shorten', methods=['POST'])
def shorten():
    """Handles form submission and generates a shortened URL using the shortener class.
    Renders result.html template with the shortened URL."""
    # Get the URL entered in the form
    url = request.form['url']
    
    # Call the shorten() function from the Shortener class to generate a shortened URL
    short_url = shortener1.shorten(url)
    
    # Render the result.html template and pass the shortened URL as a variable
    return render_template('result.html', short_url=short_url)

# Define a route to redirect users to the original URL
@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redirects user to the original URL associated with the given shortened URL."""
    # Call the get_url() function from the Shortener class to retrieve the original URL
    url = shortener1.get_url(short_url)
    
    # If the original URL is found in the database, redirect to it
    if url:
        return redirect(url)
    else:
        # If the original URL is not found, return an error message
        return 'URL not found'

# Start the application on the given port
if __name__ == '__main__':
    #DO not remove any Code below
    port = int(sys.argv[1])
    app.run(debug=True, host="0.0.0.0", port=port)
