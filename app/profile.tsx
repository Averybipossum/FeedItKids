import { StyleSheet,Text,View,Pressable,TextInput } from "react-native";
import React from "react";
import { router } from "expo-router";

const Profile = () =>{
    return(    
        <Pressable
            onPress={()=>router.replace("/home")}
            style={({ pressed }) => [
            pressed ? {backgroundColor:'black'} : {},
            styles.button
        ]}
        >
            <View>
                <Text>
                Pressable a simple opacity
                </Text>
            </View>
        </Pressable>
    )
}

export default Profile

const styles = StyleSheet.create({
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