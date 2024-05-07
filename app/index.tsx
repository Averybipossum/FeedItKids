
import React from "react";
import {Redirect } from "expo-router";
import { useFonts, Pacifico_400Regular } from '@expo-google-fonts/pacifico';

const Index = () =>{

    let [fontsLoaded] = useFonts({
        Pacifico_400Regular,
      });
      
    if (!fontsLoaded) {
    return null;
    }
    

    return(
        <Redirect href="/login"/>
    )
}

export default Index
