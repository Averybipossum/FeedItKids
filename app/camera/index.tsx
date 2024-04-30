import {Text, View, SafeAreaView, Button, Image, Platform, Dimensions, Pressable } from 'react-native';
import {styles} from './styles';
import { useEffect, useState } from 'react';
import { Camera } from 'expo-camera';
import { shareAsync } from 'expo-sharing';
import * as MediaLibrary from 'expo-media-library';
import React from 'react';
import { router } from 'expo-router';
import { AntDesign } from '@expo/vector-icons';
import { Entypo } from '@expo/vector-icons';

export default function App() {
  //permissões da camera
  const [hasCameraPermission, setHasCameraPermission] = useState(false);
  const [hasMediaLibraryPermission, setHasMediaLibraryPermission] = useState(false);
  const [camera, setCamera] = useState();
  const [photo, setPhoto] = useState();

  // Escala da tela e imagem padding
  const [imagePadding, setImagePadding] = useState(0);
  const [ratio, setRatio] = useState('4:3');  // default is 4:3
  const { height, width } = Dimensions.get('window');
  const screenRatio = height / width;
  const [isRatioSet, setIsRatioSet] =  useState(false);


  useEffect(() => {
    (async () => {
      const cameraPermission = await Camera.requestCameraPermissionsAsync();
      const mediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();
      setHasCameraPermission(cameraPermission.status === "granted");
      setHasMediaLibraryPermission(mediaLibraryPermission.status === "granted");
    })();
  }, []);

  const prepareRatio = async() =>{
    let desiredRatio = '4:3';
    if (Platform.OS === 'android') {
      const ratios = await camera.getSupportedRatiosAsync();

      let distances = [];
      let realRatios = [];
      let minDistance = null;
      for (const ratio of ratios) {
        const parts = ratio.split(':');
        const realRatio = parseInt(parts[0]) / parseInt(parts[1]);
        realRatios[ratio] = realRatio;
        // ratio can't be taller than screen, so we don't want an abs()
        const distance = screenRatio - realRatio; 
        distances[ratio] = realRatio;
        if (minDistance == null) {
          minDistance = ratio;
        } else {
          if (distance >= 0 && distance < distances[minDistance]) {
            minDistance = ratio;
          }
        }
    }

    desiredRatio = minDistance;
    const remainder = Math.floor(
      (height - realRatios[desiredRatio] * width) / 2
    );
    // set the preview padding and preview ratio
    setImagePadding(remainder);
    setRatio(desiredRatio);
    // Set a flag so we don't do this 
    // calculation each time the screen refreshes
    setIsRatioSet(true);

  }
};

const setCameraReady = async() => {
  if (!isRatioSet) {
    await prepareRatio();
  }
};

  if (hasCameraPermission === undefined) {
    return <Text>Requesting permissions...</Text>
  } else if (!hasCameraPermission) {
    return <Text style={[{}]}>Permission for camera not granted. Please change this in settings.</Text>
  }

  let takePic = async () => {
    let options = {
      quality: 1,
      base64: true,
      exif: false
    };

    let newPhoto = await camera.takePictureAsync(options);
    setPhoto(newPhoto);
  };

  if (photo) {
    let sharePic = () => {
      shareAsync(photo.uri).then(() => {
        setPhoto(undefined);
      });
    };

    let savePhoto = () => {
      MediaLibrary.saveToLibraryAsync(photo.uri).then(() => {
        setPhoto(undefined);
      });
    };

    return (
      <SafeAreaView style={styles.container}>
        <Image style={styles.preview} source={{ uri: "data:image/jpg;base64," + photo.base64 }} />
        <Button title="Share" onPress={sharePic} />
        {hasMediaLibraryPermission ? <Button title="Save" onPress={savePhoto} /> : undefined}
        <Button title="Discard" onPress={() => setPhoto(undefined)} />
      </SafeAreaView>
    );
  }

  return (
    <Camera style={[styles.container, {marginTop: imagePadding, marginBottom: imagePadding}]} onCameraReady={setCameraReady} ratio={ratio}
    ref={(ref) => {setCamera(ref);}} >
      <View>
        <Pressable 
            onPress={()=>router.replace("/bichinho")}
            style={({pressed})=>[
              pressed?{backgroundColor:'rgba(0,0,0,0.5)'}:{backgroundColor:'rgba(128,128,128,0.5)'},
              styles.buttonX]}
            >
            <AntDesign name="closecircleo" size={30} color={'white'}/>
        </Pressable>
      </View>
      <View style={styles.buttonCamera}>
        <Pressable
         onPress={takePic}
        style={({pressed})=>[
          pressed?{backgroundColor:'rgba(0,0,0,0.5)'}:{backgroundColor:'rgba(128,128,128,0.5)'},
          styles.pressableCamera
        ]}
        >
          <Entypo name="circle" size={80} color="white"/>
        </Pressable>
      </View>
    </Camera>
  );
}

