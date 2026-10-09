# 🇺🇸 US States Guessing Game

A small **Python guessing game** where the player tries to identify the names of all 50 states of the United States.

This project was created as a practical exercise to practice working with the **Pandas library**, **CSV files**, and external data in Python.

---

## 🎯 About the Project

The player is shown a map of the United States and is asked to enter the name of a state.

Whenever a correct state name is entered, its name is displayed on the map in its corresponding location.

The objective is to correctly identify all **50 US states**.

The game can also keep track of the states that have not yet been identified, allowing the player to continue practicing until all states have been guessed.

---

## 🧠 Concepts Practiced

This project focuses primarily on working with data and the Pandas library.

### Python

- Variables
- Loops
- Conditional statements
- Functions
- Lists
- Tuples
- String manipulation
- User input
- File handling

### Pandas

- Importing Pandas
- Reading CSV files
- Working with DataFrames
- Accessing rows and columns
- Filtering DataFrames
- Retrieving specific values
- Iterating through DataFrame rows

### CSV / Data Handling

- Reading structured data from a CSV file
- Using CSV data as the source for the game
- Matching user input against stored data
- Retrieving coordinates and state names from the dataset
- Generating a list of missing states

---

## 🗂️ Project Structure

```text
US-States-Guessing-Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
│
└── README.md
```

### Files

#### `main.py`

Contains the main game logic, including:

- Loading the state data
- Receiving player input
- Checking whether the answer is a valid state
- Displaying correctly guessed states
- Tracking progress
- Generating the list of states that were not guessed

#### `50_states.csv`

Contains the data used by the game.

The CSV file contains information such as:

- State names
- X coordinates
- Y coordinates

These coordinates are used to determine where each state name should be displayed on the map.

#### `blank_states_img.gif`

The blank map used as the game's visual interface.

---

## 🎮 How to Play

1. Run `main.py`.
2. A blank map of the United States will appear.
3. Enter the name of a US state in the input box.
4. If the answer is correct, the state name will appear on the map.
5. Continue guessing until all 50 states have been identified.

When the game ends, a CSV file can be generated containing the states that were not correctly identified.

---

## 📊 Data Processing

The state information is loaded from the CSV file using Pandas.

For example:

```python
import pandas as pd

data = pd.read_csv("50_states.csv")
```

The DataFrame can then be searched to find information about a specific state.

For example:

```python
state_data = data[data["state"] == answer]
```

The corresponding coordinates can then be used to place the state name on the map.

---

## 📈 Game Progress

The game keeps track of the states that have already been correctly identified.

For example:

```text
States guessed: 25 / 50
```

The game continues until:

- All 50 states have been guessed, or
- The player chooses to exit.

---

## 📝 Missing States

When the player exits before identifying all 50 states, the program can compare the list of correctly guessed states with the complete list of states from the CSV file.

This allows it to determine which states are still missing.

For example:

```text
Alaska
Hawaii
Maine
Vermont
Wyoming
...
```

The missing states can then be exported to a separate CSV file for further reference or practice.

---

## 🛠️ Technologies

- **Python**
- **Pandas**
- **CSV**
- **Turtle Graphics**
- **PyCharm**
- **Git**
- **GitHub**

---

## 📚 Learning Objectives

Through this project, I am practicing how to:

- Import and use the Pandas library
- Read data from CSV files
- Work with DataFrames
- Search and filter data
- Extract values from a DataFrame
- Combine external data with a Python program
- Manipulate lists of data
- Compare user input against stored data
- Generate new data files
- Use file handling in a practical application

---

## 📈 Development Progress

- [x] Load the state data from a CSV file
- [x] Create the blank US map
- [x] Receive user guesses
- [x] Check guesses against the state dataset
- [x] Display correctly guessed states
- [x] Track the number of correctly guessed states
- [x] Generate a list of missing states
- [x] Export missing states to a CSV file

---

## 📖 Part of My Python Studies

This project is part of my ongoing study of **Python and data manipulation**.

Unlike my previous OOP projects, this exercise focuses more heavily on **working with external datasets and the Pandas library**.

The project provides practical experience with the process of:

```text
CSV Data
    ↓
Pandas DataFrame
    ↓
Search / Filter Data
    ↓
Process Information
    ↓
Use Data in the Application
    ↓
Generate New Data
```

---

## 👩‍💻 Author

**Julia Nakamura**

This project is part of my programming studies and GitHub portfolio.

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.
