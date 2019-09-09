import axios from '@/axios'

let api = {
  getArticles(params) {
    return axios
      .get('/api/v1/posts/', {
        params
      })
  },
  getArticle(id) {
    return axios
      .get('/api/v1/post/' + id)
  },
  getComments(id, params) {
    return axios
      .get('/api/v1/post/'+id+'/comments/', {params})
  },
  postComment(id, params) {
    return axios
      .post('/api/v1/post/'+id+'/comment/', params, {
        headers: {'Content-Type': 'application/json'} 
    })
  },
  likeArticle(params) {
    return axios
      .get('/api/v1/likes/', {params})
  },
  getArchives() {
    return axios
      .get('/api/v1/archives/')
  },
  getFriends() {
    return axios
      .get('/api/v1/friends/')
  },
  postFriend(params) {
    return axios
      .post('/api/v1/friend/', params, {
        headers: {'Content-Type': 'application/json'} 
    })
  },
  getMessages(params) {
    return axios
      .get('/api/v1/messages/', {params})
  },
  postMessage(params) {
    return axios
      .post('/api/v1/message/', params, {
        headers: {'Content-Type': 'application/json'} 
    })
  },
}

export default api
