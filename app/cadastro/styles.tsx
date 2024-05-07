import { StyleSheet } from 'react-native';


export const styles = StyleSheet.create({

    titulotexto:{
        fontFamily:'Pacifico_400Regular',
        fontSize: 41,
        color: 'green',
        marginBottom: 30
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
        marginTop:40,
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
})