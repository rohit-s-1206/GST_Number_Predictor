# GST_Number_Predictor
# GSTIN Generator

## Overview
This project provides a Python script to generate and validate GSTIN (Goods and Services Tax Identification Number) based on a given PAN (Permanent Account Number) and state code.

## Features
- Validates the format of PAN numbers.
- Generates GSTIN based on state code, PAN, and entity number.
- Computes checksum using the official GSTIN algorithm.
- Provides a breakdown of the GSTIN components.

## Prerequisites
- Python 3.x

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/gstin-generator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd gstin-generator
   ```

## Usage
Run the script by executing the following command:
```sh
python GST_Final_Prediction_Python_Code.py
```
Follow the on-screen instructions to generate a GSTIN.

## Example Input & Output
**Input:**
```
Enter PAN number (format AAAAA9999A): ABCDE1234F

Available State Codes:
07: Delhi
09: Uttar Pradesh
...
Enter state code: 07
Enter entity number (1-9): 1
```

**Output:**
```
Generated GSTIN Details:
GSTIN: 07ABCDE1234F1Z5

Breakdown:
State Code: 07 (Delhi)
PAN: ABCDE1234F
Entity Number: 1
Z Character: Z
Checksum: 5
```

## Contributing
Feel free to submit issues and pull requests for improvements.

## License
This project is licensed under the MIT License.

