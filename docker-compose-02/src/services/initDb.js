const axios = require('axios');
const { Transaction, sequelize } = require('../models');
const config = require('../config');

const initDb = async () => {
  await sequelize.sync({ force: true });

  const response = await axios.get(config.apiUrl);
  const transactions = response.data;

  await Transaction.bulkCreate(transactions);
};

initDb().then(() => {
  console.log('Database initialized with seed data.');
  process.exit();
});
