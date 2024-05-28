/*
Name: James Hinson
Course: CS290 - Web Development
File: index.js
Date: 5/28/2024
*/

'use strict';

const express = require('express');
const app = express();
const PORT = 3000;

// Middleware for URL encoding
app.use(express.urlencoded({ extended: true }));

// Middleware to serve static files from the "public" directory
app.use(express.static('public'));

let htmlTop = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission Result</title>
    <link rel="stylesheet" type="text/css" media="screen" href="main.css">
    <script src="main.js"></script>
</head>
<body>
    <header>
        <h1>James Hinson</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="contact.html">Contact</a>
            <a href="interests.html">Interests</a>
            <a href="style.html" target="_blank">Style</a>
        </nav>
    </header>
    <main>
`;

let htmlBottom = `
    </main>
    <footer>
        <p>&copy; 2024 Oregon State University - CS 290 Web Development</p>
    </footer>
</body>
</html>
`;

app.post('/submit-form', (req, res) => {
    const name = req.body.name;
    const email = req.body.email;
    const message = req.body.message;
    const about = req.body.about;
    const urgency = req.body.urgency;

    res.send(`
        ${htmlTop}
        <section>
            <h2>Form Submission Results</h2>
            <p>Thank you, ${name}, for reaching out to us.</p>
            <p>We have received your message regarding "${about}". We will respond to your ${urgency} message at ${email} as soon as possible.</p>
            <p><strong>Your Message:</strong></p>
            <p>${message}</p>
        </section>
        ${htmlBottom}
    `);
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
