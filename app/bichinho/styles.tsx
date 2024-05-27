import { StyleSheet } from 'react-native';
import { objectives } from './objectives';

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
      marginTop:3,
    },
    containerInfo:{
      flex:1, 
      backgroundColor:'rgba(5, 60, 94, .7)',
      marginTop:160, 
      marginHorizontal:30, 
      marginBottom:200, 
      alignItems: 'center', 
      borderRadius: 20,
      justifyContent:'center',
      alignContent:'center'
    },
    wrapTop:{
      marginTop:10,
      flex:1,
      justifyContent:'flex-start',
    },
    wrapBottom:{
      flex:1,
      justifyContent:'flex-end',
    },
    containerBixo: {
      height:300,
      width:300,
      alignItems: 'center',
      justifyContent:'center',
    },
    objectiveContainer: {
      flexDirection: 'row',
      alignItems: 'center',
      marginBottom: 10,
    },
    objectiveText: {
      marginLeft: 10,
      fontSize:25,
    },
    objectivesContainer: {
      marginTop: 2,
      flex:5,
      justifyContent:'center',
      alignItems:'center',
    },
    objectivesHeader:{
      fontSize:30,
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
    sidebar: {
      position: 'absolute',
      zIndex: 1,
      top: 0,
      bottom: 0,
      left: 0,
      right:0,
      backgroundColor: 'white',
      width: 300, // Largura da barra lateral
      height: '100%', // Altura igual à altura da tela
      paddingTop: 50, // Espaçamento para acomodar a barra de status
      paddingHorizontal: 20,
      
    },
    sidebarTop:{
      flex:1,
      justifyContent:'flex-start',
      alignItems:'flex-end',
    },
    textBarra:{
      alignSelf: "flex-start",
      color: "white",
      fontSize: 15,
      paddingBottom: 4,
      paddingTop: 10,
    },
  }
);