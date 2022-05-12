export default function hasValuesFromArray(set, anArray) {
  for (const i in anArray) {
    if (set.has(anArray[i]) === false) {
      return false;
    }
  }
  return true;
}
