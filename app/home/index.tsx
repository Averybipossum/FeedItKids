import {Pressable, StyleSheet,Text,View,TextInput} from "react-native";
import React, { useState } from "react";
import {router } from "expo-router";

const Home = () =>{
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');
    return(
        <View style={styles.container}>
            <TextInput
                style={styles.input}
                placeholder="Nome de Usuário"
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
                onPress={()=>router.replace("/login")}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]}
            >
                <Text style={styles.buttontext}>Fazer Login</Text>
            </Pressable>
            <Pressable 
                onPress={()=>router.replace("/cadastro")}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]} 
            >
                <Text style={styles.buttontext}>Fazer Cadastro</Text>
            </Pressable>
            <Pressable 
                onPress={()=>router.replace("/bichinho")}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]} 
            >
                <Text style={styles.buttontext}>Teste</Text>
            </Pressable>
        </View>
    )
}

export default Home

const styles = StyleSheet.create({
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
        marginTop:10,
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
})