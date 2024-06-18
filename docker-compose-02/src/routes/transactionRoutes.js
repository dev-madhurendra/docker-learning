const express = require('express');
const { getTransactions, getStatistics } = require('../controllers/transactionController');
const router = express.Router();

router.get('/transactions', getTransactions);
router.get('/statistics', getStatistics);

module.exports = router;
