const updateUniqueItems = (incomingMap) => {
  incomingMap.forEach((value, key) => {
    if (value === 1) incomingMap.set(key, 100);
  });
};
export default updateUniqueItems;
