import AsyncStorage from "@react-native-async-storage/async-storage";

const timeZoneOffset = -180;

const getTime = () => {
  const today = new Date();
  today.setMilliseconds(0);
  today.setSeconds(0);
  today.setMinutes(0);
  today.setHours(0);
  return today.getTime() + (timeZoneOffset - today.getTimezoneOffset()) * 60000;
};

export default {
  async saveGusses(gusses) {
    const { gussesList, time } = JSON.parse(
      await AsyncStorage.getItem("gusses")
    );
    gusses = { gusses, time: getTime() };
    await AsyncStorage.setItem("gusses", JSON.stringify(gusses));
  },
  async getGusses() {
    let { gusses, time } = JSON.parse(await AsyncStorage.getItem("gusses"));

    if (time != getTime()) {
      gusses = [];
      this.saveGusses(gusses);
    }

    return gusses;
  },
};
