import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent:'flex-end',
    },
    containerTop: {
      flex: 1,
      alignItems: 'flex-start',
      justifyContent:'center',
      maxWidth:'auto',
      maxHeight:100,
    },
    containerIcon: {
      marginTop:5,
    },
    wrapTop:{
      flex:1,
      justifyContent:'flex-start',
    },
    wrapBottom:{
      flex:1,
      justifyContent:'flex-end',
    },
    containerBixo: {
      height:350,
      width:350,
      alignItems: 'center',
      justifyContent:'center',
    },
    containerBottom: {
      flex: 1,
      alignItems:'center',
      justifyContent:'center',
      backgroundColor:'#053C5E',
      maxWidth:'auto',
      maxHeight:270,
      borderColor:'#053C5E',
      borderWidth:3,
    },
    conteudoBottomStatus: {
      flex: 4,
      margin:5,
      alignItems:'center',
      justifyContent:'center',
      height:250,
    },
    conteudoBottomCamera: {
      flex:2,
      margin:5,
      alignItems:'center',
      justifyContent:'center',
      height:250,
    },
    pressableCamera:{
      width:120,
      height:120,
      borderRadius:90,
      alignItems:'center',
      justifyContent:'center',
      borderColor:'#053C5E',
      borderWidth:3,
    },
    containerSeletor:{
      flex:1,
      justifyContent:'center',
      alignItems:'center',
      maxWidth:'auto',
      maxHeight:'auto',
    },
    conteudoSeletor:{
      padding:20,
      backgroundColor:'rgba(255,255,255,0.8)',
      borderRadius:25,
    },
    pressableSeletor:{
      width:150,
      height:150,
      margin:5,
      alignItems:'center',
      borderWidth:5,
      borderRadius:25,
    },
    imagemSeletor:{
      flex:1,
      objectFit: 'contain',
      width: '95%',
    },
    containerTituloSeletor: {
      alignItems:'center',
      justifyContent:'flex-start',
    },
    tituloSeletor:{
      fontSize: 50,
      color: 'green',
      marginBottom: 40,
      textAlign:'center',
  },
    row: {
      flexDirection: 'row',
      justifyContent: 'space-between',
    },
    imagemBichinho: {
      flex: 1,
      width: '90%',
      objectFit: 'contain',
    },
    imagem: {
      flex: 1,
      width: '100%',
      height: '100%',
      justifyContent: 'center',
    },
    pressableIcon:{
      marginTop:20,
      marginRight:10,
      width:60,
      height:60,
      borderRadius:90,
      alignItems:'center',
      justifyContent:'center',
    },

    iconImage:{
      flex: 1,
      width:'100%',
      objectFit: 'contain',
    },
  });