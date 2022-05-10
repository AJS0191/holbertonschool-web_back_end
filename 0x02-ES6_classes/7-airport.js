export default class Airport {
  constructor(name, code) {
    if (typeof name === 'string') {
      this._name = name;
    }
    if (typeof code === 'string') {
      this._code = code;
    }
  }

  description() {
    return `${this.constructor} [${this._code}] ${this}`;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
