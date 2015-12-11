from db.user_model import User

ksc_db.create_all()


def add_user(request):
    user = User(
        first_name=request.form["firstname"],
        last_name=request.form["lastname"],
        username=request.form["username"],
        email=request.form["email"],
        password=request.form["password"],
        contact=request.form["contact"],
        dob=request.form["dob"],
        gender=request.form["gender"],
        address=request.form["currentaddress"],
        address_permanent=request.form["permanentaddress"],
        country=request.form["country"],
        city=request.form["city"],
        institution=request.form['university'],
        course=request.form['course'],
        known_ksc_by=request.form['question']
    )

    ksc_db.session.add(user)
    ksc_db.session.commit()
