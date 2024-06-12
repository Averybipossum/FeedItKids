// import React from 'react';
// import { render, fireEvent, waitFor } from '@testing-library/react-native';
// import axios from 'axios';
// import MockAdapter from 'axios-mock-adapter';
// import Home from './Home'; // Ajuste o caminho se necessário

// const mock = new MockAdapter(axios);

// describe('Home Component', () => {
//   it('should show error when passwords do not match', async () => {
//     const { getByPlaceholderText, getByText } = render(<Home />);

//     fireEvent.changeText(getByPlaceholderText('Email'), 'test@example.com');
//     fireEvent.changeText(getByPlaceholderText('Senha'), 'password123');
//     fireEvent.changeText(getByPlaceholderText('Confirme a senha'), 'password456');

//     fireEvent.press(getByText('Entrar'));

//     await waitFor(() => {
//       expect(getByText('As senhas não correspondem')).toBeTruthy();
//     });
//   });

//   it('should call the API and handle success', async () => {
//     mock.onPost('http://127.0.0.1:8000/usuarios/usuarios/').reply(200, {
//       email: 'test@example.com',
//       id_usuario: 1,
//       pontuacao_total: 0
//     });

//     const { getByPlaceholderText, getByText } = render(<Home />);

//     fireEvent.changeText(getByPlaceholderText('Email'), 'test@example.com');
//     fireEvent.changeText(getByPlaceholderText('Senha'), 'password123');
//     fireEvent.changeText(getByPlaceholderText('Confirme a senha'), 'password123');

//     fireEvent.press(getByText('Entrar'));

//     await waitFor(() => {
//       expect(console.log).toHaveBeenCalledWith('Usuário criado', {
//         email: 'test@example.com',
//         id_usuario: 1,
//         pontuacao_total: 0
//       });
//     });
//   });

//   it('should show error when API call fails', async () => {
//     mock.onPost('http://127.0.0.1:8000/usuarios/usuarios/').reply(400, {
//       detail: 'Erro ao fazer cadastro'
//     });

//     const { getByPlaceholderText, getByText } = render(<Home />);

//     fireEvent.changeText(getByPlaceholderText('Email'), 'test@example.com');
//     fireEvent.changeText(getByPlaceholderText('Senha'), 'password123');
//     fireEvent.changeText(getByPlaceholderText('Confirme a senha'), 'password123');

//     fireEvent.press(getByText('Entrar'));

//     await waitFor(() => {
//       expect(getByText('Não foi possível fazer cadastro. Verifique se já não possui uma conta registrada.')).toBeTruthy();
//     });
//   });
// });
