## IMPORTANT
- Use vscode and install github extension for easy push and pull request

---

## Running the Project Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/NocturnalDevs/tapbats-project.git
   cd tapbats-project
   ```

2. **Install Frontend Dependencies**
   ```bash
   npm install
   ```

3. **Start the Frontend**
   ```bash
   cd frontend
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

## Running the Game on Telegram

1. **Install ngrok**
   Download from [ngrok's website](https://ngrok.com/).

2. **Expose Local Port**
   ```bash
   ngrok http 5173
   ```

3. **Update Web App URL**
   - Open Telegram, search for `BotFather`, and type `/myapps`.
   - Select the TapBats bot and update the web app URL with the ngrok URL (e.g., `https://abcd1234.ngrok.io`).

---

## Setting Up the Backend

1. **Navigate to the Backend**
   ```bash
   cd backend
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. **Install Dependencies**
   Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   **If Installation Fails:**
   Manually install each dependency:
   ```bash
   pip install fastapi
   pip install uvicorn
   pip install sqlalchemy
   pip install psycopg2-binary
   pip install python-dotenv
   ```

4. **Set Up Environment Variables**
   Create a `.env` file:
   ```plaintext
   DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_database
   ```

5. **Manually Set `DATABASE_URL` (If Connection Fails)**
   If the database connection is not working, manually set the `DATABASE_URL` in the following files:

   - **File 1: `backend/database/connection.py`**
     Update the file as follows:
     ```python
     import os

     # DATABASE_URL = os.getenv("DATABASE_URL")  # Comment out this line
     DATABASE_URL = "postgresql://username:password@localhost:5432/database"  # Uncomment and replace with your credentials
     ```

   - **File 2: `backend/utils/initialize_database.py`**
     Update the file as follows:
     ```python
     import os

     # DATABASE_URL = os.getenv("DATABASE_URL")  # Comment out this line
     DATABASE_URL = "postgresql://username:password@localhost:5432/database"  # Uncomment and replace with your credentials
     ```

6. **Update `allow_origin` in `main.py`**
   Open `backend/main.py` and update the `allow_origins` parameter in the `CORSMiddleware` with your ngrok URL:
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["https://abcd1234.ngrok.io"],  # Replace with your ngrok URL
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

7. **Run the Backend Server**
   ```bash
   uvicorn main:app --reload
   ```
   Access the API docs at `http://localhost:8000/docs`.

8. **Update `requirements.txt` (Optional)**
   If you installed additional packages, update the `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

---

## Initialize Database and Create Tables

1. **Run the Database Initialization Script**
   ```bash
   python backend/utils/initialize_database.py
   ```

---

## Git Workflow

### **Development Device**
1. **Stage and Commit Changes**
   ```bash
   git add .
   git commit -m "Your commit message"
   ```

2. **Push to `develop` Branch**
   ```bash
   git push origin develop
   ```

### **Deployment Device**
3. **Pull from `develop` Branch**
   ```bash
   git pull origin develop
   ```

### **Optional: Merge `develop` into `main`**
4. **Switch to `main` and Merge**
   ```bash
   git checkout main
   git merge develop
   git push origin main
   ```

5. **Pull from `main` on Deployment Device**
   ```bash
   git pull origin main
   ```

---

## Summary
- frontend is running on port 5173 and its services are interacting with port 8000
- backend is running on port 8000
- ngrok is running on port 5173
- ngrok url is copied to WebApp URL on BotFather and main.py on backend

---

## Notes
- Use `develop` for development and `main` for stable releases.
- Always pull before pushing to avoid conflicts.
- Ensure PostgreSQL is running and the database is set up.
- Keep your ngrok URL updated in both the Telegram BotFather and the `allow_origins` setting in `main.py`.
- If the database connection fails, manually set the `DATABASE_URL` in `backend/database/connection.py` and `backend/utils/initialize_database.py`.

---