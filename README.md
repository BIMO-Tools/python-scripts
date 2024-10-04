
![run_python_cover](https://github.com/user-attachments/assets/bfba335f-8ee6-4665-8fc6-f75f4372acd3)

# BIMO Run Python Scripts

Welcome to the **BIMO Revit Python Scripts** repository! This repository is a collection of useful Python scripts designed to work with the **[Run Python](https://bimo.tools/tools?button=runPython)** command in the **[BIMO Add-in](https://bimo.tools)** for Autodesk Revit. The scripts aim to automate routine and complex tasks, streamlining workflows for Revit users.

## 📋 About

The **BIMO Add-in for Revit** includes a powerful **[Run Python](https://bimo.tools/tools?button=runPython)** command, which allows users to execute custom Python scripts within the Revit environment. This repository is intended to provide ready-to-use scripts for various tasks, along with examples to help you write your own.

Feel free to explore the scripts, adapt them to your projects, or contribute by sharing your own scripts!

## 🗂️ Repository Structure

The scripts in this repository are organized into categories to make it easier to find relevant code for your needs:

- **`wall_scripts/`**: Scripts related to wall management, such as counting walls, calculating wall areas, or modifying wall properties.
- **`door_scripts/`**: Scripts for managing doors, including swing direction checks, door schedules, and door counts.
- **`model_management/`**: Scripts to manage and optimize Revit models, like purging unused elements, auditing models, and adjusting views.
- **`room_scripts/`**: Scripts related to room management, such as calculating room volumes, adjusting room boundaries, and renaming rooms.
- **`miscellaneous/`**: Various scripts for tasks not covered in the other categories.

Each folder contains a README file with specific instructions on how to use the scripts in that category.

## 🛠️ How to Use the Scripts

### Requirements

- Autodesk Revit with the **BIMO Add-in** installed.
- Python installed on your system (if you plan to write your own scripts).

### Running a Script

1. Open Autodesk Revit.
2. Go to the **BIMO** tab on the Revit toolbar.
3. Click the **[Run Python](https://bimo.tools/tools?button=runPython)** button.
4. From the dropdown menu, select the Python script you want to execute (or load a new script from your computer).
5. Click **OK** to run the script and view the results.

### Example Scripts

Here are some example scripts you can start with:

1. **Count Walls**: Counts the total number of walls in the active model.
2. **Door Swing Direction**: Checks the swing direction of all doors and stores the result in the door's parameters.
3. **Purge Unused Elements**: Cleans up the Revit model by purging unused families, materials, and styles.

## 🤝 Contributing

We welcome contributions from the community! If you have a useful script that you'd like to share, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b your-feature-branch`).
3. Add your script in the appropriate folder.
4. Commit your changes (`git commit -m 'Add new Python script'`).
5. Push to the branch (`git push origin your-feature-branch`).
6. Open a pull request and provide a brief description of your script.

## 💬 Support

If you encounter any issues or have questions about the scripts, feel free to open an issue in the GitHub repository or reach out to the community for support.

For more information on the **BIMO Add-in**, visit the [BIMO Tools website](https://bimo.tools).

## 📜 License

This repository is licensed under the [MIT License](LICENSE).
