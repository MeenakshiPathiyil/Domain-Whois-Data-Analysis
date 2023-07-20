# Domain Whois Data Analysis
This program allows you to analyze domain names by retrieving 'whois' data and creating a dataframe for further analysis. It is designed to help users filter out useful information from the collected data, particularly in the context of information security.

## Features
* **Domain Input**: Accepts a CSV file containing a list of domain names.
* **Whois Data Retrieval**: Queries the WHOIS database to fetch information about the provided domains.
* **Dataframe Creation**: Generates a dataframe with relevant 'whois' data for analysis.
* **Flexible Filtering**: Enables users to filter the dataframe based on specific criteria.
* **Information Security Analysis**: Assists in identifying potentially malicious or suspicious domains.
* **Exporting Results**: Provides options to export the filtered data or the complete dataframe.

## Installation
To use this program, you need to have Python 3.7 installed on your machine. Follow these steps to get started:

1. Clone this repository to your local machine:

   `git clone https://github.com/MeenakshiPathiyil/Domain-Whois-Data-Analysis.git`

2. Navigate to the project directory:

   `cd Domain-Whois-Data-Analysis`

3. Install the required Python packages:

   `pip install -r requirements.txt`

## Usage
1. Prepare a CSV file called domain.csv with a list of domain names, with each domain in a seperate row.
2. This file must be there in the same folder as the python program.
3. Run the program by executing the following command.

   `python3 <DNS-Analyzer-Vx.0.py>`

4. The program will retrieve the 'whois' data for each domain and create a dataframe.
5. You can export the complete dataframe and apply filters to it to extract useful information and further analysis. Examples of filters include domain registrar, creation date, etc.

## Contribution
Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## Acknowledgements
* [**Python Whois Library**](https://pypi.org/project/python-whois/) - Used to retrieve 'whois' data.
* [**Pandas Library**](https://pandas.pydata.org/) - Used for data manipulation and analysis.

## Why it is Useful in Terms of Information Security
The Domain Whois Data Analysis program is particularly useful in the context of information security due to the following reasons:
1. **Identification of Malicious Domains**: By retrieving 'whois' data and analyzing it, the program assists in identifying potentially malicious or suspicious domains. Characteristics such as recently registered domains, anonymous registrars, or suspicious contact information can be indicators of malicious intent.

2. **Investigation of Phishing Attempts**: Phishing attacks often involve deceptive domain names that mimic legitimate websites. By analyzing the 'whois' data, users can detect unusual patterns, such as slight variations in domain names, that may indicate phishing attempts.

3. **Data-driven Risk Assessment**: A data-driven approach enables security analysts to identify patterns, correlations, and anomalies, providing a more comprehensive assessment of information security risks associated with specific domains or domain types.

By leveraging the capabilities of this program, security professionals can enhance their information security practices, detect potential threats, and make more informed decisions to protect their systems, networks, and users.


