# TOPSIS - Image Selection Web App

A web application that automates the process of selecting the best images from a scraped dataset using the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) multi-criteria decision-making method.

**Live Demo:** [https://topsis-one.vercel.app/](https://topsis-one.vercel.app/)

## 🚀 Features

-   **Image Scraping:** Automatically scrapes images based on a user-provided keyword.
-   **TOPSIS Ranking:** Ranks images based on multiple criteria:
    -   **Resolution (+):** Higher resolution is preferred.
    -   **File Size (-):** Smaller file size is preferred.
-   **Email Delivery:** Sends the top-ranked images as a ZIP file to your email.
-   **Tiered System:**
    -   **Free Tier:** Up to 50 images.
    -   **Paid Tier:** Analyze more than 50 images (uses a mock payment gateway).
-   **Interactive UI:** Clean and responsive web interface built with Flask.

## 🛠️ Tech Stack

-   **Frontend:** HTML, CSS
-   **Backend:** Python, Flask
-   **Deployment:** Vercel
-   **Algorithms:** TOPSIS (Pandas, NumPy)
-   **Tools:** Pillow (Image Processing), Requests

## 📦 Installation & Local Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Shivansh0306/topsis.git
    cd topsis
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

4.  **Open in Browser:**
    Go to `http://localhost:5000`

## 📝 How It Works

1.  Enter a **keyword** (e.g., "Space", "Nature") and the **number of images** you want.
2.  Enter your **email address**.
3.  The app scrapes images and calculates a TOPSIS score for each.
4.  Images are ranked, and the top $N$ images are selected.
5.  Proceed to the payment page (if applicable) or directly confirm.
6.  Receive a ZIP file containing the best images in your email.

## 📂 Project Structure

-   `app.py`: Main Flask application handling routes and logic.
-   `templates/`: HTML templates for the UI.
-   `static/`: CSS and static assets.
-   `TOPSIS/`: Core TOPSIS implementation scripts.

## 📄 License

This project is open-source and available for educational purposes.
