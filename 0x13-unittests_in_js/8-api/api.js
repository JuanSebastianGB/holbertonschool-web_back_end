const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 7865;

app.use(cors());

app.get('/', (req, res) => res.send('Welcome to the payment system'));

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});
