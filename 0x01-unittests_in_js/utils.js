const Utils = {
  calculateNumber(type, a, b) {
    switch (type){
      case 'SUM':  
        return Math.round(a) + Math.round(b)
      case 'SUBTRACT':
      return Math.round(a) - Math.round(b)
    
      case 'DIVIDE':
        if (Math.round(b) == 0) {
          return 'Error'
        } else {
          c = Math.round(a) / Math.round(b)
          return c
      }
    }
  },
};
module.exports = Utils