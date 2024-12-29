# TapBats

A Telegram-integrated game built with Vite, React, and Flask.

---

## Getting Started

### Test Locally

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/NocturnalDevs/bats-telegram-project.git
    cd bats-telegram-project
    ```

2. **Install Packages**:

    ```bash
    npm install
    ```

3. **Run the Development Server**:

    ```bash
    npm run dev -- --host
    ```

4. **Open Your Browser**:

    Navigate to `http://localhost:5173` to see the game setup.

---

### Test on Telegram Locally (Needs access to BotFather - I can transfer Bot Ownership to someone)

5. **Install and Open Ngrok**:

    Download and install [Ngrok](https://ngrok.com/), then open it.

6. **Run Ngrok on the Same Port as Vite**:

    ```bash
    ngrok http 5173
    ```
    Copy the Ngrok URL (e.g., `https://<random>.ngrok-free.app`).

7. **Interact with Your Bot**:

    - Open Telegram and send `/start` or `/play` to your bot.
    - Test that the bot replies and the "Play Game" button redirects to your Vite app.

---

## Notes

- Ensure Ngrok is active while testing the Telegram integration.
- Replace placeholders like `<your-ngrok-url>` and bot token with your actual values.
- This setup is for development purposes; use production best practices for deployment.
