
# Cosine Similarity Web Application

## Project Description

The Cosine Similarity Web Application is a tool designed to calculate the cosine similarity between two web page contents and display the similarity percentage on a progress bar. Additionally, it provides a table to store and view previously saved similarity percentages. Users can also delete compared results from the table. The application includes a feature for comparing text box content, displaying the similarity percentage instantly on the same page.

## Minimum Viable Product (MVP)

### 1. Registration Form

New users are required to register using a unique username and password.

### 2. Login Form

Registered users can log in using their username and password to access the application.

### 3. Web Page Content Similarity Check

- The application webscrapes the content of the provided links.
- Compares and calculates the cosine similarity.
- Displays the similarity percentage on a progress bar.
- Allows users to save the results to a table for future reference.

### 4. Text Similarity Check

- Offers a feature to compare text entered or copied/pasted by the user.
- Displays the similarity percentage on the same page.

## Getting Started

1. Clone the repository to your local machine.
   
2. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```

3. Run the application.
   ```
   python app.py
   ```

4. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Register as a new user with a unique username and password.
2. Log in using your credentials.
3. To compare web page content:
   - Enter the URLs you want to compare.
   - Click the "Submit" button.
   - The similarity percentage will be displayed on a progress bar.
   - Save the results to the table if needed.
4. To compare text content:
   - Enter or paste the text in the provided text box.
   - Click the "Compare Text" button.
   - The similarity percentage will be displayed on the same page.


---
