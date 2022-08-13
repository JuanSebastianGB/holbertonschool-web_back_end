const fs = require('fs');

const countStudents = (path) => {
  try {
    const response = fs.readFileSync(path, 'utf8');
    const students = response.split('\n').map((student) => student.split(','));
    students.shift();
    const fields = {};
    console.log(`Number of students: ${students.length}`);

    students.forEach((student) => {
      if (student[3] in fields) fields[student[3]].push(student[0]);
      else fields[student[3]] = [student[0]];
    });

    Object.keys(fields).forEach((field) => {
      let message = `Number of students in ${field}: ${fields[field].length}.`;
      message += ` List: ${fields[field].join(', ')}`;
      console.log(message);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
