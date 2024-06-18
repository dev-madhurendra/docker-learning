const { Sequelize, DataTypes } = require('sequelize');
const config = require('../config');

const sequelize = new Sequelize(config.db);

const Transaction = sequelize.define('Transaction', {
  title: {
    type: DataTypes.STRING,
    allowNull: false
  },
  description: {
    type: DataTypes.STRING,
    allowNull: false
  },
  price: {
    type: DataTypes.FLOAT,
    allowNull: false
  },
  dateOfSale: {
    type: DataTypes.STRING,
    allowNull: false
  },
  sold: {
    type: DataTypes.BOOLEAN,
    allowNull: false
  }
});

sequelize.sync();

module.exports = {
  sequelize,
  Transaction
};
