import React, { useState } from 'react';
import { View, Pressable, StyleSheet } from 'react-native';
import { AntDesign } from '@expo/vector-icons'; // Importe os ícones do AntDesign

interface CustomCheckboxProps {
  value: boolean;
  onValueChange: () => void;
  color?: string;
  style?: any;
}

const CustomCheckbox: React.FC<CustomCheckboxProps> = ({ value, onValueChange, color, style }) => {
  const [checked, setChecked] = useState(value);

  const toggleCheckbox = () => {
    setChecked(!checked);
    onValueChange();
  };

  return (
    <Pressable onPress={toggleCheckbox} style={[styles.checkbox, style]}>
      <AntDesign name={checked ? 'checkcircle' : 'checkcircleo'} size={40} color={color || '#07ce1b'} />
    </Pressable>
  );
};

const styles = StyleSheet.create({
  checkbox: {
    borderRadius: 100, // Define a borda do checkbox como circular
    width: 50,
    height: 50,
    alignItems: 'center',
    justifyContent: 'center' },
});

export default CustomCheckbox;
