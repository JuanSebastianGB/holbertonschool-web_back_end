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
      let message = `Number of students: ${students.length}\n`;
      const fields = {};

      students.forEach((student) => {
        if (student[3] in fields) fields[student[3]].push(student[0]);
        else fields[student[3]] = [student[0]];
      });

      const fieldList = Object.keys(fields);
      fieldList.forEach((field) => {
        message += `Number of students in ${field}: ${fields[field].length}.`;
        message += ` List: ${fields[field].join(', ')}\n`;
      });
      console.log(message);
      resolve(message);
    });
  });

  return newPromise;
};

module.exports = countStudents;
