const express = require('express');
const router = express.Router();

// Mock route for plumbing advice
router.get('/', (req, res) => {
  res.json({ advice: 'Always turn off the main water supply before any repair.' });
});

// More routes can be added here as needed

module.exports = router;

