from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

@app.route('/')
def my_shop():
	return render_template("home.html")

@app.route ('/product')
def my_2_shop():
	return render_template("product.html")




# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
