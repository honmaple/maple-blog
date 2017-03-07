function timesince (time) {
  const between = Date.now() / 1000 - Number(time);
  if (between < 3600) {
    return pluralize(~~(between / 60), ' minute');
  } else if (between < 86400) {
    return pluralize(~~(between / 3600), ' hour');
  } else if (between < 259200) {
    return pluralize(~~(between / 86400), ' day');
  } else {
    return time;
  }
}

function pluralize (time, label) {
  if (time === 1) {
    return time + label;
  }
  return time + label + 's';
}
export default {timesince};
