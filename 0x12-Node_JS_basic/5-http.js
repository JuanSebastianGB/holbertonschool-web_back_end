const http = require('http');
const countStudents = require('./3-read_file_async');

const PORT = 1245;

const requestListener = async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  const { url } = req;
  if (url === '/') res.end('Hello Holberton School!');
  if (url === '/students') {
    countStudents(process.argv[2])
      .then((data) => res.end(`This is the list of our students\n${data}`))
      .catch((err) => res.end(`${err.message}\n`));
  }
};

const app = http.createServer(requestListener);

app.listen(PORT);

module.exports = app;
