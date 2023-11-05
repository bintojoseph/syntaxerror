const { PythonShell } = require("python-shell");
const { response } = require("express");
var db = require("../config/connection");
var collection = require("../config/collections");

const { MongoClient } = require("mongodb");
// or as an es module:
// import { MongoClient } from 'mongodb'

module.exports = {
  recom: async () => {
    console.log("test");
    const options = {
      scriptPath: "./helpers",
      //args: [userInput],
    };

    PythonShell.run("test.py", options).then((messages) => {
      console.log(messages);
    });
    console.log("...");
    // if (err) console.log(err) ;
    // if (results) console.log(results)
    // const recommendations = results;
    // console.log(results) // Process the recommendations as needed
    // res.json({ recommendations });
    console.log("Import success");
  },
  list: async() => {
    // Connection URL
    const url = "mongodb://localhost:27017";
    const client = new MongoClient(url);

    // Database Name
    const dbName = "restaurant";

    async function main() {
      // Use connect method to connect to the server
      await client.connect();
      console.log("Connected successfully to server");
      const db = client.db(dbName);
      const collection = db.collection("menu");

      // the following code examples can be pasted here...
      const findResult = await collection.find({}).toArray();
      console.log('Found documents =>', findResult);

      return "done.";
    }

    main()
      .then(console.log)
      .catch(console.error);
  },
};
