const express = require("express");
const multer = require("multer");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());
app.use(express.json());

// 📌 Multer Storage for Image Uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/");
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + "-" + file.originalname);
  },
});
const upload = multer({ storage });

// 📌 Image Upload API
app.post("/upload", upload.single("image"), (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: "No file uploaded" });
  }
  res.json({ imageUrl: `http://localhost:5000/uploads/${req.file.filename}` });
});

// 📌 Blogs JSON File
const BLOGS_FILE = "blogs.json";

// 📌 Get Blogs API
app.get("/blogs", (req, res) => {
  fs.readFile(BLOGS_FILE, (err, data) => {
    if (err) return res.status(500).json({ error: "Error reading file" });
    res.json(JSON.parse(data));
  });
});

// 📌 Add Blog API
app.post("/blogs", (req, res) => {
  const newBlog = req.body;

  fs.readFile(BLOGS_FILE, (err, data) => {
    let blogs = [];
    if (!err) blogs = JSON.parse(data);

    blogs.push(newBlog);

    fs.writeFile(BLOGS_FILE, JSON.stringify(blogs, null, 2), (err) => {
      if (err) return res.status(500).json({ error: "Error saving blog" });
      res.json({ message: "Blog saved", blog: newBlog });
    });
  });
});

app.listen(5000, () => console.log("Server running on port 5000"));
