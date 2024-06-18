const express = require('express');
const transactionRoutes = require('./routes/transactionRoutes');
const { sequelize } = require('./models');

const app = express();
const port = 3000;

app.use(express.json());
app.use('/api', transactionRoutes);

sequelize.authenticate().then(() => {
  console.log('Database connected...');
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
}).catch(err => {
  console.error('Unable to connect to the database:', err);
});
