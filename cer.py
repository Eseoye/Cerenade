from flask import Flask, redirect, render_template, url_for, request, flash
import datetime
import smtplib
from flask_mail import Mail, Message
from config import mail_username, mail_password


app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/service.html')
def service():
    
    return render_template('service.html')

@app.route("/contact.html", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        msg = Message(subject=f"Mail from {name}", body=f"Name: {name}\nE-mail: {email}\nPhone: {phone}\n\n\n{message}", sender=mail_username, recipients=['esenosa.ugiagbe@gmail.com'] )
        mail.send(msg)
        return render_template("contact.html", success=True)
        
    return render_template('contact.html')





if __name__ == "__main__":
    app.run(debug=True)
