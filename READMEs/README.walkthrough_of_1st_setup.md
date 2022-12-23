# 1st walkthrough

## TLDR - walking through how to set up a Python project

Here is how you can setup some files and folders on your computer to start playing around with Python...

### Python

```.sh
brew install python
which python3 # /usr/local/bin/python3
python3 --version # 3.10.9 -> 3.10.x
python3 -m pip install --user --upgrade pip  # pip : Python :: npm : Node.js :: bundle : Ruby
which pip3 # /usr/local/bin/pip3
python3 -m pip --version # 22.3.1
```

### Virtualenv

```.sh
python3 -m pip install --user virtualenv
python3 -m virtualenv --version # 20.17.1
python3 -m venv ./venv # like the node_modules folder in Node.js land
source ./venv/bin/activate # for configuring python in you shell to install packages to project and not system
```

### Smoke test the Python setup

```.sh
touch main.py
echo "print(\"Hello World\")" > main.py
python3 main.py
python main.py
```

### Add .gitignore

`https://github.com/github/gitignore/blob/main/Python.gitignore`

- touch .gitignore

### Install some packages

```.sh
pip install pandas
pip install matplotlib
mkdir data
touch data/temperature_data.csv
```

### developing main.py further

```.py
import pandas as pd
import matplotlib.pyplot as plt

temperature_in_miami = pd.read_csv("data/temperature_data.csv", index_col=0, parse_dates=True)
temperature_in_miami.head()
temperature_in_miami.plot(figsize=(10, 6))
plt.show()
```

### finally show how to save the installed packages and deactivate venv

```.sh
pip freeze > requirements.txt
deactivate # to disable venv a use packages installed to system
python3 --version
```

### and show what the reactivation process looks like

```.sh
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt # like `npm install` or `bundle install`
```
