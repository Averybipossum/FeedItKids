import { ImageBackground, Pressable, StyleSheet,Text,View,TextInput} from "react-native";
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
                Login
            </Text>
            <TextInput
                style={styles.input}
                placeholder="Email"
                onChangeText={newText => setNomeText(newText)}
                defaultValue={nometext}
            />
            <View>
            <TextInput
                secureTextEntry={true}
                style={styles.input}
                placeholder="Senha"
                onChangeText={newText => setSenhaText(newText)}
                defaultValue={senhatext}
            />
            </View>
            <Pressable 
                onPress={()=>router.replace("/bichinho")}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]}
            >
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

const styles = StyleSheet.create({

    titulotexto:{
        fontFamily: "monospace",
        //depois tentar fazer a fonte
        fontSize: 50,
        color: 'green',
        marginBottom: 40
    },

    texto:{
        marginTop:50,
        color: 'blue'
    },
    containerconfig:{
        backgroundColor:"aliceblue",
        alignSelf: 'center',
        height: 500,
        width: 370,
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius:20,
        
    },
    input: {
        height: 50,
        margin: 12,
        borderWidth: 1,
        padding: 10,
        minWidth:300,
    },
    container: {
        alignItems: 'center',
        justifyContent: 'center',
        flex:1,
    },
    button:{
        alignItems: 'center',
        justifyContent: 'center',
        marginTop:20,
        paddingVertical: 8,
        paddingHorizontal: 32,
        borderRadius: 4,
        elevation: 3,
        minWidth:300,
    },
    buttontext: {
        fontSize: 16,
        lineHeight: 21,
        fontWeight: 'bold',
        letterSpacing: 0.25,
        color: 'white',
    },
    imagem: {
        flex: 1,
        width: '100%',
        height: '100%',
        resizeMode: "cover",
        justifyContent: 'center',
    },
})