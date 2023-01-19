from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'astorx.team@gmail.com'
app.config['MAIL_PASSWORD'] = 'pzxrvxaqipfxojdu'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



app = Flask(__name__)

@app.route("/" )
def send_email():
    msg = Message('Hello from the other side!', sender='astorx.team@gmail.com', recipients=['samanaroto3@gmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
   app.run(debug = True)