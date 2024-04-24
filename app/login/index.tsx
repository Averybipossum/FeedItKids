import * as React from 'react';
import { Button, View, Text } from 'react-native';
import { Link, router } from "expo-router";

function LoginScreen() {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Login Screen</Text>
        <Button
                title="ir para Home"
                onPress={()=>router.replace("/home")}
                color="#841584"
            />
      </View>
    );
  }

  export default LoginScreen;