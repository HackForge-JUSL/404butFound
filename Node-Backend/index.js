const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcrypt");

const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors());

const DB = process.env.VITE_APP_MONGO_SERVER;
mongoose
  .connect(DB, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("MongoDB connected");
  })
  .catch((error) => {
    console.log("Error in connecting to server", error);
  });

const User = require("./Models/UsersModel");
const Doctor = require("./Models/DoctorModel");
const Appointment = require("./Models/AppointmentModel");

// Routes
app.get("/", (req, res) => {
  res.send("Hello, world!");
});
