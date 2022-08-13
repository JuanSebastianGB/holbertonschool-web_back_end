const fs = require('fs');

const countStudents = (path) => {
  try {
    const response = fs.readFileSync(path, 'utf8');
    const students = response.split('\n');
    students.shift();
    const fields = {};

    students.map((student) => {
      const sList = student.split(',');
      if (sList[3] in fields) fields[sList[3]].push(sList[0]);
      else fields[sList[3]] = [sList[0]];
      return 0;
    });

    Object.keys(fields).map((field) => {
      const message = `Number of students in ${field}: ${
        fields[field].length
      }. List: ${fields[field].join(', ')}`;
      console.log(message);
      return 0;
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
