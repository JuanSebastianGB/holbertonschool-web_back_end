const fs = require('fs');

const countStudents = (path) => {
  const newPromise = new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const students = data
        .trim()
        .split('\n')
        .map((student) => student.split(','));
      students.shift();

      const messagesList = [];
      messagesList.push(`Number of students: ${students.length}`);
      const fields = {};

      students.forEach((student) => {
        if (student[3] in fields) fields[student[3]].push(student[0]);
        else fields[student[3]] = [student[0]];
      });

      const fieldList = Object.keys(fields);
      fieldList.forEach((field) => {
        let message = `Number of students in ${field}: ${fields[field].length}.`;
        message += ` List: ${fields[field].join(', ')}`;
        messagesList.push(message);
      });
      const customMessage = messagesList.join('\n');
      console.log(customMessage);
      resolve(customMessage);
    });
  });

  return newPromise;
};

module.exports = countStudents;
