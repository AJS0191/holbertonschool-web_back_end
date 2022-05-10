export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() { return this.contructor; }

  cloneCar() {
    const clone = new this.constructor();
    return clone;
  }
}
