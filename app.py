import io

import numpy as np
from PIL import Image
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

model = load_model("static/models/cat_dog.keras")


def predict_image(image_data):
    img = Image.open(io.BytesIO(image_data)).resize((180, 180))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)

    if prediction[0][0] > 0.5:
        return "This is a dog!"
    else:
        return "Yes, this is a cat!"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/classify", methods=["POST"])
def predict():
    if "image" not in request.files:
        return render_template("result.html", prediction=None)

    image_file = request.files["image"].read()

    try:
        prediction = predict_image(image_file)
        return render_template("result.html", prediction=prediction)
    except Exception as e:
        return render_template("result.html", prediction=None)


if __name__ == "__main__":
    app.run(debug=True)
