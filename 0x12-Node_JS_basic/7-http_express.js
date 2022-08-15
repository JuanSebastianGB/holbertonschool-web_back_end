const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => res.send('Hello Holberton School!'));
app.get('/students', async (req, res) => {
  countStudents(process.argv[2])
    .then((response) => {
      const message = `This is the list of our students\n${response}`;
      res.send(message);
    })
    .catch((err) => res.send(`${err.message}`));
});

app.listen(1245);

module.exports = app;
