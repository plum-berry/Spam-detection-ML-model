# Spam Detection ML Model

A machine learning model that detects whether a given message is spam or not. This project uses the [Spambase dataset](https://archive.ics.uci.edu/ml/datasets/spambase) and implements a Logistic Regression classifier from [scikit-learn](https://scikit-learn.org/stable/index.html).

The trained model is saved as `Spam_detect.pkl` and is loaded via `main.py` to classify sample inputs.

## 🚀 Getting Started

### Clone this repository
```bash
git clone https://github.com/plum-berry/Spam-detection-ML-model.git
cd Spam-detection-ML-model
```
### Create a virtual environement
```
python -m venv venv_name
```
### Activate the virtual environment
For Powershell
```
venv_name\Scripts\Activate.ps1
```
For CMD
```
venv-name\Scripts\activate.bat
```
## Installing dependencies
```
pip intall -r "requirements.txt"
```
## Running the Spam detection python application
```
python main.py
```
The application will load the trained model and display whether a sample input is spam or not.

## 📝 Requirements

- Python 3.8+
- sciki-learn
- numpy
- pandas
