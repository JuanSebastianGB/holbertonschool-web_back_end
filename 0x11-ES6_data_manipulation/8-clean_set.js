const cleanSet = (set, starString) => {
  if (typeof set !== 'object') return '';
  if (typeof starString !== 'string') return '';
  if (starString === '') return '';

  const temporalArray = Array.from(set);
  const filteredArray = temporalArray.filter(
    (el) => el !== undefined && el.startsWith(starString),
  );
  return filteredArray.map((element) => element.replace('bon', '')).join('-');
};
export default cleanSet;
