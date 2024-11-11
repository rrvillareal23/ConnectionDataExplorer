# NetworkConnectionAnalyzer

## Overview

**NetworkConnectionAnalyzer** is a Python project that loads network connection data from a CSV file and provides tools to analyze, filter, and visualize key connection metrics. The project reads data from an IP connection log, filters out irrelevant entries, pairs connection data with various metrics, and plots visualizations of these relationships.

This project leverages the **Pandas** library for data manipulation and **Matplotlib** for creating visualizations, making it easy to observe and analyze network traffic patterns and other connection-related information.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Customization](#customization)
- [License](#license)

## Features

- **Data Loading**: Reads data from a CSV file (`IP-CONNECT.csv`) into a Pandas DataFrame.
- **Data Filtering**: Filters out rows containing IPv6 addresses.
- **Column Pairing**: Creates paired DataFrames between the "CONNECTION" column and specified columns related to connection types (e.g., `TCP`, `UDP`, `ARP`, etc.).
- **Data Visualization**: Generates horizontal bar charts for each paired DataFrame, making it easy to visualize and analyze the distribution of connection types across various metrics.

## Requirements

To run this project, you need the following Python libraries:

- **Pandas**: `pip install pandas`
- **Matplotlib**: `pip install matplotlib`

You can install these dependencies by running:

pip install pandas matplotlib

## Usage

1. Clone this repository to your local machine.
2. Place your CSV file (`IP-CONNECT.csv`) in the same directory as the script.
3. Run the script:python network_connection_analyzer.py

### How It Works

1. The script reads `IP-CONNECT.csv` into a Pandas DataFrame and displays the columns.
2. It filters out IPv6 rows, showing only IPv4 data for analysis.
3. For each specified metric in the `columns_to_pair` list, the script creates a new paired DataFrame with the `CONNECTION` column and the metric column.
4. It then generates a horizontal bar chart for each pairing, visualizing the number of observations for each connection type in relation to the specified metric.

## Sample Output

After running the script, you’ll see output in the terminal, including:
- A list of the columns in the DataFrame
- Sample data rows (first 10 rows)
- Paired DataFrames printed for each column pairing
- Horizontal bar charts for each connection pairing

These charts display the relationship between the `CONNECTION` type and the chosen metric, making it easier to interpret the network traffic patterns.

## Customization

- **Add More Columns**: Modify the `columns_to_pair` list to analyze additional metrics.
- **Adjust Display Settings**: Update `pd.set_option` configurations to change display width, row count, or column count as needed.
- **Modify Plots**: Customize the `plt.barh` settings to adjust chart appearance (color, labels, size, etc.).

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Enjoy analyzing your network connection data with NetworkConnectionAnalyzer!** 

For any questions or improvements, feel free to open an issue or make a pull request.

