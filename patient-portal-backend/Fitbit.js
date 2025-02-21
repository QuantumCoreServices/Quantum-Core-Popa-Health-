// Example: Fetching data from Fitbit API using axios
const axios = require('axios');

async function fetchFitbitData(accessToken) {
  try {
    const response = await axios.get('https://api.fitbit.com/1/user/-/activities/heart/date/today/1d.json', {
      headers: { Authorization: `Bearer ${accessToken}` }
    });
    return response.data;
  } catch (error) {
    throw new Error('Error fetching Fitbit data');
  }
}
