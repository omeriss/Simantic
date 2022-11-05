import React, { useEffect, useState } from "react";
import { View, StyleSheet } from "react-native";
import { DarkTheme, Provider as PaperProvider } from "react-native-paper";
import WordSelector from "./Components/WordSelector";
import GuessList from "./Components/GuessList";
import asyncStorage from "./api/asyncStorage";

const App = () => {
  const [gusses, setGesses] = useState([]);

  useEffect(() => {
    const changeGesees = async () => {
      setGesses((await asyncStorage.getGusses()) || []);
    };

    changeGesees();
  }, []);

  return (
    <PaperProvider theme={styles.theme}>
      <View style={styles.app}>
        <WordSelector gusses={gusses} setGesses={setGesses} />
        <GuessList gusses={gusses} />
      </View>
    </PaperProvider>
  );
};

const styles = StyleSheet.create({
  theme: {
    ...DarkTheme,
    roundness: 2,
    colors: {
      ...DarkTheme.colors,
      primary: "#3498db",
      accent: "#f1c40f",
    },
  },
  app: {
    paddingTop: "10%",
    flex: 1,
    alignItems: "center",
    paddingRight: "5%",
    paddingLeft: "5%",
    backgroundColor: "black",
  },
});

export default App;
