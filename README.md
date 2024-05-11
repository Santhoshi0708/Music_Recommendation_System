# <img src="img.png" alt="Img" style="width: 30px; height: auto; background-color: black;"/> Music Recommendation System

This is a Music Recommendation System that provides personalized song recommendations based on user-selected songs. It utilizes machine learning techniques to analyze song features and recommend similar songs to the user.

## Overview

The Music Recommendation System is built using Streamlit, a Python library for creating web applications, and various machine learning algorithms for recommendation purposes. It allows users to select a song from a dropdown menu and generates recommendations based on the selected song's features such as artists, album, and user ratings. The recommendations are dynamically generated using cosine similarity between song features.

## Features

- **User Interface**: The system provides a simple and intuitive user interface built using Streamlit, allowing users to interact with the application easily.
- **Song Selection**: Users can select a song from a dropdown menu populated with available songs.
- **Dynamic Recommendations**: Recommendations are generated dynamically based on the selected song, providing real-time personalized suggestions.
- **Customization**: Users can further customize their recommendations based on their preferences by selecting different songs.

## Installation

1. Clone the repository:

    ```
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```
    streamlit run app.py
    ```

4. Access the app in your web browser at `http://localhost:8501`.

## Usage

1. Launch the Streamlit app using the instructions above.
2. Select a song from the dropdown menu.
3. Click the "Show Recommendation" button to see recommended songs based on your selection.
4. Explore the recommended songs and enjoy!

## Data Sources

The song data used for recommendations can be obtained from various sources, including APIs, databases, or CSV files. Ensure that the data includes features such as song title, artists, album, and user ratings for accurate recommendations.

## Credits

- **Streamlit**: Used for building the interactive web application.
- **Python Libraries**: Including pandas, scikit-learn, and requests for data manipulation, machine learning, and API requests, respectively.
- **APIs**: Utilized for fetching song data and poster URLs.

## Preview
[Checkout Here]()

## 🔗 Follow us
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kothapalli-santhoshi-368951254/)

## Feedback
If you have any feedback, please reach out to us at santhu2002.kothapalli@gmail.com

## License

This project is licensed under the [MIT License](LICENSE).
