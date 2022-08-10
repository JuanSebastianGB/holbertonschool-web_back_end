const cleanSet = (set, starString) => {
  if (starString === undefined || starString === '') return '';
  const temporalArray = Array.from(set);
  const filteredArray = temporalArray.filter(
    (el) => el !== undefined && el.includes(starString),
  );
  return filteredArray.map((element) => element.replace('bon', '')).join('-');
};
export default cleanSet;
