const API = {
  api_prefix: 'http://127.0.0.1:5000/api',
  api:{
    bloglist: '/blog/',
    categorylist: '/blog/category/',
    blogtimelist: '/blog/time/',
    blogarchives: '/blog/archives',
    taglist: '/blog/tag/',
    book:'/book/',
    book_tag:'/book/tags',
    timeline:'/timeline/'
  },
  create: function() {
    Object.keys(this.api).forEach(key => {
      this.api[key] = this.api_prefix + this.api[key];
    });
    return this.api;
  }
};

export default API.create();
