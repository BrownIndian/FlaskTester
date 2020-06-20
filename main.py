from flask import Flask, render_template,request, session, url_for,redirect
from UserForm import UserForm, InfoForm, firebase_initializer, passer

#DELTE SOME OF THE FIREBASE STUFF IF YOU HAVE ERRORS

fb_init = firebase_initializer()
auth = fb_init[0]
db = fb_init[1]


class sender():
    def __init__(self, sentby):
        self.sentby = sentby

proxy = sender("")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfhlasdfklhfsdhfsabvn'


@app.route('/', methods=['GET', "POST"])
def index():
    proxy.sentby = "infoform"
    print(proxy.sentby)
    form = InfoForm()

    if form.validate_on_submit():
        print("Valid form")
        session['fname'] = form.fname.data
        session['lname'] = form.lname.data
        session['address'] = form.address.data
        
        
        if auth.current_user != None:
            print("Logged In")

            # doc_ref = db.collection(u'users').document(u'blackindian')
            # doc_ref.update(
            #     {u'fname': session['fname'],
            #     u'lname': session['lname'],
            #     u'address': session['address'],
            #     })

            # doc_ref = db.collection(u'users').document()
            # doc_ref.set({
                
            #     u'fname': session['fname'],
            #     u'lname': session['lname'],
            #     u'address': session['address'],
            #     u'city': session['city']
            # })
            print("Successfully updated to database")
        return redirect(url_for('thankyou'))
    return render_template('index.html', form = form)

@app.route('/register' , methods=['GET', "POST"])
def register():
    proxy.sentby = "register"

    form = UserForm()
    
    if form.validate_on_submit():
        print(request.form['index'])

    
    if request.method == "POST":
        print(request.form['index'])


        # user = auth.create_user_with_email_and_password(session['email'], session['password'])
        # user = auth.sign_in_with_email_and_password(session['email'], session['password'])


    return render_template('register.html',  form=form)

@app.route('/login', methods=['GET', "POST"])
def login():
    proxy.sentby = "login"
    form = UserForm()

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['password'] = form.password.data
        # try:
        #     auth.sign_in_with_email_and_password(session['email'], session['password'])
        # except:
        #     print("Pass is too short")

        return redirect(url_for('thankyou'))

    return render_template('login.html', form=form)



@app.route('/thankyou')
def thankyou():
    doc = db.collection(u'users').document(u'blackindian').get()
    return render_template('thankyou.html', sent=proxy.sentby)
    
if __name__ == "__main__":
    app.run(debug=True)


