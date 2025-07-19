# 💱 Currency Converter CLI (Python)

A command-line currency converter built using **Python** that fetches real-time exchange rates from [x-rates.com](https://www.x-rates.com). It allows you to convert currency between 50+ countries by parsing live data and supports offline fallback as well.

---

## 📦 Features

- 🌐 **Real-time exchange rates** using `requests` and web scraping
- ⚡ **Fast command-line interface** (CLI)
- 🔁 **Convert between any two supported currencies**
- 💾 **Offline fallback** using local file (`main_info.txt`)
- 📄 All country names and conversion data are stored in plain text

---

## 🛠️ Requirements

- Python 3.x
- Internet connection (for real-time update)
- Works only on **Windows** (uses `os.popen()` and `wmic` for disk info parsing)

### Install Dependencies

```bash
pip install requests
```

---

## 📁 File Structure

```
currency_converter/
│
├── main_currency_converter.py    # Main CLI script
├── main_info.txt                 # Stores parsed currency data (updated daily)
├── string_info.txt               # HTML content of x-rates.com table
```

---

## 🚀 How to Use

### 1. Run the App

```bash
python main_currency_converter.py
```

### 2. Enter Conversion Details

```text
📅 Date: 19/07/2025
[INFO] Online currency data fetched successfully.
[INFO] 'main_info.txt' updated with fresh data.

--------------💱 Available Countries---------------
1 ) Euro
2 ) Indian Rupee
3 ) Japanese Yen
...
54 ) US Dollar

💰 Enter amount: 100
🔁 From country: US Dollar
➡️ Convert Us Dollar to: Indian Rupee
💰 Result: 100 US Dollar is equal to 8324.00 Indian Rupee
```

---

## 🔍 How It Works

1. Downloads the HTML table from `x-rates.com`
2. Parses rows with `<td>` tags to extract:
   - Country name
   - Conversion rate (USD → Country)
   - USD equivalent (Country → USD)
3. Updates `main_info.txt` with this structured data
4. Allows the user to:
   - Input amount
   - Select source and destination currencies
   - Get real-time conversion

---

## 📝 Sample `main_info.txt` Format

```
Indian Rupee	83.24	0.012
Euro	0.91	1.0989
Japanese Yen	156.10	0.0064
```

---

## ⚠️ Notes

- Make sure you are **connected to the internet** when running for the first time.
- If the connection fails, it uses previously saved data from `main_info.txt`.
- The HTML response is saved in `string_info.txt` for parsing.

---

## 🧠 Troubleshooting

- If `main_info.txt` is empty:
  - Ensure you're online when the app runs.
  - Make sure the HTML structure of x-rates hasn't changed.
- If you see `[ERROR] 'string_info.txt' not found`, it means the site wasn't fetched.

---

## ✍️ Author

Developed by **Ellalan (whitedevilprogrammer)**  
🔗 [GitHub Profile »](https://github.com/whitedevilprogrammer)

---

## 📜 License

This project is licensed under the **MIT License**.  
Free to use, modify, and distribute with credit.
