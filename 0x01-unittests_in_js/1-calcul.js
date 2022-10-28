function calculateNumber(a, b, type) {
  if (type == 'SUM') {
    return Math.round(a) + Math.round(b)
  }
  if (type == 'SUBTRACT') {
    return Math.round(b) - Math.round(a)
  }
  if (type == 'DIVIDE') {
    if (Math.round(b) == 0) {
      return 'Error'
    } else {
      c = Math.round(a) / Math.round(b)
      return Math.round(c)
    }
  }
}

module.exports = calculateNumber
