import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 

import socket, ssl
import OpenSSL
from cryptography import x509
import cryptography
from datetime import datetime
import base64
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///certificates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecret'

db = SQLAlchemy(app)

class Host(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(50), nullable=False)

#def get_weather_data(city):
   # url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
   # r = requests.get(url).json()
   # return r

def get_cert_validity(hostname):
    port = 443
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as sslsock:
            der_cert = sslsock.getpeercert(True)
        # from binary DER format to PEM
        pem_cert = ssl.DER_cert_to_PEM_cert(der_cert)             
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem_cert)
        #pk = x509.get_pubkey()
        #print(x509.get_notAfter())
        #valid_till = datetime.strptime(x509.get_notAfter().decode('ascii'),'%Y%m%d%H%M%SZ')
        validity_till = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
        return validity_till

@app.route('/', methods=['GET'])
def index_get():
    hostnames = Host.query.all()

    cert_data = []

    for hostname in hostnames:
        validity = get_cert_validity(hostname.name)
        print(validity)

        cert = {
            'hoster' : hostname.name,
            'Valid untill' : validity,
            }

        cert_data.append(cert)
    return render_template('weather.html', cert_data=cert_data)


@app.route('/<hostname>')
def index(hostname):
    hostname = Host(hostname= hostname)
    db.session.add(hostname)
    db.session.commit()
    return '<h1>Added New host</h1>'
