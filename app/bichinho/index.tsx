import * as React from 'react';
import { styles } from './styles';
import { StyleSheet,Button, View, Text,Image, ImageBackground, Modal, Pressable,} from 'react-native';
import {router} from "expo-router";
import { useState,useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import Empty from "../../assets/Empty.png"
import MagmaSlime from "../../assets/MagmaSlime.png";
import IceSlime from "../../assets/IceSlime.png"
import BGimage from "../../assets/BGimage.png"
import BGSeletor from "../../assets/BGSeletor.jpg"
import slimeIcon from "../../assets/SlimeLogo.png"
import { Entypo } from '@expo/vector-icons';

function Bichinho() {
  const [seletorVisivel,setSeletorVisivel] = useState(false);
  const [baseImageIndex, setBaseImageIndex] = useState(Empty);

  const abrirSeletor = ()=>{
    setSeletorVisivel(true);
  }
  const fecharSeletor = ()=>{
    setSeletorVisivel(false);
  }

  const escolherBichinho = (index: any)=>{
    setBaseImageIndex(index);
    saveBaseImageIndex(index)
    fecharSeletor()
  }

  const saveBaseImageIndex = async (index:any) => {
    try {
      await AsyncStorage.setItem('baseImageIndex', index.toString());
    } catch (error) {
      console.error('Erro ao salvar imagem base:', error);
    }
  };

  useEffect(() => {
    const loadBaseImage = async () => {
      try {
        const savedIndex = await AsyncStorage.getItem('baseImageIndex');
        if (savedIndex !== null) {
          setBaseImageIndex(parseInt(savedIndex));
        }
      } catch (error) {
        console.error('Erro ao carregar imagem base:', error);
      }
    };
    loadBaseImage();
  }, []);

  return (
    <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
      <View style={styles.wrapTop}>
        <View style={styles.containerTop}>
            
        </View>
        <View style={styles.containerIcon}>
          <View style={styles.row}>
            <Pressable
              onPress={abrirSeletor}
              style={({pressed})=>[
                pressed?{backgroundColor:'#053C5E'}:{backgroundColor:'#5AA9E6'},
                styles.pressableIcon]}
            >
              <Image style={styles.iconImage} source={slimeIcon}/>
            </Pressable>
          </View>
      </View>
      </View>

      <View style={styles.container}>
        <View style={styles.containerBixo}>
          <Image style={styles.imagemBichinho} source={baseImageIndex}/>
        </View>
      </View>
      <View style={styles.wrapBottom}>
        <View style={styles.containerBottom}>
          <View style={styles.row}>
              <View style={styles.conteudoBottomStatus}>

              </View>
              <View style={styles.conteudoBottomCamera}>
                  <Pressable
                    onPress={()=>router.replace("/camera")}
                    style={({pressed})=>[
                      pressed?{}:{},
                      styles.pressableCamera
                    ]}
                  >
                    <Entypo name="camera" size={72} color="white" />
                  </Pressable>
              </View>
          </View>
        </View>
      </View>
      <View>
        <Modal
            animationType='slide'
            transparent={true}
            visible={seletorVisivel || baseImageIndex === Empty}
            onRequestClose={fecharSeletor}>
              <ImageBackground source={BGSeletor} resizeMode="cover" style={styles.imagem}>
                <View style={styles.containerSeletor}>
                  <View style={styles.conteudoSeletor}>
                    <View style={styles.containerTituloSeletor}>
                      <Text style={styles.tituloSeletor}>
                        Escolha seu Bichinho!
                      </Text>
                    </View>
                    <View style={styles.row}>
                      <Pressable
                        onPress={()=>escolherBichinho(MagmaSlime)}
                        style={({pressed})=>[
                          pressed?{backgroundColor:'green',borderColor:'lightgreen'}:{backgroundColor:'white',borderColor:'lightgreen'},
                          styles.pressableSeletor
                        ]}
                      >
                        <Image style={styles.imagemSeletor} source={MagmaSlime}></Image>
                      </Pressable>
                      <Pressable
                        onPress={()=>escolherBichinho(IceSlime)}
                        style={({pressed})=>[
                          pressed?{backgroundColor:'green',borderColor:'lightgreen'}:{backgroundColor:'white',borderColor:'lightgreen'},
                          styles.pressableSeletor
                        ]}
                      >
                      
                        <Image style={styles.imagemSeletor} source={IceSlime}></Image>
                      </Pressable>
                    </View>
                  </View>
                </View>
              </ImageBackground>
        </Modal>
      </View>
    </ImageBackground>
  );
}


  export default Bichinho;