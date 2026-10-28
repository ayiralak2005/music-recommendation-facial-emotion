from flask import Flask, render_template, request
import os

app = Flask(__name__)

MUSIC_DIR = "static"

@app.route("/", methods=["GET", "POST"])
def home():
    f = open("emotion.txt")
    emot = f.read()
    f.close()
    emotion = emot #request.args.get("emotion", "happy")  # Default: Happy songs
    index = request.args.get("index", 0, type=int)  # Get current song index
    songs = []

    # Check if emotion folder exists
    emotion_folder = os.path.join(MUSIC_DIR, emotion)
    if os.path.exists(emotion_folder):
        songs = [f"{emotion}/{song}" for song in os.listdir(emotion_folder) if song.endswith(".mp3")]

    total_songs = len(songs)

    # Ensure index is within bounds
    if total_songs == 0:
        current_song = None
    else:
        index = max(0, min(index, total_songs - 1))
        current_song = songs[index]

    return render_template("home.html",
                           songs=songs,
                           current_song=current_song,
                           emotion=emotion,
                           index=index,
                           total_songs=total_songs)

if __name__ == "__main__":
    app.run(debug=True)
