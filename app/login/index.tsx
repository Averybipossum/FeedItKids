import { ImageBackground, Pressable, StyleSheet,Text,View,TextInput, Alert} from "react-native";
import { styles } from './styles';
import React, { useState } from "react";
import {router } from "expo-router";
import { FontAwesome6 } from '@expo/vector-icons';
// import login from './request_login';
import axios from 'axios';

import BGimage from "../../assets/BGlogin.png"

const Home = () =>{
    //constantes
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');

    const handleLogin = async () => {
        try {
            const formData = new FormData();
            formData.append('username', nometext);
            formData.append('password', senhatext);

            const response = await axios.post('http://127.0.0.1:8000/auth/token', formData, {
                headers:{
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
            });

            // Se a chamada for bem-sucedida, você pode lidar com a resposta aqui
            console.log('Token de acesso:', response.data.acess_token);
            router.replace("/bichinho");

        } catch (error) {
            // Se houver um erro na chamada, exibir mensagem de erro
            console.error('Erro ao fazer login:', error);
            Alert.alert('Erro', 'Não foi possível fazer login. Verifique suas credenciais e tente novamente.');
        }
    };


    //página
    return(
        <View style={styles.container}>
            <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
                <View style={styles.wrapMedico}>
                    <View style={styles.iconMedico}>
                        <Pressable
                        onPress={()=>router.replace("/loginMedico")}
                        style={({pressed})=>[
                            pressed?{backgroundColor:'#053C5E'}:{backgroundColor:'#5AA9E6'},
                            {marginLeft:10,marginRight:0},styles.pressableIcon]}>
                            <FontAwesome6 name="user-doctor" size={24} color="#053C5E" />
                        </Pressable>
                    </View>
                </View>
                <View style={styles.containerconfig}>

                    <Text style={styles.titulotexto}>
                        Feed it!
                    </Text>

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
                        style={({pressed}) => [
                            pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                            styles.button]}>
                        <Text style={styles.buttontext}>Entrar</Text>
                    </Pressable>

                    <Text style={styles.texto} onPress={()=>router.replace("/cadastro")}>
                        Fazer Cadastro
                    </Text>
                    {/* Botão provisório para acessar o bichinho pelo celular*/}
                    <Text style={styles.texto} onPress={()=>router.replace("/bichinho")}>
                        Bichinho
                    </Text>
                
                </View>
            </ImageBackground>
        </View>
    )
}

export default Home