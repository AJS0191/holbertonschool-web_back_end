import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(studentList) {
  const idArray = getListStudentIds(studentList);
  return idArray.reduce((total, num) => total + num);
}
