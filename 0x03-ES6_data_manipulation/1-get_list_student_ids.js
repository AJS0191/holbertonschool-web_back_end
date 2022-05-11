export default function getListStudentIds(anArray) {
  if (anArray instanceof Array) {
    const idArray = [];
    anArray.map((student) => { idArray.push(student.id); return idArray; });
    return idArray;
  }
  return [];
}
