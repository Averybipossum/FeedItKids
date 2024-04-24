import { Image } from 'expo-image';
import * as React from 'react';
import { StyleSheet,Button, View, Text } from 'react-native';
import {router } from "expo-router";

function Teste() {
    return (
      <View style={styles.container}>
        <Text>Bichinho</Text>
        <Image
        style={styles.image}
        source="https://picsum.photos/seed/696/3000/2000"
        contentFit="cover"
        transition={1000}
        />
        <Button
                title="ir para Home"
                onPress={()=>router.replace("/home")}
                color="#841584"
            />
      </View>
    );
  }
const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
    image: {
      flex: 1,
      width: '100%',
      backgroundColor: '#0553',
    },
  });

  export default Teste;