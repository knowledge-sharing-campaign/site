import hashlib


class User(ksc_db.Model):
    first_name = ksc_db.Column(ksc_db.String(140))
    last_name = ksc_db.Column(ksc_db.String(140))
    username = ksc_db.Column(ksc_db.String(80), unique=True, primary_key=True)
    email = ksc_db.Column(ksc_db.String(120), unique=True, primary_key=True)
    password = ksc_db.Column(ksc_db.String(128))
    contact = ksc_db.Column(ksc_db.Integer())
    dob = ksc_db.Column(ksc_db.String(10))
    gender = ksc_db.Column(ksc_db.String(6))
    address = ksc_db.Column(ksc_db.String(200))
    address_permanent = ksc_db.Column(ksc_db.String(200))
    country = ksc_db.Column(ksc_db.String(50))
    city = ksc_db.Column(ksc_db.String(50))
    institution = ksc_db.Column(ksc_db.String(100))
    course = ksc_db.Column(ksc_db.String(50))
    known_ksc_by = ksc_db.Column(ksc_db.String(20))

    def __init__(self, first_name, last_name, username, email, password, contact, dob, gender, address,
                 address_permanent, country, city, institution, course, known_ksc_by):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = hashlib.sha512(password).hexdigest()
        self.contact = contact
        self.dob = dob
        self.gender = gender
        self.address = address
        self.address_permanent = address_permanent
        self.country = country
        self.city = city
        self.institution = institution
        self.course = course
        self.known_ksc_by = known_ksc_by

    def __repr__(self):
        return '<User %r>' % self.username
