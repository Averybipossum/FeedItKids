import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({

    titulotexto:{
        fontFamily: "Pacifico_400Regular",
        fontSize: 35,
        color: '#053C5E',
        marginHorizontal:20,
        marginVertical:20
    },
    texto:{
        marginTop:10,
        fontSize:13,
        color: 'black',
        textAlign: 'center',
        marginBottom:10,
        paddingLeft:50,
        paddingRight:50,
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
    reportTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        color: '#053C5E',
        marginTop: 20,
        marginBottom: 10,
    },
    containerRelatorio:{
        backgroundColor:"aliceblue",
        alignSelf: 'center',
        height: '90%',
        width: '90%',
        borderRadius:20,
        alignItems: 'center',
    },
    chartImage: {
        width: 300,
        height: 300,
        resizeMode: 'contain',
    },
  });