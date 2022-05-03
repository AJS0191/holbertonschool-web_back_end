export default function createEmployeesObject(departmentName, employees) {
  const deptList = {
    [departmentName]: [
      ...employees,
    ],
  };
  return deptList;
}
