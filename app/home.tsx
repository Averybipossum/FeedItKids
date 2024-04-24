import {Pressable, StyleSheet,Text,View,TextInput} from "react-native";
import React, { useState } from "react";
import {router } from "expo-router";

const Home = () =>{
    const [text, setText] = useState('');
    return(
        <View style={styles.container}>
            <TextInput
                style={styles.input}
                placeholder="Type here to translate!"
                onChangeText={newText => setText(newText)}
                defaultValue={text}
            />
            <Pressable 
                onPress={()=>router.replace("/login")}
                style={styles.button} 
            >
                <Text style={styles.buttontext}>Ir para Login</Text>
            </Pressable>
            <Pressable 
                onPress={()=>router.replace("/profile")}
                style={styles.button} 
            >
                <Text style={styles.buttontext}>Ir para Profile</Text>
            </Pressable>
        </View>
    )
}

export default Home

const styles = StyleSheet.create({
    input: {
        height: 40,
        margin: 12,
        borderWidth: 1,
        padding: 10,
        color:'black',
      },
    container: {
        alignItems: 'center',
    },
    button:{
        alignItems: 'center',
        justifyContent: 'center',
        marginTop:10,
        paddingVertical: 12,
        paddingHorizontal: 32,
        borderRadius: 4,
        elevation: 3,
        backgroundColor: 'turquoise',
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