function calculateNumber(a, b, type) {
  switch (type){
    case 'SUM':  
      return Math.round(a) + Math.round(b)
    case 'SUBTRACT':
    return Math.round(b) - Math.round(a)
  
    case 'DIVIDE':
      if (Math.round(b) == 0) {
        return 'Error'
      } else {
        c = Math.round(a) / Math.round(b)
        return Math.round(c)
    }
  }}
    module.exports = calculateNumber
