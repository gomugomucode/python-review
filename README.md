# Python Review Repository

A structured repository containing practical Python projects, command-line applications, and data manipulation reviews.

---

## 📁 Repository Structure

```
python-review/
├── expense-tracker-cli/         # Interactive CLI application for expense tracking
│   ├── main.py                  # Application entry point and interactive menu
│   ├── expense.py               # Expense model with JSON serialization
│   ├── addexpense.py            # Expense collection management and persistence
│   ├── viewexpense.py           # Formatted table viewing, updating, and deletion
│   └── expense.json             # Persistent JSON storage
├── numpy-pandas-matplotlib/     # Data science & analytics practice
│   ├── main.py                  # Synthetic transaction dataset generation (NumPy & Pandas)
│   └── try.py                   # Data cleaning experiments (missing values, outliers)
├── torch.ipynb                  # PyTorch & CUDA GPU acceleration verification & tests
├── pyrightconfig.json           # Python language server and path configuration
├── requirements.txt             # Project dependencies (including PyTorch with CUDA 13.0)
├── .gitignore                   # Ignored files and environments
└── README.md                    # Repository documentation
```

---

## 🚀 Projects Overview

### 1. Expense Tracker CLI (`expense-tracker-cli/`)

A command-line expense management application built using Python and [InquirerPy](https://github.com/kazhala/InquirerPy) for interactive terminal UI navigation.

- **Features**:
  - Interactive arrow-key navigation menus
  - Add expenses with category, description, and custom/automatic timestamps
  - View expenses in an aligned summary table with total spending calculation
  - Update any field of existing expenses
  - Delete individual expenses
  - Automatic persistence to `expense.json`

**How to Run:**
```bash
# Run from repository root
python expense-tracker-cli/main.py

# Or run from inside the folder
cd expense-tracker-cli
python main.py
```

---

### 2. Data Science Review (`numpy-pandas-matplotlib/`)

Exercises and scripts for generating realistic datasets, applying statistical distributions, and practicing data manipulation.

- **Features**:
  - Generates realistic synthetic transaction records using `numpy.random`
  - Simulates realistic spending behavior using exponential distributions
  - Implements category and regional probability distributions
  - Injects realistic data imperfections (missing values / `NaN` and statistical outliers)
  - Packages results into clean `pandas.DataFrame` structures for analysis

**How to Run:**
```bash
python numpy-pandas-matplotlib/main.py
python numpy-pandas-matplotlib/try.py
```

---

### 3. PyTorch & CUDA Acceleration (`torch.ipynb`)

Jupyter notebook for verifying PyTorch installation, hardware acceleration, and GPU computing.

- **Features**:
  - Validates PyTorch environment, CUDA runtime build, and device count
  - Detects dedicated NVIDIA GPU hardware (tested with **NVIDIA GeForce RTX 5050 Laptop GPU**)
  - Configured with CUDA 13.0 (`cu130`) for native compatibility with NVIDIA Blackwell architecture (`sm_120`)
  - Compares CPU vs. GPU tensor allocation and device management

**How to Run:**
Open [`torch.ipynb`](torch.ipynb) in VS Code or Jupyter Lab, select the `myenv` kernel, and run all cells.

---

## 🛠️ Environment Setup & Installation

1. **Prerequisites**: Python 3.10+ (tested on Python 3.12).

2. **Create and activate a virtual environment**:
   ```bash
   # Windows (PowerShell)
   python -m venv myenv
   .\myenv\Scripts\Activate.ps1

   # macOS / Linux
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install Dependencies**:
   - **For CPU-only or general libraries:**
     ```bash
     pip install -r requirements.txt
     ```
   - **For NVIDIA GPU (CUDA 13.0) Acceleration:**
     ```bash
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
     ```

---

## 📝 Configuration & Tooling

- **`pyrightconfig.json`**: Configured to resolve package imports from both subproject folders (`expense-tracker-cli` and `numpy-pandas-matplotlib`) as well as the virtual environment.
- **`.vscode/settings.json`**: Pre-configured Python interpreter and analysis paths for Visual Studio Code.
- **CUDA Support**: Verified on Windows 11 with NVIDIA driver 610.88+ and RTX 50-series (Blackwell) GPU hardware.
