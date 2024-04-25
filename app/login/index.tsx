import * as React from 'react';
import { Button,StyleSheet, View, Text, Pressable } from 'react-native';
import { Link, router } from "expo-router";
import { Camera, CameraType } from 'expo-camera';

function LoginScreen() {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Login Screen</Text>
        <Button
                title="ir para Home"
                onPress={()=>router.replace("/home")}
                color="#841584"
        />
        <Pressable 
                onPress={()=>router.replace("/camera")}
                style={({pressed}) => [
                    pressed ? {backgroundColor:'#0F118C'}:{backgroundColor: '#2A2CDF',},
                    styles.button
                ]}
            >
                <Text style={styles.buttontext}>Câmera</Text>
            </Pressable>
      </View>
    );
  }

  export default LoginScreen;

  const styles = StyleSheet.create({
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