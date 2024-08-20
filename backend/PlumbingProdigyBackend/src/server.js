require('dotenv').config();

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Modularized Routes
const plumbingAdviceRoutes = require('./routes/plumbingAdviceRoutes');

// Use Routes
app.use('/api/v1/plumbing-advice', plumbingAdviceRoutes);

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
