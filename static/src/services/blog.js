import api from 'api'

export default {
  methods: {
    getItemList: function(query) {
      return this.$http.get(api.bloglist,{params:query});
    },
    getItem: function(blogId) {
      return this.$http.get(api.bloglist + blogId)
    },
    getCategoryList: function(query) {

    },
    getTagList: function(query) {

    },
    getTimeList: function(query) {

    }
  }
};
