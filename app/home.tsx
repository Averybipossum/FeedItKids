import { Button, Pressable, StyleSheet,Text,View } from "react-native";
import React from "react";
import { router } from "expo-router";

const Home = () =>{
    return(
        <View>
            <Text>Home</Text>
            <Pressable onPress={()=>router.replace("/")}>
                <Text>Go to Main Page</Text>
            </Pressable>
        </View>
    )
}

export default Home

const styles = StyleSheet.create({})