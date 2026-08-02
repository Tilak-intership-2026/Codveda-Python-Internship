# Introduction to API Integration: Cryptocurrency Price Tracker

## 1. Project Overview

The **Cryptocurrency Price Tracker** is developed as part of the **Codveda Technology Python Development Internship – Level 2 (Intermediate)**. The project demonstrates the practical implementation of **RESTful API integration** by retrieving live cryptocurrency market data from the **CoinGecko Public API** and presenting it through a clean command-line interface (CLI).

Unlike applications that rely on static or locally stored data, this project communicates directly with an external web service to fetch real-time information. It highlights the complete API communication lifecycle—from sending an HTTP request to processing a JSON response—while following industry-standard practices for error handling and user interaction.

### Internship Objectives Achieved

* Integrate an external REST API using the **requests** library.
* Perform HTTP **GET** requests to retrieve live cryptocurrency prices.
* Parse and process JSON responses efficiently.
* Display data in a structured and user-friendly format.
* Implement comprehensive exception handling for network and API-related failures.

---

# 2. Understanding REST APIs and HTTP Methods

An **Application Programming Interface (API)** enables communication between independent software systems. Modern web applications primarily use **REST (Representational State Transfer)** APIs over the **HTTP protocol** to exchange data.

Although this project utilizes only the **GET** method, understanding all major HTTP methods is fundamental for developing complete CRUD (Create, Read, Update, Delete) applications.

| HTTP Method     | CRUD Operation | Purpose                                                                          | Usage in This Project                |
| --------------- | -------------- | -------------------------------------------------------------------------------- | ------------------------------------ |
| **GET**         | Read           | Retrieves data from the server without modifying resources. Safe and idempotent. | ✅ Fetches live cryptocurrency prices |
| **POST**        | Create         | Creates a new resource on the server.                                            | ❌ Not required                       |
| **PUT / PATCH** | Update         | Updates existing resources.                                                      | ❌ Not required                       |
| **DELETE**      | Delete         | Removes resources from the server.                                               | ❌ Not required                       |

**Note:** While this application focuses on data retrieval using the **GET** method, the remaining HTTP methods form the foundation of full-stack applications such as task managers, inventory systems, and web-based CRUD platforms.

---

# 3. API Request Lifecycle

The application follows a structured six-stage workflow to retrieve live market data.

### Step 1 — Endpoint Construction

The application dynamically constructs the API endpoint using the cryptocurrency entered by the user.

```text
https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd
```

---

### Step 2 — DNS Resolution

The operating system resolves the domain **api.coingecko.com** into its corresponding IP address through DNS.

---

### Step 3 — Secure Connection Establishment

A secure HTTPS connection is created using the **TCP/TLS handshake**, ensuring encrypted communication between the client and CoinGecko servers.

---

### Step 4 — HTTP GET Request

The application sends an HTTP GET request with appropriate request headers such as:

* User-Agent
* Accept: application/json

---

### Step 5 — Server Processing

The CoinGecko server validates the request, retrieves current market data from its database, and responds with:

* HTTP Status Code (200, 404, 429, etc.)
* JSON response containing the requested cryptocurrency price

---

### Step 6 — Client-Side Processing

The **requests** library converts the JSON response into native Python dictionaries, allowing efficient extraction and display of price information.

---

# 4. Technology Stack

## Python 3.x

Python provides a clean syntax and an extensive ecosystem, making it one of the most widely used languages for automation, API integration, scripting, and backend development.

### Why Python?

* Readable and maintainable code
* Rich standard library
* Excellent third-party package ecosystem
* Ideal for rapid application development

---

## Requests Library

The **requests** library simplifies HTTP communication by abstracting low-level networking details.

### Advantages

* Automatic HTTPS support
* Built-in JSON parsing using `.json()`
* Simplified request handling
* Custom headers and timeout support
* Well-structured exception hierarchy

---

## JSON (JavaScript Object Notation)

JSON is the industry-standard format for exchanging data between clients and servers.

### Benefits

* Lightweight
* Human-readable
* Easy conversion into Python dictionaries and lists
* Widely supported across programming languages

---

## Exception Handling Framework

Network communication is inherently unreliable. To ensure application stability, multiple layers of exception handling are implemented.

