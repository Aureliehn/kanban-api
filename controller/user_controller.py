from flask import jsonify
from db import get_db
import bcrypt
from flask import session

SUCCESS_MESSAGE = 'Connexion réussie'
FAILURE_MESSAGE = 'Échec de la connexion'

def hash_password(password):
    salt = bcrypt.gensalt()
    print(salt)
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")

def insert_user_service(data):
    try:
        new_user = data
        firstName = new_user['firstName']
        lastName = new_user['lastName']
        mail = new_user['mail']
        password = hash_password(new_user['password'])
        db = get_db()
        cursor = db.cursor()
        statement = "INSERT INTO users (firstName, lastName, mail, password) VALUES (?, ?, ?, ?)"
        cursor.execute(statement, [firstName, lastName, mail, password])
        db.commit()
        return jsonify({"message": "Utilisateur inséré avec succès."})
    except Exception as e:
        print(str(e))
        import traceback
        traceback.print_exc()
        return jsonify({"message": "Une erreur s'est produite lors de l'insertion de l'utilisateur."})

def get_user_by_email(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE mail = ?", (email,))
    user = cursor.fetchone()
    return user

def login_service(login_data):
    print(login_data['password'])
    email = login_data['mail']
    password = login_data['password']
    user = get_user_by_email(email)
    if user and bcrypt.checkpw(password.encode('utf-8'), user[4].encode('utf-8')):
        session['user_id'] = user[0]  # Storing the user ID in the session
        return jsonify({'message': SUCCESS_MESSAGE})
    else:
        return jsonify({'message': FAILURE_MESSAGE})

def logout_service():
    session.clear()
    return jsonify({'message': 'Déconnexion réussie'})

def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, firstName, lastName, mail, password FROM users"
    cursor.execute(query)
    return cursor.fetchall()