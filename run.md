1. Put the chromedriver browser into /venv/Scripts (Windows) or venv/bin/(Mac) folder

   For Mac
   ```bash
    py -m venv venv

2. For Windows
   ```bash
   python -m venv venv

3. Activate virtual environment
    For Mac
   ```bash
    venv/bin/activate
4. For Windows
   ```bash
    venv/Scripts/activate
5. Install requirements
    ```bash
    pip install -r requirements.txt

6. For tests execution run 
    ```bash
    pytest tests/
   