export default function createInt8TypedArray(length, position, number) {
  const int8 = new ArrayBuffer(10);
  if (position > 9 || position < 0) {
    throw new Error('Position outside range');
  }
  const view = new DataView(int8);
  view.setInt8(position, number);
  return view;
}
