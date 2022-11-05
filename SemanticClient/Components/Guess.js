import { Text, View, Dimensions, StyleSheet } from "react-native";
import { DataTable } from "react-native-paper";

const screenWidth = Dimensions.get("window").width;
const screenHeight = Dimensions.get("window").height;

const Guess = (props) => {
  const MAX_RANK = 1000;

  let distanceCell = "לא קרוב";

  if (props.similarity == 100) {
    distanceCell = "ניצחת";
  } else if (props.rank != -1) {
    distanceCell = (
      <View
        style={{
          width: screenWidth / 4.9,
          height: screenHeight / 25,
          backgroundColor: "grey",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <View
          style={{
            position: "absolute",
            left: 0,
            top: 0,
            height: screenHeight / 25,
            width: (screenWidth * (props.rank / MAX_RANK)) / 4.9,
            backgroundColor: "green",
          }}
        />
        <Text
          style={{
            color: "white",
          }}
        >{`${props.rank}/1000`}</Text>
      </View>
    );
  }

  return (
    <DataTable.Row>
      <DataTable.Cell style={styles.tableCell}>{distanceCell}</DataTable.Cell>
      <DataTable.Cell
        style={styles.tableCell}
      >{`${props.similarity}%`}</DataTable.Cell>
      <DataTable.Cell style={styles.tableCell}>{props.word}</DataTable.Cell>
      <DataTable.Cell style={styles.tableCell}>{props.id}</DataTable.Cell>
    </DataTable.Row>
  );
};

const styles = StyleSheet.create({
  tableCell: {
    flexDirection: "row-reverse",
  },
});

export default Guess;
