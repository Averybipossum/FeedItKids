import { StyleSheet,Text,View,Button } from "react-native";
import React from "react";
import { router } from "expo-router";

const Profile = () =>{
    return(
        <View>
            <Text>Profile</Text>
            <Button
                title="Voltar para Main"
                onPress={()=>router.replace("/")}
                color="#841584"
            />
        </View>
    )
}

export default Profile

const styles = StyleSheet.create({})