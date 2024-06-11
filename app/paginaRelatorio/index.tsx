import React, { useState } from "react";
import { View, Text, TextInput, Pressable, ImageBackground, Alert, Image, StyleSheet } from "react-native";
import axios from "axios";
import BGimage from "../../assets/BGmedico.png";
import { FontAwesome6 } from '@expo/vector-icons';
import { styles } from "./styles";

const Home = () => {
    const [anoSelect, setAnoSelect] = useState('');
    const [chartUri, setChartUri] = useState<string | null>(null);

    const gerarRelatorio = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/generate_chart?ano=${anoSelect}`, { responseType: 'blob' });
            const reader = new FileReader();
            reader.onload = () => {
                setChartUri(reader.result as string);
            };
            reader.readAsDataURL(response.data);
        } catch (error) {
            console.error('Erro ao gerar relatório:', error);
            Alert.alert('Erro', 'Não foi possível gerar o relatório. Verifique o ano e tente novamente.');
        }
    };

    return (
        <View style={styles.container}>
            <ImageBackground source={BGimage} resizeMode="cover" style={styles.imagem}>
                {chartUri ? (
                    <View style={styles.containerRelatorio}>
                        <Text style={styles.titulotexto}>
                            Relatório {anoSelect}
                        </Text>
                        <Image source={{ uri: chartUri }} style={styles.chartImage} />
                    </View>
                ) : (
                    <View style={styles.containerconfig}>
                        <FontAwesome6 name="user-doctor" size={90} color="#053C5E" />
                        <Text style={styles.titulotexto}>Área do Médico</Text>
                        <Text style={styles.texto}>
                            Insira o ano (XXXX) no qual deseja acessar o relatório obtido.
                        </Text>
                        <TextInput
                            style={styles.input}
                            placeholder="Ano"
                            onChangeText={newText => setAnoSelect(newText)}
                            defaultValue={anoSelect}
                            maxLength={4}
                            keyboardType="numeric"
                        />
                        <Pressable
                            onPress={gerarRelatorio}
                            style={({ pressed }) => [
                                { backgroundColor: pressed ? '#0F118C' : '#2A2CDF' },
                                styles.button
                            ]}
                        >
                            <Text style={styles.buttontext}>Gerar Relatório</Text>
                        </Pressable>
                    </View>
                )}
            </ImageBackground>
        </View>
    );
};

export default Home;