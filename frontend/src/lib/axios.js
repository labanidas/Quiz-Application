// src/lib/axios.js
import axios from 'axios';

export const axiosInstance = axios.create({
  baseURL: 'http://localhost:5000/api', 
  withCredentials: true, // Optional: If you are handling cookies or authentication
});
