---

# 🌿 Virtual Herbarium

The **Virtual Herbarium** project leverages deep learning models to accurately classify medicinal plant leaves from images, streamlining the identification process. This innovative platform bridges the gap between traditional herbal knowledge and modern technology by connecting identified leaves to a detailed database of medicinal benefits and traditional uses.

Developed using **TensorFlow** and **Keras**, the project includes a user-friendly interface for uploading leaf images, identifying plants, and exploring their medicinal significance. This initiative promotes accessibility, fosters awareness, and encourages sustainable health practices.

---

## ✨ Features

- **Medicinal Plant Classification**: Upload an image of a medicinal plant leaf to classify it with high accuracy using a robust deep learning model.
- **Comprehensive Database**: Access detailed information about medicinal uses, benefits, and traditional applications of the identified plants.
- **Interactive UI**: Intuitive design with options to upload images, predict classifications, and explore additional plant details.
- **Promoting Sustainability**: Educates users about traditional herbal practices, promoting awareness of sustainable health solutions.

---

## 🚀 Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Deep Learning Models**: TensorFlow, Keras
- **Database**: A comprehensive plant information repository

---

## 🛠️ Installation Guide

Follow these steps to run the project locally:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Varalakshmikannuru/virtualHerbarium.git
   ```
2. Navigate to the project directory:
   ```bash
   cd virtualHerbarium
   ```
3. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Flask application:
   ```bash
   flask run
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🖼️ How to Use

### Step 1: Upload an Image
1. On the homepage, you will find an **Upload Section**.
2. Drag and drop an image of the medicinal plant leaf or click **Browse Files** to select an image from your computer.

### Step 2: Predict the Plant Class
1. Once the image is uploaded, click the **Predict** button.
2. The system will process the image and display the plant classification with its name.

### Step 3: Explore More Details
- After the prediction, click the **More Details** button to access in-depth information about the plant, including:
  - Medicinal properties
  - Traditional uses
  - Cultural significance

### Step 4: Discover More Plants
- If you want to explore additional medicinal plants, click the **More Leaves** button on the interface. This will display a collection of other plants available in the database with detailed descriptions.

---

## 📂 Project Structure

```
virtualHerbarium/
│
├── static/                # Static assets (images, CSS, JavaScript)
├── templates/             # HTML templates for the web pages
├── model/                 # Pre-trained deep learning models
├── app.py                 # Flask application logic
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── ...                    # Other files and scripts
```

---

## 🌟 Highlights

1. **Efficiency**: Reduces the time and effort required for medicinal plant identification.
2. **Accessibility**: Simplifies access to traditional herbal knowledge.
3. **Educational**: Promotes awareness of the benefits of medicinal plants in sustainable healthcare.

---

## 📸 Screenshots

**Homepage**  
_A clean and interactive interface to upload and predict plant classification._  

![Homepage](static/screenshots/homepage.png)

**Prediction Output**  
_Display of plant classification and a detailed explanation._  

![Prediction](static/screenshots/prediction.png)

---

## 🌱 Contributing

We welcome contributions to improve the project! Please feel free to submit pull requests or report issues.

---

## 📬 Contact

If you have any questions or feedback, feel free to reach out:

- **Email**: [varalakshmikannuru1107@gmail.com]
- **GitHub**: [Varalakshmikannuru](https://github.com/Varalakshmikannuru)

---
