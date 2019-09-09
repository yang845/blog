import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  // console.log(config)
  config.params = {
    ...config.params,
    // appkey: ''
  }
  return config
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error)
})

export default axios
