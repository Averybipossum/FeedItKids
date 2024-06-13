import { StyleSheet } from 'react-native';


export const styles = StyleSheet.create({
    
    titulotexto:{
        fontFamily: "Pacifico_400Regular",
        fontSize: 35,
        color: '#053C5E',
        marginBottom: 20
    },

    texto:{
        marginTop:50,
        color: 'blue'
    },
    containerconfig:{
        backgroundColor:"aliceblue",
        alignSelf: 'center',
        height: 500,
        width: 370,
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius:20,
        position:'absolute'
        
    },
    input: {
        height: 50,
        margin: 12,
        borderWidth: 1,
        padding: 10,
        minWidth:300,
    },
    container: {
        alignItems: 'center',
        justifyContent: 'center',
        flex:1,
    },
    button:{
        alignItems: 'center',
        justifyContent: 'center',
        marginTop:20,
        paddingVertical: 8,
        paddingHorizontal: 32,
        borderRadius: 4,
        elevation: 3,
        minWidth:300,
    },
    buttontext: {
        fontSize: 16,
        lineHeight: 21,
        fontWeight: 'bold',
        letterSpacing: 0.25,
        color: 'white',
    },
    imagem: {
        flex: 1,
        width: '100%',
        height: '100%',
        resizeMode: "cover",
        justifyContent: 'center',

    },
    wrapMedico:{
        flex:1,
        alignContent:'flex-start',
        justifyContent:'flex-start',
        
    },
    iconMedico:{
        marginTop:10,
        minHeight:100,
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
  });