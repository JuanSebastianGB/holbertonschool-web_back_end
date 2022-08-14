const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const PORT = 1245;

app.get('/', (req, res) => res.send('Hello Holberton School!'));
app.get('/students', async (req, res) => {
  try {
    const students = await countStudents(process.argv[2]);
    res.send(`This is the list of our students\n${students}`);
  } catch (err) {
    res.end(`${err}\n`);
  }
});

app.listen(PORT, () => {
  console.log('...');
});

module.export = app;
