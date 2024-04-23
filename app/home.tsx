import { Button, Pressable, StyleSheet,Text,View } from "react-native";
import React from "react";
import { Link, router } from "expo-router";

const Home = () =>{
    return(
        <View>
            <Text>Home</Text>
            <Button
                title="Ir para Profile"
                onPress={()=>router.replace("/profile")}
                color="#841584"
            />
        </View>
    )
}

export default Home

const styles = StyleSheet.create({})