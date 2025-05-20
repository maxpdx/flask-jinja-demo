# Flask Jinja Demo

A minimal Flask application that renders HTML templates using Jinja and supports automatic browser reloading when templates are modified. Perfect for rapid frontend-backend prototyping using Python.

## 🚀 Features

- ✅ Flask + Jinja templating
- 🔄 Auto-reloads the browser when HTML templates are updated
- ⚙️ Simple, single-file Python setup
- 👨‍💻 Dev-friendly: works with VS Code + WSL

---

## 📦 Requirements

- Python 3.x
- [pip](https://pip.pypa.io/)
- Recommended: [WSL + VS Code](https://code.visualstudio.com/docs/remote/wsl)

---

## 🛠 Installation

```bash
# Clone the repo
git clone https://github.com/maxpdx/flask-jinja-demo.git
cd flask-jinja-demo

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Running the App

1. `python3 app.py`
1. Open your browser to: http://localhost:5500
1. Now edit `templates/index.html`, save, and your browser will reload automatically.
