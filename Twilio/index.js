const express = require("express");

const app = express();
const port = 3000;

app.use(express.json());

app.post("/api/data", (req, res) => {
  const data = req.body;

  res.send("Data received successfully");
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
