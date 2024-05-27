// request_login.ts
import axios from 'axios';

interface LoginResponse {
  access_token: string;
  token_type: string;
}

const login = async (username: string, password: string): Promise<LoginResponse> => {
  try {
    const response = await axios.post<LoginResponse>('http://127.0.0.1:8000/auth/token', {
      username: username,
      password: password,
    });

    return response.data;
  } catch (error) {
    console.error('Error logging in:', error);
    throw new Error('Invalid credentials');
  }
};

export default login;

