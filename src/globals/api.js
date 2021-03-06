
// let baseUrl = "http://128.195.53.189:4001/api";
// let baseUrl = "https://uci-tippers.ics.uci.edu/api";
// let baseUrl = "https://dev-tippers.ics.uci.edu/api";
// let baseUrl = "http://home-tippers.ics.uci.edu/api";
let baseUrl = process.env.REACT_APP_BASE_URL;

export default {
  entity: baseUrl + "/entity",
  observation: baseUrl + "/observation/" + process.env.REACT_APP_OBSERVATION_ID,
  query: baseUrl + "/test/query",
}