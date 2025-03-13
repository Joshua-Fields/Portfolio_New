from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
import logging

app = Flask(__name__)

# Setup logging to write errors to a file (for Railway logs)
logging.basicConfig(filename="error.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s: %(message)s")

# Configure Flask-Mail with environment variables for security
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config['MAIL_PORT'] = int(os.getenv("MAIL_PORT", 587))
app.config['MAIL_USE_TLS'] = os.getenv("MAIL_USE_TLS", "True") == "True"
app.config['MAIL_USE_SSL'] = os.getenv("MAIL_USE_SSL", "False") == "True"
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME", "joshuafields.dev@gmail.com")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD", "ozau zvjd tgmt gxnc")
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

# Sample project data
projects = [
    {
        "name": "Cloud-Native E-commerce Platform",
        "description": "This project is a cloud-native e-commerce platform built using Flask, Docker, and Google Kubernetes Engine (GKE).",
        "github": "https://github.com/Joshua-Fields/cloud-native-ecommerce"
    },
    {
        "name": "RFIQD Flattening & Mock-File Reducer",
        "description": "This repository provides tools to reduce the size of .rfiqd files by creating 'mock' copies with limited data.",
        "github": "https://github.com/Joshua-Fields/RFIQD-Compression"
    },
    {
        "name": "Distributed Mandelbrot Fractal Renderer",
        "description": "Demonstrates distributed processing by rendering the Mandelbrot fractal across multiple Dask workers.",
        "github": "https://github.com/Joshua-Fields/Monte-Carlo/tree/main"
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects, github="https://github.com/Joshua-Fields", linkedin="https://www.linkedin.com/in/joshua-fields-/")

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message_body = request.form.get('message')

    msg = Message(
        subject=f"New Contact Request from {name}",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=["JoshuaFields.dev@gmail.com"]
    )
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"

    try:
        logging.info(f"Attempting to send email from {email} to {app.config['MAIL_DEFAULT_SENDER']}")
        mail.send(msg)
        flash("Message sent successfully!", "success")
        logging.info("Email sent successfully!")
    except Exception as e:
        error_message = f"Failed to send message: {str(e)}"
        logging.error(error_message)
        flash(error_message, "danger")

    return redirect(url_for('home'))

@app.route('/test-email')
def test_email():
    try:
        msg = Message("Test Email from Railway",
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=["JoshuaFields.dev@gmail.com"])
        msg.body = "This is a test email from Railway."
        mail.send(msg)
        return "✅ Test email sent successfully!", 200
    except Exception as e:
        return f"❌ Failed to send test email: {str(e)}", 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0", port=port, debug=True)
