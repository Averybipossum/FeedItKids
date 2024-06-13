// import React from 'react';
// import { render, screen, fireEvent, waitFor } from '@testing-library/react';
// import axios from 'axios';
// import MockAdapter from 'axios-mock-adapter';
// import Home from './Home'; // Ajuste o caminho se necessário

// const mock = new MockAdapter(axios);

// describe('Home Component', () => {
//   it('should call the API and handle login success', async () => {
//     mock.onPost('http://127.0.0.1:8000/auth/token').reply(200, {
//       acess_token: 'test-token',
//     });
    
//     render(<Home />);
    
//     fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
//     fireEvent.change(screen.getByPlaceholderText('Senha'), { target: { value: 'password123' } });
    
//     fireEvent.click(screen.getByText('Entrar'));
    
//     await waitFor(() => {
//       expect(screen.getByText('Token de acesso: test-token')).toBeInTheDocument();
//     });
//   });

//   it('should show error when login fails', async () => {
//     mock.onPost('http://127.0.0.1:8000/auth/token').reply(401);
    
//     render(<Home />);
    
//     fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
//     fireEvent.change(screen.getByPlaceholderText('Senha'), { target: { value: 'password123' } });
    
//     fireEvent.click(screen.getByText('Entrar'));
    
//     await waitFor(() => {
//       expect(screen.getByText('Não foi possível fazer login. Verifique suas credenciais e tente novamente.')).toBeInTheDocument();
//     });
//   });
// });