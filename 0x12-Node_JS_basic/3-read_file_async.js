const fs = require('fs');

const countStudents = async (path) => {
  const newPromise = new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) reject(new Error('Cannot load the database'));
      const students = data.split('\n').map((student) => student.split(','));
      students.shift();
      console.log(`Number of students: ${students.length}`);
      const fields = {};

      students.forEach((student) => {
        if (student[3] in fields) fields[student[3]].push(student[0]);
        else fields[student[3]] = [student[0]];
      });

      const fieldList = Object.keys(fields);
      fieldList.forEach((field) => {
        console.log(
          `Number of students in ${field}: ${
            fields[field].length
          }. List: ${fields[field].join(', ')}`,
        );
      });
      resolve(students);
    });
  });

  return newPromise;
};

module.exports = countStudents;
