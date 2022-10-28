function calculateNumber(a, b, type) {
  if (type == 'SUM') {
    return Number(a.toFixed(0)) + Number(b.toFixed(0))
  }
  if (type == 'SUBTRACT') {
    return Number(b.toFixed(0)) - Number(a.toFixed(0))
  }
  if (type == 'DIVIDE') {
    if (Number(b.toFixed(0)) == 0) {
      return 'Error'
    } else {
      c = Number(a.toFixed(0)) / Number(b.toFixed(0))
      return Number(c.toFixed(2))
    }
  }
}

module.exports = calculateNumber
