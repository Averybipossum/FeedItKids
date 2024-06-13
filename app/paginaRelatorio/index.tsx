import React, { useState, useEffect } from 'react';
import { View, Image, Text, ScrollView } from 'react-native';
import axios from 'axios';

interface ConsumptionData {
  consumo_plot: string;
  media_plot: string;
  moda_plot: string;
}

const ConsumptionDataComponent: React.FC = () => {
  const [data, setData] = useState<ConsumptionData | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const response = await axios.get('http://3.135.200.39:8000/consumo/consumo_animal/?ano=2024');
        setData(response.data);
      } catch (error) {
        console.error("Failed to fetch data:", error);
        setError('An error occurred while fetching data.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  if (isLoading) {
    return <Text>Loading consumption data...</Text>;
  }

  if (error) {
    return <Text>Error: {error}</Text>;
  }

  if (!data) {
    return <Text>No data found for the specified year.</Text>;
  }

  return (
    <ScrollView>
      <View>
        <Text>Consumo de Alimentos por Grupo</Text>
        <Image
          source={{ uri: `data:image/png;base64,${data.consumo_plot}` }}
          style={{ width: '100%', height: 200 }}
        />
        <Text>Média de Consumo de Alimentos por Grupo</Text>
        <Image
          source={{ uri: `data:image/png;base64,${data.media_plot}` }}
          style={{ width: '100%', height: 200 }}
        />
        <Text>Grupo de Alimento Mais Consumido por Mês</Text>
        <Image
          source={{ uri: `data:image/png;base64,${data.moda_plot}` }}
          style={{ width: '100%', height: 200 }}
        />
      </View>
    </ScrollView>
  );
};

export default ConsumptionDataComponent;