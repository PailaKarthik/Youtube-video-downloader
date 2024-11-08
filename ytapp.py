from flask import Flask, render_template, request, send_file
import os
from yt_dlp import YoutubeDL  # or import youtube_dl if using that

app = Flask(__name__)

# Route to display the home page
@app.route('/')
def index():
    return render_template('new.html')

# Route to handle video download
@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    
    # Set your desired download path here
    download_directory = r'C:\Users\rakes\Documents\trail\web\ytVD\%(title)s.%(ext)s'
    
    # Options for yt-dlp (or youtube_dl)
    ydl_opts = {
        'format': 'best',
        'outtmpl': download_directory,  # Set the download path
        'noplaylist': True,  # Download only single video, not playlists
    }
    
    try:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(download_directory), exist_ok=True)
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info_dict = ydl.extract_info(url, download=False)  # Get info to get the filename
            filename = ydl.prepare_filename(info_dict)  # Prepare the filename

        return send_file(filename, as_attachment=True)
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
