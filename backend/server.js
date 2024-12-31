const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const port = 5000;

// Middleware to parse JSON requests
app.use(express.json());

// Connect to SQLite database
const dbPath = path.join(__dirname, 'database', 'game.db');
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Error connecting to the database:', err.message);
    } else {
        console.log('Connected to the SQLite database.');
    }
});

// Create tables (if they don't exist)
db.serialize(() => {
    db.run(`
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            gem_count INTEGER DEFAULT 0,
            nocturnal_level TEXT DEFAULT 'Fledgling'
        )
    `);
});

// API Endpoints

// Get user data
app.get('/api/user/:username', (req, res) => {
    const { username } = req.params;

    db.get('SELECT * FROM users WHERE username = ?', [username], (err, row) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        if (!row) {
            return res.status(404).json({ error: 'User not found' });
        }
        res.json(row);
    });
});

// Update user data (e.g., gem count or level)
app.post('/api/user/:username/update', (req, res) => {
    const { username } = req.params;
    const { gemCount, nocturnalLevel } = req.body;

    db.run(
        'UPDATE users SET gem_count = ?, nocturnal_level = ? WHERE username = ?',
        [gemCount, nocturnalLevel, username],
        function (err) {
            if (err) {
                return res.status(500).json({ error: err.message });
            }
            if (this.changes === 0) {
                return res.status(404).json({ error: 'User not found' });
            }
            res.json({ message: 'User updated successfully' });
        }
    );
});

// Create a new user
app.post('/api/user', (req, res) => {
    const { username } = req.body;

    db.run('INSERT INTO users (username) VALUES (?)', [username], function (err) {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        res.json({ id: this.lastID, username });
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});