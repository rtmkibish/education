function isDuplicate(left, right) {
  const leftKeys = Object.keys(left);
  const rightKeys = Object.keys(right);

  if (leftKeys.length - rightKeys.length !== 0) return false;

  for (let key of leftKeys) {
    if (typeof left[key] == 'object' && typeof right[key] == 'object') {
      if (!isDuplicate(left[key], right[key])) {
        return false;
      }
    } else if (left[key] !== right[key]) {
      return false;
    }
  }
  return true;

}
