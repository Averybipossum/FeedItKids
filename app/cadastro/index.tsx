import { ImageBackground, Pressable,Text,View,TextInput, Alert} from "react-native";
import { styles } from './styles';
import React, { useState } from "react";
import {router } from "expo-router";

import BGimage from "../../assets/BGlogin.png"
import axios from "axios";

const Home = () =>{
    //constantes
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');
    const [confirmSenhaText, setConfirmSenhaText] = useState('');

    // Verificação se as senhas correspondem
    const isButtonDisabled = !nometext || !senhatext || senhatext !== confirmSenhaText;

    const handleCadastro = async () => {
        if (senhatext !== confirmSenhaText) {
            Alert.alert('Erro', 'As senhas não correspondem.');
            return;
        }
        try {
            const response = await axios.post('http://127.0.0.1:8000/usuarios/usuarios/',{
                email: nometext,
                senha: senhatext,
                pontuacao_total: 0
            });

            // Se a chamada for bem-sucedida, você pode lidar com a resposta aqui
            console.log('Usuário criado', response.data);
            router.replace("/bichinho");

        } catch (error) {
            // Se houver um erro na chamada, exibir mensagem de erro
            console.error('Erro ao fazer cadastro:', error);
            Alert.alert('Erro', 'Não foi possível fazer cadastro. Verifique se já não possui uma conta registrada.');
        }
    };

    //página
    return(
        <View style={styles.container}>
            <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
                <View style={styles.containerconfig}>

                <Text style={styles.titulotexto}>
                    Cadastro
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
                
                <TextInput
                    secureTextEntry={true}
                    style={styles.input}
                    placeholder="Confirme a senha"
                    onChangeText={newText => setConfirmSenhaText(newText)}
                    defaultValue={confirmSenhaText}
                />

                    {isButtonDisabled && senhatext !== '' && confirmSenhaText !== '' && (
                        <Text style={styles.errorText}>As senhas não correspondem</Text>
                    )}

                <Pressable 
                    onPress={handleCadastro}
                    disabled={isButtonDisabled}
                    style={({pressed}) => [
                        {
                            backgroundColor: isButtonDisabled ? '#cccccc' : pressed ? '#0F118C' : '#2A2CDF',
                        },
                        styles.button]}>
                    <Text style={styles.buttontext}>Entrar</Text>
                </Pressable>

                </View>
            </ImageBackground>
        </View>
    )
}

export default Home