# Python Socket Chat App
This project is a **basic client-server chat application** implemented using Python's `socket` library. It facilitates **two-way text communication** between a server and a client on the same local network (or the same machine).

![Static Badge](https://img.shields.io/badge/python-socket-blue)


## 🔧 **Project Overview**

### **Purpose**:
To demonstrate **network socket programming** through a simple interactive **chat interface** where a server and a client exchange messages.

---

## 📁 **Files & Roles**

### **1. Server Side (server.py)**

* **Creates a socket** and binds it to a specified IP and port (`HOST_ADDRESS`, `12345`).
* Waits for a connection from a client (`server_socket.listen()` and `accept()`).
* After the client connects, it sends a welcome message.
* Enters a loop to:

  * Receive messages from the client.
  * Respond with messages entered by the server user.
  * Exit the loop if either party sends `"quit"`.

### **2. Client Side (client.py)**

* **Creates a socket** and connects to the server on the same IP and port.
* After connecting, receives and prints the welcome message from the server.
* Enters a loop to:

  * Read messages from the server.
  * Respond with input from the client user.
  * Exit the loop if either party sends `"quit"`.

---

## 🔁 **How Communication Works**

1. **Server starts first** and listens for a connection.
2. **Client starts** and connects to the server.
3. They exchange text messages in turn (like a basic chat app).
4. Typing `"quit"` on either side closes the connection.

---

## 🧠 **Key Concepts Demonstrated**

* TCP socket communication (`AF_INET`, `SOCK_STREAM`)
* Encoding/decoding messages using `utf-8`
* Message-based interaction using `recv()` and `send()`
* Blocking I/O with `input()`, making the program synchronous
* Graceful shutdown of sockets

---

## ⚠️ **Limitations**

* Only supports **one client at a time**.
* **Blocking I/O** — both server and client wait for user input before proceeding.
* No error handling (e.g. connection drop, invalid messages).
* Designed for **local testing** (`socket.gethostname()`); not suitable for remote or multi-client use without modifications.

---

## ✅ **Use Case / Learning Outcome**

This is a great starting project for beginners learning about:

* Network programming
* Client-server architecture
* Real-time communication basics

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Terminal or command prompt
- Two terminal windows (one for server, one for client)

### 📁 File Structure

```bash
.
├── server.py   # Server-side script
├── client.py   # Client-side script
└── README.md   # This file
````

### 🔧 Usage

#### 1. Start the Server

```bash
python3 server.py
```

#### 2. Start the Client (in a new terminal)

```bash
python3 client.py
```

### 💡 Notes

* Make sure the server is running **before** the client connects.
* To end the chat, type `quit` on either side.

## 🛠 Future Improvements (Ideas)

* Add support for multiple clients using threading
* Build a GUI with `tkinter` or `PyQt`
* Add authentication or encryption
* Support messages from both ends without blocking input

## 📄 License

This project is open-source and free to use for learning and personal development.

---

**Author**: *Rodrick Cheruiyot*