| Exception                             | Purpose                                |
| ------------------------------------- | -------------------------------------- |
| `requests.exceptions.ConnectionError` | Internet connection or DNS failure     |
| `requests.exceptions.Timeout`         | Request exceeded timeout limit         |
| `requests.exceptions.HTTPError`       | HTTP 4xx or 5xx server responses       |
| `KeyError`                            | Unexpected or malformed JSON structure |
| `Exception`                           | Handles unforeseen runtime errors      |

This layered approach ensures the application remains stable and provides informative feedback instead of terminating unexpectedly.

---

# 5. Features Implemented

### Real-Time Cryptocurrency Prices

Retrieves the latest market prices directly from the CoinGecko Public API.

### Dynamic Cryptocurrency Search

Users can query any cryptocurrency supported by CoinGecko, including:

* Bitcoin
* Ethereum
* Solana
* Dogecoin
* Litecoin
* Ripple
* And many others

### Interactive Command-Line Interface

Allows users to perform multiple searches within a single execution until they choose to exit.

### Input Validation

Processes user input using:

to ensure consistent, case-insensitive queries.

### Robust Error Handling

Gracefully manages:

* Invalid cryptocurrency names
* Internet connectivity issues
* API failures
* Rate limiting
* Unexpected server responses

The application never crashes unexpectedly and always returns meaningful feedback.

---

# 6. Learning Outcomes

This project demonstrates proficiency in the following areas:

* Understanding RESTful API architecture.
* Working with HTTP request-response communication.
* Making API requests using Python.
* Parsing and processing JSON data.
* Implementing production-oriented exception handling.
* Developing reliable network-dependent applications.
* Transitioning from local data processing to distributed web-based systems.

These skills form the foundation for modern backend development, cloud computing, automation, and full-stack software engineering.

---

# 7. Future Enhancements

Potential improvements include:

* Save favorite cryptocurrencies using the **POST** concept with a local JSON database.
* Implement request throttling to comply with API rate limits.
* Visualize historical price trends using **Matplotlib**.
* Cache frequently requested data using **functools.lru_cache** to reduce redundant API calls.
* Display additional market information such as:

  * Market Capitalization
  * 24-Hour Price Change
  * Trading Volume
  * Market Rank
* Add support for multiple fiat currencies (USD, EUR, INR, GBP, etc.).
* Export cryptocurrency data to CSV or Excel for further analysis.
* Develop a graphical user interface (GUI) using Tkinter or PyQt.
* Integrate real-time notifications for significant market movements.

---

# Conclusion

The **Cryptocurrency Price Tracker** demonstrates the practical application of REST API integration using Python. By combining live data retrieval, JSON processing, structured exception handling, and an intuitive command-line interface, the project reflects industry-standard software development practices. It serves as a strong foundation for more advanced API-driven applications while reinforcing essential concepts in networking, backend development, and modern Python programming.
#=====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
# CRUD Operations in REST APIs

REST APIs are commonly designed around the **CRUD (Create, Read, Update, Delete)** model. Each CRUD operation corresponds to a specific HTTP method that defines how a client interacts with server resources.

| CRUD Operation | HTTP Method     | Purpose                                                                                                            | Usage in This Project                                              |
| -------------- | --------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| **Create**     | **POST**        | Creates a new resource on the server by sending data in the request body.                                          | ❌ Not Used                                                         |
| **Read**       | **GET**         | Retrieves existing data from the server without modifying any resources.                                           | ✅ Used to fetch live cryptocurrency prices from the CoinGecko API. |
| **Update**     | **PUT / PATCH** | Updates an existing resource. **PUT** replaces the entire resource, while **PATCH** modifies only specific fields. | ❌ Not Used                                                         |
| **Delete**     | **DELETE**      | Removes an existing resource from the server permanently.                                                          | ❌ Not Used                                                         |

### CRUD Usage in This Project

The **Cryptocurrency Price Tracker** is a **Read-only** application. It interacts with the CoinGecko Public API exclusively through the **HTTP GET** method to retrieve real-time cryptocurrency prices.

Since the application does not create, modify, or delete any server-side resources, the remaining CRUD operations (**POST, PUT/PATCH, and DELETE**) are not required.

Although only the **Read** operation is implemented, understanding all four CRUD operations is essential for developing complete RESTful applications such as task management systems, inventory management software, blogging platforms, and full-stack web applications.
