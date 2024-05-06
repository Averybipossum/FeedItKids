import { ImageBackground, Pressable,Text,View,TextInput} from "react-native";
import { styles } from './styles';
import React, { useState } from "react";
import {router } from "expo-router";

import BGimage from "../../assets/FundoHome.png"

const Home = () =>{
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');
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
                onChangeText={newText => setSenhaText(newText)}
                defaultValue={senhatext}
            />

            <Pressable 
                onPress={()=>router.replace("/login")}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]}
            >
                <Text style={styles.buttontext}>Entrar</Text>
            </Pressable>
            </View>
            </ImageBackground>
        </View>
    )
}

export default Home