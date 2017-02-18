const API = {
  api_prefix: 'http://127.0.0.1:5000',
  create: function() {
    return {
      bloglist: this.api_prefix + '/blog/',
      categorylist: this.api_prefix + '/blog/category/',
      taglist: this.api_prefix + '/blog/tag/',
      book:this.api_prefix + '/book/',
      timeline:this.api_prefix + '/timeline/'
    }
  }
};
export default API.create()
// const api_prefix = 'http://127.0.0.1:5000'
// const api = {
//     bloglist: api_prefix + '/blog',
//     categorylist: api_prefix + '/blog/category'
// }
