import React, { useState } from "react";
import { View, Text, TextInput, Pressable, ImageBackground, Alert } from "react-native";
import { WebView } from 'react-native-webview';
import * as FileSystem from 'expo-file-system';
import { Asset } from 'expo-asset';
import BGimage from "../../assets/BGmedico.png"; // Atualize o caminho conforme necessário
import { styles } from './styles'; // Atualize o caminho conforme necessário

const Home = () => {
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');
    const [htmlContent, setHtmlContent] = useState<string | null>(null);

    const abrirPagina = async () => {
        try {
            const htmlFile = Asset.fromModule(require('../../assets/index.html')); // Certifique-se de que o caminho está correto
            await htmlFile.downloadAsync();
            const htmlString = await FileSystem.readAsStringAsync(htmlFile.localUri!);
            setHtmlContent(htmlString);
        } catch (error) {
            console.error('Failed to load HTML file', error);
            Alert.alert('Error', 'Failed to load HTML file');
        }
    };

    return (
        <View style={styles.container}>
            <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
                <View style={styles.containerconfig}>
                    <Text style={styles.titulotexto}>Área do Médico</Text>
                    <TextInput
                        style={styles.input}
                        placeholder="Email"
                        onChangeText={newText => setNomeText(newText)}
                        defaultValue={nometext}
                    />
                    <TextInput
                        secureTextEntry={true}
                        style={styles.input}
                        placeholder="Senha"
                        onChangeText={newText => setSenhaText(newText)}
                        defaultValue={senhatext}
                    />
                    <Pressable
                        onPress={abrirPagina}
                        style={({ pressed }) => [
                            { backgroundColor: pressed ? '#0F118C' : '#2A2CDF' },
                            styles.button
                        ]}
                    >
                        <Text style={styles.buttontext}>Relatório</Text>
                    </Pressable>
                    {/* ta dando erro exatamente nesta posição
                    talvez eu faça um redirecionamento onde o webview possa abrir sozinho :"D " */}
                    {htmlContent && (
                        <WebView
                            originWhitelist={['*']}
                            source={{ html: htmlContent }}
                            style={{ flex: 1, width: 100, height: 100 }}
                        />
                    )}
                </View>
            </ImageBackground>
        </View>
    );
}

export default Home;


    // const [resultado, setResultado] = useState(null);
    // const abrirPagina = async() =>{
    //     let resultado = await WebBrowser.openBrowserAsync(HTML);
    //     setResultado(resultado);
    // };