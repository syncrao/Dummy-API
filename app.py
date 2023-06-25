from flask import Flask, render_template, request, redirect, session, flash, abort, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import psycopg2
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sssrrrkkk'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(50))
    posts = db.relationship('Post', foreign_keys='Post.post_id', backref='bpost' ,  lazy='dynamic', )
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy='dynamic')
    messages_received = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', lazy='dynamic')



class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('UTC')) + timedelta(hours=5, minutes=30))


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now(pytz.timezone('UTC')) + timedelta(hours=5, minutes=30))

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    note_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    note_content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now(pytz.timezone('UTC')) + timedelta(hours=5, minutes=30))


@app.route('/', methods=['GET', 'POST'])
def index():
    with app.app_context():
        db.create_all()
    if 'user_id' not in session:
        return redirect('/login')

    posts = Post.query.join(User).order_by(Post.id.desc()).all()

    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            user_id = session['user_id']
            post = Post(content=content, post_id=user_id)
            db.session.add(post)
            db.session.commit()
            return redirect('/')

    return render_template('index.html', posts=posts, username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect('/')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()    
        if user is not None:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect('/')
        else:
            flash('invalid username or password')    
               
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():    
    if 'user_id' in session:
        return redirect('/')

    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(name=name, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect('/')

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.bpost.id != session['user_id']:
        abort(403)
    db.session.delete(post)
    db.session.commit()

    flash('Post deleted successfully', 'success')
    return redirect('/')


@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        recipient_username = request.args.get('recipient_username')
        content = request.form.get('content')

        sender_id = session['user_id']
        sender = User.query.get(sender_id)
        recipient = User.query.filter_by(username=recipient_username).first()

        if not recipient:
            flash('Recipient not found', 'error')
            return redirect('/messages')

        if content == None:
            return redirect(url_for('messages', recipient_username=recipient_username))    

        message = Message(sender_id=sender.id, recipient_id=recipient.id, content=content)
        db.session.add(message)
        db.session.commit()

        flash('Message sent successfully', 'success')
        return redirect(url_for('messages', recipient_username=recipient_username))

    recipient_username = request.args.get('recipient_username')

    if recipient_username:
        recipient = User.query.filter_by(username=recipient_username).first()

        if not recipient:
            abort(404)

        current_user_id = session['user_id']
        messages_sent = Message.query.filter((Message.sender_id == current_user_id) & (Message.recipient_id == recipient.id)).order_by(Message.id).all()

        messages_received = Message.query.filter((Message.sender_id == recipient.id) & (Message.recipient_id == current_user_id)).order_by(Message.id).all()

        combined_messages = messages_sent + messages_received
        messages = sorted(combined_messages, key=lambda x: x.id, reverse=True)

        return render_template('messages.html', recipient=recipient, messages=messages)


    return render_template('messages.html', messages=messages)

@app.route('/note', methods=['POST', 'GET'])
def note():
    if 'user_id' not in session:
        return redirect('/login') 
    note_id = session['user_id']     
    notes = Note.query.filter(Note.note_user == note_id).order_by(Note.id.desc()).all()
    if request.method == 'POST':
        note_content = request.form.get('note_content')  
        if note_content:
            
            note = Note(note_content=note_content, note_user=note_id)
            db.session.add(note)
            db.session.commit()
            return redirect('/note')

    return render_template('note.html', notes=notes )   

@app.route('/edit-note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    if 'user_id' not in session:
        return redirect('/login')

    note = Note.query.get(note_id)

    if note is None or note.note_user != session['user_id']:
        return redirect('/note')

    if request.method == 'POST':
        note_content = request.form.get('note_content')

        if note_content:
            note.note_content = note_content
            db.session.commit()
            return redirect('/note')

    return render_template('edit_note.html', note=note)

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    post = Note.query.get_or_404(note_id)
    db.session.delete(post)
    db.session.commit()

    flash('Post deleted successfully', 'success')
    return redirect('/note')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')        

if __name__ == '__main__':
    app.run(debug=True)
