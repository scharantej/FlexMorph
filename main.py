
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

# Create the Flask application instance
app = Flask(__name__)

# Set the secret key for session management
app.config['SECRET_KEY'] = 'super-secret-key'

# Define the form for assembly and dismantle triggers
class AssemblyDismantleForm(FlaskForm):
    assemble = BooleanField('Assemble')
    dismantle = BooleanField('Dismantle')
    submit = SubmitField('Trigger')

# Define the routes
@app.route('/')
def index():
    # Render the main landing page
    return render_template('index.html')

@app.route('/assemble', methods=['GET', 'POST'])
def assemble():
    form = AssemblyDismantleForm()
    if form.validate_on_submit():
        if form.assemble.data:
            # Trigger the assembly animation
            return redirect(url_for('car_assembly'))
    return render_template('index.html', form=form)

@app.route('/dismantle', methods=['GET', 'POST'])
def dismantle():
    form = AssemblyDismantleForm()
    if form.validate_on_submit():
        if form.dismantle.data:
            # Trigger the dismantle animation
            return redirect(url_for('car_dismantle'))
    return render_template('index.html', form=form)

@app.route('/car-assembly')
def car_assembly():
    # Render the car assembly section
    return render_template('car-assembly.html')

@app.route('/car-dismantle')
def car_dismantle():
    # Render the car dismantle section
    return render_template('car-dismantle.html')

@app.route('/static/<path:path>')
def static_files(path):
    # Serve static files (CSS, JavaScript, etc.)
    return app.send_static_file(path)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


This Python code creates a Flask application with the necessary routes and templates to implement a dynamic landing page for a 4-wheeler SUV car that can be assembled and dismantled on user interaction.