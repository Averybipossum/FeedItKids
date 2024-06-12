import React, { useState } from "react";
import { View, Text, TextInput, Pressable, ImageBackground, Alert, Button } from "react-native";
import { WebView } from 'react-native-webview';
import * as FileSystem from 'expo-file-system';
import { Asset } from 'expo-asset';
import BGimage from "../../assets/BGmedico.png"; 
import { styles } from './styles';

import { FontAwesome6 } from '@expo/vector-icons';

const Home = () => {
    const [nometext, setNomeText] = useState('');
    const [senhatext, setSenhaText] = useState('');
    const [htmlContent, setHtmlContent] = useState<string | null>(null);
    const [showWebView, setShowWebView] = useState(false); // Estado para controlar a visibilidade do WebView

    const abrirPagina = async () => {
        try {
            const htmlFile = Asset.fromModule(require('../../assets/index.html')); //Função do Expo para carregar um arquivo local como um asset gerenciável.
            await htmlFile.downloadAsync(); // Método do objeto Asset que baixa o arquivo para o diretório local do dispositivo.
            const htmlString = await FileSystem.readAsStringAsync(htmlFile.localUri!);
            setHtmlContent(htmlString);
            setShowWebView(true); // Mostrar o WebView quando o conteúdo for carregado
        } catch (error) {
            console.error('Falhou ao carregar o arquivo HTML', error);
            Alert.alert('Error', 'Falhou ao carregar o arquivo HTML');
        }
    };

    return (
        <View style={styles.container}>
            <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
                {showWebView ? (
                    <View style={{ flex: 1, width: '100%', height: 'auto' }}>
                        {htmlContent && (
                            <WebView
                                originWhitelist={['*']}
                                source={{ html: htmlContent }}
                                style={{ flex: 1 }}
                            />
                        )}
                        <Pressable onPress={() => setShowWebView(false)} style={({ pressed }) => [
                                { backgroundColor: pressed ? '#0F118C' : '#2A2CDF' },
                                styles.buttonRelatorio
                            ]}>
                                <Text style={styles.buttontext}>Voltar</Text>
                        </Pressable>
                    </View>
                ):(
                    <View style={styles.containerconfig}>
                        <FontAwesome6 name="user-doctor" size={90} color="#053C5E" />
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
                            ]}>
                            <Text style={styles.buttontext}>Relatório</Text>
                        </Pressable>
                    </View>
                )}
            </ImageBackground>
        </View>
    );
}

export default Home;
