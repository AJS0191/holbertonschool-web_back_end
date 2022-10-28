function calculateNumber(a, b, type) {
  if (type == 'SUM') {
    return Number(a.toFixed(0)) + Number(b.toFixed(0))
  }
  if (type == 'SUBTRACT') {
    return Number(b.toFixed(0)) - Number(a.toFixed(0))
  }
  if (type == 'DIVIDE') {
    if (b == 0) {
      return 'Error'
    } else {
      return Number(a.toFixed(0)) / Number(b.toFixed(0))
    }
  }
}

module.exports = calculateNumber
