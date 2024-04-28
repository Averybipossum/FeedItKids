
import * as React from 'react';
import { StyleSheet,Button, View, Text,Image, ImageBackground, Modal, Pressable,} from 'react-native';
import {router} from "expo-router";
import MagmaSlime from "../../assets/MagmaSlime.png";
import IceSlime from "../../assets/IceSlime.png"
import BGimage from "../../assets/BGimage.png"
import { useState } from 'react';


function Bichinho() {
  const [seletorVisivel,setSeletorVisivel] = useState(false);
  const [showFirstImage, setShowFirstImage] = useState(true);
  const firstImage = MagmaSlime;
  const secondImage = IceSlime;
  let escolhaBichinho = false;
  const changeImageSource = () => {
    setShowFirstImage(!showFirstImage)
  }
  const abrirSeletor = ()=>{
    setSeletorVisivel(true);
  }
  const fecharSeletor = ()=>{
    setSeletorVisivel(false);
  }
  return (
    <View style={styles.container}>
      <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
        <View style={styles.container}>
          <Image style={styles.imagemBichinho} source={showFirstImage?firstImage:secondImage}/>
        </View>
        <View>
          <Modal
              animationType='slide'
              transparent={true}
              visible={seletorVisivel}
              onRequestClose={fecharSeletor}>
                <View style={styles.containerSeletor}>
                  <View style={styles.conteudoSeletor}>
                  </View>
                </View>
          </Modal>
        </View>
        <View>
        <Button
            title="ir para Home"
            onPress={()=>router.replace("/home")}
            color="#841584"
          />
        <Button
            title="Mudar Imagem"
            onPress={abrirSeletor}
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
    containerSeletor:{
      flex:1,
      justifyContent:'center',
      alignItems:'center',
      backgroundColor:'rgba(0,0,0,0.5)',
    },
    conteudoSeletor:{
      padding:20,
    },
    imagemSeletor:{
      flex: 1,
      objectFit:'contain',
      width:200,
    },
    imagemBichinho: {
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