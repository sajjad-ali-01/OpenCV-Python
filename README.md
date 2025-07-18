
# 👤 Face Detection & Recognition with OpenCV

This project demonstrates how to perform **face detection** and **face recognition** using Python and OpenCV. It includes functionality to detect faces in real-time from a webcam feed and recognize known individuals using trained data.

## 📌 Features

- **face detection** using Haar cascades.
- **Face recognition** using LBPH (Local Binary Patterns Histograms).
- Save and label faces for training.

## 🧠 How It Works

* **Detection:** Uses Haar cascade to find face regions.
* **Recognition:** Uses OpenCV’s `cv2.face.LBPHFaceRecognizer_create()` model to match input faces with trained faces.
* **Training:** Stores multiple labeled images per person and trains a model on them.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Author

**Sajjad Ali**
Feel free to connect via [LinkedIn](https://www.linkedin.com/sajjadali116) or raise an issue in this repo!

```
