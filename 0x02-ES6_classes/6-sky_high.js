import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super();
    this._sqft = sqft;
    if (typeof floors === 'number') {
      this._floors = floors;
    }
  }

  get floors() {
    return this._floors;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
