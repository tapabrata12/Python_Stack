
# Cat vs Dog Classifier

This project uses TensorFlow and Streamlit to create a web app that can classify images of cats and dogs. The model was trained using a dataset of cat and dog images, and it uses a convolutional neural network (CNN) to make predictions.

## Technologies Used
- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Pillow (PIL)

## Features
- Upload an image of a cat or a dog.
- The model will predict whether the image is a cat or a dog.
- Simple and easy-to-use web interface built with Streamlit.

## Setup and Installation

### 1. Clone the repository
Clone the project repository to your local machine.

```bash
git clone https://github.com/tapabrata12/Python.git
```

### 2. Create a Conda Environment
If you don't already have a Conda environment, create one with the following command:

```bash
conda create --name cat-dog-env python=3.8
conda activate cat-dog-env
```

### 3. Install Required Packages

Make sure you have the required dependencies installed. You can install them using `pip` or by running the provided `requirements.txt` file.

#### Option 1: Using `pip`

```bash
pip install -r requirements.txt
```

#### Option 2: Manually Install with `pip`

```bash
pip install tensorflow streamlit numpy pillow
```

### 4. Run the Streamlit App

After the installation is complete, you can run the Streamlit app using the following command:

```bash
streamlit run app.py
```

This will start the app, and you can open it in your browser by going to `http://localhost:8501`.

## Usage
- Upload an image of a cat or a dog.
- The model will process the image and show the prediction (`🐱 Cat` or `🐶 Dog`).
- The app will display the uploaded image along with the prediction result.

## Model Details
The model used in this project is a convolutional neural network (CNN) trained on a dataset of cat and dog images. The model is saved in the file `cat_dog_classifier.h5`.
oblems with the app or the model.