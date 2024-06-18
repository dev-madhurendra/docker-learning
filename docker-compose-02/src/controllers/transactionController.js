const { Transaction } = require('../models');
const { Op } = require('sequelize');

const getTransactions = async (req, res) => {
  const { page = 1, per_page = 10, search = '' } = req.query;
  const limit = parseInt(per_page);
  const offset = (page - 1) * limit;

  const where = search
    ? {
        [Op.or]: [
          { title: { [Op.like]: `%${search}%` } },
          { description: { [Op.like]: `%${search}%` } },
          { price: { [Op.like]: `%${search}%` } }
        ]
      }
    : {};

  const transactions = await Transaction.findAndCountAll({ where, limit, offset });

  res.json({
    data: transactions.rows,
    pagination: {
      total: transactions.count,
      page: parseInt(page),
      per_page: limit
    }
  });transactions
};

const getStatistics = async (req, res) => {
  const { month } = req.query;

  if (!month) {
    return res.status(400).json({ error: 'Month parameter is required' });
  }

  const soldItemsCount = await Transaction.count({
    where: { dateOfSale: { [Op.like]: `%${month}%` }, sold: true }
  });

  const notSoldItemsCount = await Transaction.count({
    where: { dateOfSale: { [Op.like]: `%${month}%` }, sold: false }
  });

  const totalSales = await Transaction.sum('price', {
    where: { dateOfSale: { [Op.like]: `%${month}%` }, sold: true }
  });

  res.json({
    total_sales: totalSales,
    sold_items: soldItemsCount,
    not_sold_items: notSoldItemsCount
  });
};

module.exports = {
  getTransactions,
  getStatistics
};
