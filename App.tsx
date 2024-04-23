import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

import Home from './screens/login'
import Cadastro from './screens/cadastro';
const App  = () => {

  return (
    <NavigationContainer>
    <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={Home}
        />
        <Stack.Screen name="Profile" component={Cadastro} />
      </Stack.Navigator>

  </NavigationContainer>

  );
};

export default App;