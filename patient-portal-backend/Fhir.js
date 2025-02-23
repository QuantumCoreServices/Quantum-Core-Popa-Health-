const FHIR = require('fhir.js');
const client = FHIR({
  baseUrl: 'https://ehr.example.com/fhir'
});

client.read({ type: 'Patient', id: '12345' })
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
