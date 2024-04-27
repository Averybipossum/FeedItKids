
import * as React from 'react';
import { StyleSheet,Button, View, Text,Image, ImageBackground} from 'react-native';
import {router} from "expo-router";
import MagmaSlime from "../../assets/MagmaSlime.png";
import IceSlime from "../../assets/IceSlime.png"
import BGimage from "../../assets/BGimage.png"
import { useState } from 'react';


function Bichinho() {
  const [showFirstImage, setShowFirstImage] = useState(true);
  const firstImage = MagmaSlime;
  const secondImage = IceSlime;
  const changeImageSource = () => {
    setShowFirstImage(!showFirstImage)
  }
  return (
    <View style={styles.container}>
      <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
        <View style={styles.container}>
          <Text>Bichinho</Text>
          <Image style={styles.image} source={showFirstImage?firstImage:secondImage}/>
        </View>
        <View>
        <Button
            title="ir para Home"
            onPress={()=>router.replace("/home")}
            color="#841584"
          />
        <Button
            title="Mudar Imagem"
            onPress={changeImageSource}
            color="#841584"
          />
        </View>
      </ImageBackground>
    </View>
  );
}
const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    },
    image: {
      flex: 1,
      width: '75%',
      objectFit: 'contain',
    },
    imagem: {
      flex: 1,
      width: '100%',
      height: '100%',
      resizeMode: "cover",
      justifyContent: 'center',
    },
  });

  export default Bichinho;