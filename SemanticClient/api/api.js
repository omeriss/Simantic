import axios from "axios";

const baseURL = "http://10.11.35.20/";
const baseConnection = axios.create({
  baseURL,
});

export default {
  async testWord(word) {
    const data = (await baseConnection.get(`/test/${word}`)).data;
    console.log(data);

    return data;
  },
};
