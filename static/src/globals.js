export function callback(that,response,func) {
  var router = that.$router;
  if (response.status == '500') {
    router.push({ name: '500' });
  }else if (response.status == '404') {
    router.push({ name: '404' });
  }else if (response.status == '403') {
    router.push({ name: '403' });
  }else {
    func(that);
  }
}

export function lazyload(name) {
  return function(resolve) {
    require(['components/' + name], resolve);
  };
}

// export default {callback,lazyload};
