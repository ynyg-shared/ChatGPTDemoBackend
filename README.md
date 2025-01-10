# **ChatGPT Demo**

![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20|%203.13-blue)  
![License](https://img.shields.io/badge/license-MIT-green)  
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688)  
![Frontend](https://img.shields.io/badge/Frontend-Vue.js-42b883)

這是一個使用 **ChatGPT** 進行對話的簡單示例，結合了 **FastAPI** 作為後端框架，並使用 **Vue.js** 作為前端框架。

---

## 📖 **目錄**

- [簡介](#簡介)
- [環境要求](#環境要求)
- [安裝](#安裝)
- [使用說明](#使用說明)
- [功能特性](#功能特性)
- [授權](#授權)
- [聯繫方式](#聯繫方式)

---

## 📝 **簡介**

這個項目展示了如何整合 **ChatGPT** 以進行對話功能，並支持以下特性：

- **多輪對話**：支持上下文的記憶與連貫性。
- **多主題對話**：可根據需求切換話題。
- **WebSocket 支持**：提供流式數據傳輸，提升用戶體驗。
- **數據持久化**：支持保存與加載對話內容。

後端使用 **FastAPI**，前端採用 **Vue.js**。

---

## 🔧 **環境要求**

本項目支持以下 Python 版本：

| Python 版本 | 支持狀態 |
|-----------|------|
| **3.10**  | ✅    |
| **3.11**  | ✅    |
| **3.12**  | ✅    |
| **3.13**  | ✅    |

⚠️ **其他 Python 版本可能無法保證兼容性**。

---

## 📦 **安裝**

請按照以下步驟完成項目的安裝：

1. **克隆代碼庫**：
   ```bash
   git clone https://github.com/ynyg-shared/ChatGPTDemoBackend.git
   cd ChatGPTDemoBackend
   ```
2. **安裝依賴**：
   ```bash
   pip install -r requirements.txt
    ```
3. 配置環境變量： 將 .env 文件中的 OPENAI_API_KEY 替換為你的 OpenAI API 密鑰。
4. **啟動服務器**：
   ```bash
   uvicorn main:app --reload
   ```

## 🚀 **使用說明**

1. 啟動服務器後，訪問以下地址打開應用程序：
   ``` bash
   http://127.0.0.1:8000
    ```
2. 開始與 ChatGPT 進行交互，支持多輪對話與主題切換。

## ✨ **功能特性**

- 支持多輪對話
- 支持多個對話主題
- 支持 WebSocket 提供流式對話
- 支持對話歷史記錄
- 支持對話內容的保存和加載

## 📜 **授權**

本項目基於 [MIT協議](LICENSE) 進行分發和使用。歡迎進行修改與二次開發，但請保留原始作者的聲明。

## 📬 **聯繫方式**

如果有任何問題，請隨時聯繫我們：

| 聯繫方式      | 詳情                |
|-----------|-------------------|
| **Email** | 3305534115@qq.com |

