var express = require('express');
var router = express.Router();
const userHelpers = require('../helpers/user-helpers');

/* GET users listing. */
router.get('/',async function(req, res, next) {
  //const userInput = req.body;
  await userHelpers.list()
  res.send('respond with a resource');
});

module.exports = router;
