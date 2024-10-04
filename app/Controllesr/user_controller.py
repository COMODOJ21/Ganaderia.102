#vamos a definir la lógica para el registro, login y perfil, utilizando consultas SQL manuales. Este código se conecta directamente a la base de datos y ejecuta consultas SQL para el login, registro, y el perfil de usuario.
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_bcrypt import Bcrypt
from flask import session
import os
from werkzeug.utils import secure_filename


user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']

        connection = current_app.connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, cedula FROM usuario WHERE apellido=%s", (nombre,))
                result = cursor.fetchone()
                if result and bcrypt.check_password_hash(result['apellido'], apellido):
                    session['user_id'] = result['id']  # Guardar el ID del usuario en la sesión
                    session['user_role'] = result['role_id']  # Guardar el rol del usuario en la sesión
                    return redirect(url_for('user_bp.dashboard'))  # Redirigir al dashboard
                else:
                    return "Login Failed"
        except Exception as e:
            return str(e)

    return render_template('login.html')

@user_bp.route('/dashboard')
def dashboard():
    # Redirigir al usuario a su página según el rol
    role_id = session.get('user_role')

    if role_id == 1:  # Administrador
        return redirect(url_for('admin_bp.admin_dashboard'))
    elif role_id == 2:  # Vendedor
        return redirect(url_for('seller_bp.seller_dashboard'))
    elif role_id == 3:  # Repostero
        return redirect(url_for('baker_bp.baker_dashboard'))
    else:
        return "Invalid Role"

@user_bp.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('user_bp.login'))

    connection = current_app.connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, email, role_id FROM usuarios WHERE id=%s", (user_id,))
            user = cursor.fetchone()
            if not user:
                return "User not found"
    except Exception as e:
        return str(e)

    return render_template('profile.html', user=user)

@user_bp.route('/logout')
def logout():
    # Limpiar la sesión y redirigir al login
    session.clear()
    return render_template('home.html')
    #return redirect(url_for('user_bp.login'))