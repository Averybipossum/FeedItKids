import React, { useState, useEffect } from 'react';
import { View, Animated, Pressable } from 'react-native';
import Checkbox from 'expo-checkbox';

interface CustomCheckboxProps {
  value: boolean;
  onValueChange: () => void;
  color?: string;
  style?: any; // Você pode especificar um tipo mais específico para estilo, como ViewStyle, se desejar
}

const CustomCheckbox: React.FC<CustomCheckboxProps> = ({ value, onValueChange, color, style }) => {
  const [checked, setChecked] = useState(value);
  const animation = new Animated.Value(checked ? 1 : 0);

  useEffect(() => {
    Animated.timing(animation, {
      toValue: checked ? 1 : 0,
      duration: 100, // Duration of the animation
      useNativeDriver: true,
    }).start();
  }, [checked]);

  const toggleCheckbox = () => {
    setChecked(!checked);
    onValueChange();
  };

  return (
    <Pressable onPress={toggleCheckbox}>
      <Animated.View style={[style, { opacity: animation }]}>
        <Checkbox
          value={checked}
          color={color}
          style={{ width: 30, height: 30 }}
        />
      </Animated.View>
    </Pressable>
  );
};

export default CustomCheckbox;
