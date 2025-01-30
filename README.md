## TP Cours 1
### Question 1 :
#### Say you want to run a command that needs the virtual environment to be activated and you do not want, or can't, use uv. How do you activate it ?
Using venv command
```python -m venv --activate /path/to/your/env ```

### Question 2
#### You want to install the version 1.40.0 of streamlit. How would you remove the 1.41.1 version and add this specific version ?
1. Uninstall the existing Streamlit version
```uv uninstall streamlit```

2. Install the specific version (1.40.0)
```uv install streamlit==1.40.0```


3. Write a command in your makefile to run the frontend.
```.PHONY: frontend
frontend:
	python3 -m streamlit run main.py```
puis
```make frontend``` dans l'invite de commande

coucou le hibou
