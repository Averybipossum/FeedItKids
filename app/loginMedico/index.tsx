import React, { useState } from "react";
import { View, Text, TextInput, Pressable, ImageBackground, Alert, Button } from "react-native";
import BGimage from "../../assets/BGmedico.png"; 
import { styles } from './styles';

import { FontAwesome6 } from '@expo/vector-icons';
import axios from "axios";
import { router } from "expo-router";

const Home = () => {
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');

    const nomePermitido = 'medico@email.com';
    const senhaPermitida = 'medico123';

    const handleLogin = async () => {

        if(nometext !== nomePermitido || senhatext !== senhaPermitida){
            console.log('Este usuário não possui as credencias para acessar esta área.')
            Alert.alert('Erro', 'Este usuário não possui as credencias para acessar esta área.')
            return;
        }

        try {
            const formData = new FormData();
            formData.append('username', nometext);
            formData.append('password', senhatext);

            const response = await axios.post('http://127.0.0.1:8000/auth/token', formData, {
                headers:{
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
            });

            console.log('Token de acesso:', response.data.acess_token);

            router.replace('/paginaRelatorio')
            
            
        } catch (error) {
            // Se houver um erro na chamada, exibir mensagem de erro
            console.error('Erro ao fazer login:', error);
            Alert.alert('Erro', 'Não foi possível fazer login. Verifique suas credenciais e tente novamente.');
        }
    };

    return (
        <View style={styles.container}>
            <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
                    <View style={styles.containerconfig}>
                        <FontAwesome6 name="user-doctor" size={90} color="#053C5E" />
                        <Text style={styles.titulotexto}>Área do Médico</Text>
                        <TextInput
                            style={styles.input}
                            placeholder="Email"
                            onChangeText={newText => setNomeText(newText)}
                            defaultValue={nometext}
                        />
                        <TextInput
                            secureTextEntry={true}
                            style={styles.input}
                            placeholder="Senha"
                            onChangeText={newText => setSenhaText(newText)}
                            defaultValue={senhatext}
                        />
                        <Pressable
                            onPress={handleLogin}
                            style={({ pressed }) => [
                                { backgroundColor: pressed ? '#0F118C' : '#2A2CDF' },
                                styles.button
                            ]}>
                            <Text style={styles.buttontext}>Entrar</Text>
                        </Pressable>
                    </View>
            </ImageBackground>
        </View>
    );
}

export default Home;
