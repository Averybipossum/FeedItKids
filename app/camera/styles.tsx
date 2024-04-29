import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
    container: {
      backgroundColor: 'black',
      flex: 1,
    },
    buttonContainer: {
      backgroundColor: '#000',
      bottom: "-99%",
      right: 0
    },
    preview: {
      alignSelf: 'stretch',
      flex: 1
    },
    buttonX:{
        alignItems:'center',
      margin:10,
      top:10,
      right:0,
      width:30,
      height:30,
      borderRadius:90,
      position: 'absolute',
      
    },
    buttontext: {
      fontSize: 16,
      lineHeight: 21,
      fontWeight: 'bold',
      letterSpacing: 0.25,
      color: 'white',
    },
    buttonCamera:{
      flex: 1,
      justifyContent: 'flex-end',
    }
  });