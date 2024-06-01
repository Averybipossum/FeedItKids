// authStorage.ts

import AsyncStorage from '@react-native-async-storage/async-storage';

const TOKEN_KEY = 'accessToken';
const USER_DATA_KEY = 'userData';

export const saveTokenToStorage = async (token: string) => {
  try {
    await AsyncStorage.setItem(TOKEN_KEY, token);
  } catch (error) {
    console.error('Error saving token to storage:', error);
    throw error;
  }
};

export const getTokenFromStorage = async (): Promise<string | null> => {
  try {
    const token = await AsyncStorage.getItem(TOKEN_KEY);
    return token;
  } catch (error) {
    console.error('Error getting token from storage:', error);
    throw error;
  }
};

export const saveUserDataToStorage = async (userData: any) => {
  try {
    const jsonUserData = JSON.stringify(userData);
    await AsyncStorage.setItem(USER_DATA_KEY, jsonUserData);
  } catch (error) {
    console.error('Error saving user data to storage:', error);
    throw error;
  }
};

export const getUserDataFromStorage = async (): Promise<any | null> => {
  try {
    const jsonUserData = await AsyncStorage.getItem(USER_DATA_KEY);
    if (jsonUserData) {
      return JSON.parse(jsonUserData);
    }
    return null;
  } catch (error) {
    console.error('Error getting user data from storage:', error);
    throw error;
  }
};

export const clearStorage = async () => {
  try {
    await AsyncStorage.clear();
  } catch (error) {
    console.error('Error clearing storage:', error);
    throw error;
  }
};

export const getUserIdFromStorage = async (): Promise<number | null> => {
    try {
      const jsonUserData = await AsyncStorage.getItem(USER_DATA_KEY);
      if (jsonUserData) {
        const userData = JSON.parse(jsonUserData);
        return userData.id_usuario; // Return only the id_usuario
      }
      return null;
    } catch (error) {
      console.error('Error getting user ID from storage:', error);
      throw error;
    }
  };

//   import { getUserIdFromStorage } from './authStorage';

// const getUserIdAndUseAsVariable = async () => {
//     try {
//       const userId = await getUserIdFromStorage();
//       if (userId) {
//         console.log('ID do usuário:', userId);

//       } else {
//         console.log('ID do usuário não encontrado.');
//       }
//     } catch (error) {
//       console.error('Erro ao obter o ID do usuário:', error);
//     }
//   };
  
//   // Call the function to get the id_usuario and use it as a variable
//   getUserIdAndUseAsVariable();