import json
from flask import Flask, render_template, request, redirect, url_for, abort

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# --- Fungsi untuk Memuat Data ---

def load_movies():
    """Memuat data film dari file JSON."""
    with open('app/data/movies.json', 'r') as f:
        return json.load(f)

def load_users():
    """Memuat data pengguna dari file JSON."""
    with open('app/data/users.json', 'r') as f:
        return json.load(f)

# --- Fungsi Helper Data ---

def get_user_by_username(username):
    """Mencari pengguna berdasarkan nama pengguna."""
    users = load_users()
    for user in users:
        if user['username'] == username:
            return user
    return None

def get_all_users():
    """Mendapatkan semua nama pengguna dari data."""
    users = load_users()
    return [user['username'] for user in users]

# --- Logika Inti: Sistem Rekomendasi ---

def get_recommendations(user):
    """
    Menghasilkan rekomendasi film untuk pengguna berdasarkan preferensi genre.
    """
    if not user:
        return []

    movies = load_movies()
    user_preferences = user.get('preferences', [])
    user_history = user.get('history', [])

    recommendations = []
    for movie in movies:
        if movie['genre'] in user_preferences and movie['id'] not in user_history:
            recommendations.append(movie)

    return recommendations[:5]

# --- Logika untuk Umpan Balik (Placeholder) ---

def save_feedback(username, movie_id, feedback_type):
    """
    Menyimpan umpan balik dari pengguna.
    Untuk MVP, fungsi ini akan menyimpan umpan balik ke file log.
    """
    with open('app/feedback.log', 'a') as f:
        f.write(f"FEEDBACK: Pengguna '{username}' menandai film ID '{movie_id}' sebagai '{feedback_type}'.\n")


# --- Rute Aplikasi Flask ---

@app.route('/')
def index():
    """Halaman utama untuk memilih pengguna."""
    users = get_all_users()
    return render_template('index.html', users=users)

@app.route('/recommendations/<username>')
def show_recommendations(username):
    """Menampilkan rekomendasi untuk pengguna yang dipilih."""
    user = get_user_by_username(username)
    if not user:
        abort(404, description="Pengguna tidak ditemukan")

    recommendations = get_recommendations(user)
    return render_template('recommendations.html', user=user, recommendations=recommendations)

@app.route('/profile/<username>')
def show_profile(username):
    """Menampilkan halaman profil pengguna."""
    user = get_user_by_username(username)
    if not user:
        abort(404, description="Pengguna tidak ditemukan")

    return render_template('profile.html', user=user)

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """Menerima dan memproses umpan balik dari pengguna."""
    username = request.form.get('username')
    movie_id = request.form.get('movie_id')
    feedback_type = request.form.get('feedback_type')

    if not all([username, movie_id, feedback_type]):
        # Penanganan jika ada data yang hilang
        return "Data umpan balik tidak lengkap.", 400

    save_feedback(username, movie_id, feedback_type)

    # Alihkan kembali ke halaman rekomendasi setelah memberikan umpan balik
    return redirect(url_for('show_recommendations', username=username))


# --- Blok Eksekusi Utama ---

if __name__ == '__main__':
    # Menjalankan server pengembangan Flask
    # Host '0.0.0.0' membuat server dapat diakses dari luar container
    app.run(host='0.0.0.0', port=5001, debug=True)
