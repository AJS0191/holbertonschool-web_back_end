export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const gradedStudents = studentList.filter((student) => student.location === city).map(
    (student) => {
      const newStudent = {};
      newStudent.id = student.id;
      newStudent.firstName = student.firstName;
      newStudent.location = student.location;
      for (let i = 0; newGrades[i] !== undefined; i += 1) {
        if (newGrades[i].studentId === newStudent.id) {
          newStudent.grade = newGrades[i].grade;
        } else if (newStudent.grade === undefined) {
          newStudent.grade = 'N/A';
        }
      }
      return newStudent;
    },
  );
  return gradedStudents;
}
