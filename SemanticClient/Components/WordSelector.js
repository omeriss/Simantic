import React, { useState } from "react";
import { View, StyleSheet, Keyboard } from "react-native";
import { IconButton, TextInput } from "react-native-paper";
import asyncStorage from "../api/asyncStorage";
import api from "../api/api";

const WordSelector = ({ gusses, setGesses }) => {
  const [word, setWord] = useState("");

  const onPress = async () => {
    try {
      Keyboard.dismiss();
      const data = await api.testWord(word);

      if (data.similarity == -1) {
        alert("אני לא מכיר את המילה הזאת");
      } else {
        const newGesses = [
          {
            id: gusses.reduce((a, b) => Math.max(a, b.id), 0) + 1,
            similarity: (data.similarity * 100).toFixed(2),
            rank: data.rank,
            word: word,
          },
          ...[...gusses].sort((a, b) => b.similarity - a.similarity),
        ];
        setGesses(newGesses);
        await asyncStorage.saveGusses(newGesses);
      }
    } catch (err) {
      console.log(err);
      console.log("can not get data from server");
    }
  };

  return (
    <View style={styles.selectorContainer}>
      <TextInput
        label="נסה מילה"
        mode="Flat"
        onChangeText={(word) => {
          setWord(word);
        }}
        value={word}
        style={styles.textBox}
      />
      <IconButton
        icon="send-circle-outline"
        onPress={() => onPress()}
        size={45}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  selectorContainer: {
    flexDirection: "row",
    width: "100%",
    justifyContent: "center",
    alignItems: "center",
  },
  textBox: {
    width: "80%",
    aspectRatio: 5 / 1,
    justifyContent: "center",
    textAlign: "right",
    direction: "rtl",
    alignContent: "flex-end",
  },
});

export default WordSelector;
