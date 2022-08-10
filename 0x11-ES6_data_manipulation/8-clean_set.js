const cleanSet = (set, starString) => {
  if (typeof set !== 'object') return '';
  if (typeof starString !== 'string') return '';
  if (starString.length === 0) return '';

  const resultList = [];
  set.forEach((el) => {
    if (el !== undefined && el.startsWith(starString)) {
      const processedElement = el.replace('bon', '');
      resultList.push(processedElement);
    }
  });
  return resultList.join('-');
};
export default cleanSet;
