import { ImageBackground, Pressable, StyleSheet,Text,View,TextInput, Alert} from "react-native";
import { styles } from './styles';
import React, { useState } from "react";
import {router } from "expo-router";
import { FontAwesome6 } from '@expo/vector-icons';
import login from './request_login';
import axios from 'axios';


import BGimage from "../../assets/BGlogin.png"

const Home = () =>{
    //constantes
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');


    async function login(username: string, password: string) {
        try {
            const response = await axios.post('/token', {
                username: username,
                password: password
            });
            
            // Se a chamada for bem-sucedida, retorna o token de acesso
            return response.data.access_token;
        } catch (error) {
            // Se houver um erro na chamada, lança uma exceção ou trata de outra forma
            console.error('Erro ao fazer login:', error);
            throw error;
        }
    }

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
                        onPress={login}
                        style={({pressed}) => [
                            pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                            styles.button]}>
                        <Text style={styles.buttontext}>Entrar</Text>
                    </Pressable>

                    <Text style={styles.texto} onPress={()=>router.replace("/cadastro")}>
                        Fazer Cadastro
                    </Text>
                
                </View>
            </ImageBackground>
        </View>
    )
}

export default Home