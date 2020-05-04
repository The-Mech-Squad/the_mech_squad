const express = require('express');
const app = express();

app.listen(3000, () => console.log('listening at 3000'));
app.use(express.static('client'));

app.post('/temperature', (request, response) => {
    console.log(request);
});

app.get('/temperature', (request, response) => {
    console.log(request);
});