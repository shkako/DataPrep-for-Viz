**Historical Price of Computer Memory and Storage (2025 W1)**

This repository contains Python code that processes and prepares data from Our World in Data on the historical prices of computer memory and storage. The data was originally denormalized, and the goal of this project was to transform it into a more structured format to allow for visualizations of deviations in costs over time.

**Project Overview**
The dataset used in this project is provided by Our World in Data and includes historical information on computer memory (RAM) and storage (Hard Drives, SSDs) prices. The data was denormalized, which made it difficult to directly analyze trends. The main steps of this project were:

Data Download: The data was downloaded from the Our World in Data website.
Data Transformation: The raw data was cleaned and transformed using Python. Key transformations include:
Normalizing columns for better analysis.
Calculating deviations in prices over time to highlight trends.
Data Analysis: The transformed data was analyzed to find the cost trends and deviations in computer memory and storage prices over the years.
Visualization: The final step involved visualizing the data to better understand the trends and identify any significant patterns or deviations.
Getting Started
To get started with this project, follow these steps:

Prerequisites
You need to have Python 3.x installed on your system. You will also need to install the following Python libraries:

pandas – for data manipulation.
You can install it using pip:

bash
Copy code
pip install pandas 
Running the Code
Clone the Repository:

First, clone the repository to your local machine using Git:

bash
Copy code
git clone https://github.com/yourusername/your-repository-name.git
Navigate to the Project Directory:

Go into the project directory:

bash
Copy code
cd your-repository-name
Run the Python Script:

The main Python script to run the transformation and visualization is data_preparation.py. To execute the script, run:

bash
Copy code
python data_preparation.py
This will:

Load the dataset.
Perform data transformations.
Generate visualizations of price deviations over time.
View the Visualizations:

After running the script, you will see plots saved in the project directory, which visualize the trends in memory and storage prices.

Data Source
The data used in this project comes from Our World in Data, which is an open-access resource that provides a collection of datasets covering a wide range of global topics.

Dataset URL: https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Our World in Data for providing the dataset.
Libraries like Pandas, Matplotlib, and Numpy for making the analysis and visualization easy.
Contributing
Feel free to fork this repository, make your improvements or fixes, and create a pull request. Contributions are welcome!

Notes:
Replace yourusername and your-repository-name with your actual GitHub username and repository name.
If your project contains more specific steps or instructions (such as additional files or dependencies), feel free to expand on this template.
Ensure the script name matches the file in your repository (if it’s not data_preparation.py, update the README accordingly).
You may also want to explain any assumptions made during the transformation or any specific decisions in the code (e.g., how you dealt with missing data, outliers, etc.).
