
import * as React from 'react';
import { StyleSheet,Button, View, Text,Image} from 'react-native';
import {router } from "expo-router";

function Teste() {
    return (
      <View style={styles.container}>
        <Text>Bichinho</Text>
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