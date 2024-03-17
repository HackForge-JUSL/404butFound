// index.js
const express = require("express");
const bodyParser = require("body-parser");
const twilio = require("twilio");

const app = express();
const port = process.env.PORT || 3000;

const { TWILIO_ACCOUNT_SID, YOUR_TWILIO_AUTH_TOKEN } = process.env;

// Twilio credentials
const accountSid = TWILIO_ACCOUNT_SID;
const authToken = YOUR_TWILIO_AUTH_TOKEN;
const client = twilio(accountSid, authToken);

app.use(bodyParser.urlencoded({ extended: false }));

// Route for receiving SMS messages
app.post("/sms", (req, res) => {
  const receivedMessage = req.body.Body;
  const senderNumber = req.body.From;

  console.log(`Received message: ${receivedMessage} from ${senderNumber}`);

  // Process the received message and decide on a reply
  let replyMessage = "";
  if (receivedMessage.toLowerCase().includes("hello")) {
    replyMessage = "Hi there! How can I assist you?";
  } else {
    replyMessage = "Sorry, I didn't understand that. Please try again.";
  }

  // Send a reply message
  client.messages
    .create({
      body: replyMessage,
      to: senderNumber,
      from: "YOUR_TWILIO_PHONE_NUMBER",
    })
    .then((message) => console.log(`Sent reply: ${message.sid}`));

  res.sendStatus(200);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
