import { ScrollView, StyleSheet, SafeAreaView, View } from "react-native";
import {
  DataTable,
  Banner,
  Text,
  Dialog,
  Button,
  Paragraph,
} from "react-native-paper";
import { useState } from "react";
import Guess from "./Guess";

const GuessList = ({ gusses }) => {
  const [visible, setVisible] = useState(true);
  const hideDialog = () => {
    setVisible(false);
  };

  return (
    <DataTable>
      <DataTable.Header>
        <DataTable.Title style={styles.tableHeader}>מרחק</DataTable.Title>
        <DataTable.Title style={styles.tableHeader}>קרבה</DataTable.Title>
        <DataTable.Title style={styles.tableHeader}>ניחוש</DataTable.Title>
        <DataTable.Title style={styles.tableHeader}>#</DataTable.Title>
      </DataTable.Header>
      <SafeAreaView style={styles.container}>
        <ScrollView style={styles.scrollView}>
          {gusses.map((guess) => (
            <Guess
              id={guess.id}
              word={guess.word}
              similarity={guess.similarity}
              rank={guess.rank}
              key={guess.id}
            />
          ))}
        </ScrollView>
      </SafeAreaView>
      {gusses.reduce((a, b) => Math.max(a, b.similarity), 0) === 100 &&
        visible && (
          <Dialog visible={true} onDismiss={hideDialog}>
            <Dialog.Title style={styles.rtl}>מצאת את המילה</Dialog.Title>
            <Dialog.Content>
              <Paragraph style={styles.rtl}>
                כל הכבוד!! מצאת את המילה של היום.
              </Paragraph>
            </Dialog.Content>
            <Button onPress={hideDialog}>המשך לשחק</Button>
          </Dialog>
        )}
    </DataTable>
  );
};

const styles = StyleSheet.create({
  tableHeader: {
    flexDirection: "row-reverse",
  },
  container: {
    flexDirection: "column",
  },
  scrollView: {
    height: "85%",
    width: "100%",
    marginBottom: 20,
    alignSelf: "center",
  },
  winContainer: {
    justifyContent: "center",
    alignItems: "center",
  },
  winText: {
    justifyContent: "center",
    alignItems: "center",
    color: "blue",
    fontWeight: "bold",
    fontSize: 30,
  },
  rtl: {
    textAlign: "right",
  },
});

export default GuessList;
