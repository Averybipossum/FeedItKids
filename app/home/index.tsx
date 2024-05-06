import { ImageBackground, Pressable, StyleSheet,Text,View,TextInput, Modal} from "react-native";
import React, { useState } from "react";
import {router } from "expo-router";

import BGimage from "../../assets/FundoHome.png"
// Rest of the import statements


const Home = () =>{

    const [seletorVisivel,setSeletorVisivel] = useState(false);

    const abrirSeletor = ()=>{
        setSeletorVisivel(true);
    }
    const fecharSeletor = ()=>{
        setSeletorVisivel(false);
    }

    return(
        <View style={styles.container}>
            <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
            <View style={styles.containerconfig}>
            <Text style={styles.titulotexto}>
                Feed It!
            </Text>
            <Pressable 
                onPress={()=>router.replace("/bichinho")}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]}
            >
                <Text style={styles.buttontext}>Jogar!</Text>
            </Pressable>
            <Pressable 
                onPress={abrirSeletor}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]} 
            >
                <Text style={styles.buttontext}>Instruções</Text>
            </Pressable>
            </View>
            <View>
                <Modal animationType='fade'
                visible={seletorVisivel}
                transparent={true}>
                    <View style={({flex:1, backgroundColor:'rgba(5, 60, 94, .8)',marginVertical:200, marginHorizontal:30, alignItems: 'center', borderRadius: 20})}>
                        <Text style={({color: 'white', textAlign: 'center', padding: 20})}>Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
                        laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
                        eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est
                        laborum. At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti
                        quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt
                        mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore,
                        cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda
                        est, omnis dolor repellendus. Temporibus autem.</Text>
                        <Text style={({color: 'white',})} onPress={fecharSeletor}>
                        Fechar
                        </Text>
                    </View>
                </Modal>
            </View>
            </ImageBackground>
        </View>
    )
}
// 053C5E

export default Home

const styles = StyleSheet.create({

    titulotexto:{
        // fontFamily: "Pulang",
        //ele nao reconhece essa fonte
        fontSize: 50,
        color: 'green',
        marginBottom: 30
    },
    containerconfig:{
        backgroundColor:"aliceblue",
        alignSelf: 'center',
        height: 400,
        width: 370,
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius:20,
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