
import * as React from 'react';
import { StyleSheet,Button, View, Text,Image} from 'react-native';
import {router} from "expo-router";
import MagmaSlime from "../../assets/MagmaSlime.jpg";
function Teste() {
    return (
      <View style={styles.container}>
        <Text>Bichinho</Text>
        <Image style={styles.image} source={MagmaSlime}/>
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
      width: '75%',
      objectFit: 'contain',
    },
  });

  export default Teste;