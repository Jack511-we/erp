// 通用请求封装
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:5000/api',
  timeout: 10000,
});


instance.interceptors.request.use((config) => {
  // 可在此添加 token、header 等
  return config;
});


instance.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error)
);

export function request<T = any>(config: any): Promise<any> {
  return Promise.resolve(instance.request(config));
}

export default instance;
