# yalan-dunya-web-app

## How to run it locally?
- Be sure that you have python3, pip3, virtualenv

 
```bash
virtualenv --python=python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
```

- Rename the `config.py.sample` to `config.py` and edit the file with the needed credentials

- Then;
```bash
python run.py
```

- Now check `http://0.0.0.0:8080/`
