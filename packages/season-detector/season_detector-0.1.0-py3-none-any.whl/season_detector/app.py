from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Utility function to determine the season based on average RGB values
def determine_season(rgb):
    r, g, b = rgb
    if r > 200 and g > 200 and b < 100:
        return "Summer"
    elif r > 200 and g < 100 and b < 100:
        return "Fall"
    elif r < 100 and g < 100 and b > 200:
        return "Winter"
    elif r < 100 and g > 200 and b < 100:
        return "Spring"
    else:
        return "Unknown"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    if file:
        # Save the uploaded file
        filename = file.filename
        file_path = os.path.join('season_detector/static', filename)
        file.save(file_path)
        
        # Open the image file and calculate the average RGB values
        image = Image.open(file_path)
        image = image.resize((100, 100))  # Resize for faster processing
        np_image = np.array(image)
        avg_color_per_row = np.average(np_image, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        
        season = determine_season(avg_color)
        
        return jsonify({"season": season, "rgb": avg_color.tolist(), "image_url": file_path})

if __name__ == '__main__':
    app.run(debug=True)
