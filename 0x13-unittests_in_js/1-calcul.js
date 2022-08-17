const calculateNumber = (type, a, b) => {
  switch (type) {
    case 'SUM':
      return Math.round(a) + Math.round(b);
    case 'SUBTRACT':
      return Math.round(a) - Math.round(b);
    case 'DIVIDE':
      if (b === 0) return 'Error';
      const result = Math.round(a) / Math.round(b);
      return Number.parseFloat(result.toFixed(2));
    default:
      break;
  }
};

module.exports = calculateNumber;
