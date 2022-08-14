const http = require('http');
const countStudents = require('./3-read_file_async');

const PORT = 1245;

const requestListener = (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  const { url } = req;
  if (url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
  if (url === '/students') {
    countStudents(process.argv[2])
      .then((response) => {
        res.write(`This is the list of our students\n${response}`);
        res.end();
      })
      .catch((err) => res.end(`${err}\n`));
  }
};

const app = http.createServer(requestListener);

app.listen(PORT, () => {
  console.log('...');
});

module.exports = app;
