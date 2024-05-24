import sys
import os
import pandas as pd
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QTextBrowser, QFileDialog, QTabWidget, QPushButton, QFrame
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtCore import Qt
from tabulate import tabulate

class SQLTextEdit(QTextEdit):
    """Custom QTextEdit widget for SQL input with special handling for Enter and Shift+Enter keys.

    Args:
        parent (QWidget, optional): Parent widget. Defaults to None.
        dashboard (Dashboard, optional): Reference to the Dashboard instance. Defaults to None.
    """

    def __init__(self, parent=None, dashboard=None):
        super().__init__(parent)
        self.dashboard = dashboard

    def keyPressEvent(self, event):
        """Handles key press events to execute query on Enter and add new line on Shift+Enter.

        Args:
            event (QKeyEvent): The key press event.
        """
        if event.key() == Qt.Key.Key_Return and not (event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            self.dashboard.execute_query()
        elif event.key() == Qt.Key.Key_Return and (event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            self.insertPlainText('\n')
        else:
            super().keyPressEvent(event)

class Dashboard(QMainWindow):
    """Main application window for the data dashboard."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Datadash')

        # Create the "New Query" button
        new_query_button = QPushButton("New Query")
        new_query_button.clicked.connect(self.open_file_dialog)

        # Add the "New Query" button to a toolbar
        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(new_query_button)

        # Create a tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)  # Enable closing tabs
        self.tab_widget.tabCloseRequested.connect(self.close_tab)  # Connect to close_tab method

        # Layout for the main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Dictionary to store connections per tab
        self.connections = {}

        # Setup hotkeys for tab navigation
        self.setup_hotkeys()

    def setup_hotkeys(self):
        """Sets up hotkeys for tab navigation and other actions."""
        next_tab_action = QAction(self)
        next_tab_action.setShortcut(QKeySequence("Ctrl+Tab"))
        next_tab_action.triggered.connect(self.next_tab)
        self.addAction(next_tab_action)

        prev_tab_action = QAction(self)
        prev_tab_action.setShortcut(QKeySequence("Ctrl+Shift+Tab"))
        prev_tab_action.triggered.connect(self.previous_tab)
        self.addAction(prev_tab_action)

        close_tab_action = QAction(self)
        close_tab_action.setShortcut(QKeySequence("Ctrl+W"))
        close_tab_action.triggered.connect(self.close_current_tab)
        self.addAction(close_tab_action)

        new_query_action = QAction(self)
        new_query_action.setShortcut(QKeySequence("Ctrl+N"))
        new_query_action.triggered.connect(self.open_file_dialog)
        self.addAction(new_query_action)

        next_left_tab_action = QAction(self)
        next_left_tab_action.setShortcut(QKeySequence("Ctrl+PgUp"))
        next_left_tab_action.triggered.connect(self.previous_tab)
        self.addAction(next_left_tab_action)

        next_right_tab_action = QAction(self)
        next_right_tab_action.setShortcut(QKeySequence("Ctrl+PgDown"))
        next_right_tab_action.triggered.connect(self.next_tab)
        self.addAction(next_right_tab_action)

    def next_tab(self):
        """Switches to the next tab."""
        current_index = self.tab_widget.currentIndex()
        new_index = (current_index + 1) % self.tab_widget.count()
        self.tab_widget.setCurrentIndex(new_index)

    def previous_tab(self):
        """Switches to the previous tab."""
        current_index = self.tab_widget.currentIndex()
        new_index = (current_index - 1) % self.tab_widget.count()
        self.tab_widget.setCurrentIndex(new_index)

    def close_current_tab(self):
        """Closes the current tab."""
        current_index = self.tab_widget.currentIndex()
        if current_index != -1:
            self.close_tab(current_index)

    def create_query_tab(self, file_name):
        """Creates a new tab for SQL queries.

        Args:
            file_name (str): The name of the file associated with the tab.

        Returns:
            QWidget: The widget containing the tab layout.
        """
        query_entry = SQLTextEdit(dashboard=self)
        query_entry.setPlaceholderText("Enter your SQL query here...")
        query_entry.setPlainText("SELECT * FROM data")

        query_output_view = QTextBrowser()

        # Separator between the query input and output
        separator_line = QFrame()
        separator_line.setFrameShape(QFrame.Shape.HLine)
        separator_line.setFrameShadow(QFrame.Shadow.Sunken)

        # Layout for the SQL query tab
        query_layout = QVBoxLayout()
        query_layout.addWidget(query_entry, 1)  # Add query_entry to layout, stretch factor 1
        query_layout.addWidget(separator_line)
        query_layout.addWidget(query_output_view, 2)  # Add query_output_view to layout, stretch factor 2

        query_widget = QWidget()
        query_widget.setLayout(query_layout)

        # Store the query_entry and query_output_view widgets in the widget itself
        query_widget.query_entry = query_entry
        query_widget.query_output_view = query_output_view

        return query_widget

    def execute_query(self):
        """Executes the SQL query from the input field and displays the result in the output view."""
        # Get the current tab index
        current_index = self.tab_widget.currentIndex()
        if current_index == -1:
            return  # No tab is open

        # Get the widgets from the current tab
        current_widget = self.tab_widget.widget(current_index)
        query_entry = current_widget.query_entry
        query_output_view = current_widget.query_output_view
        query = query_entry.toPlainText()

        # Execute the SQL query on the data
        try:
            conn = self.connections[current_index]
            result = pd.read_sql_query(query, conn)

            # Convert DataFrame to HTML table
            html_table = result.to_html(index=False)

            # Display the HTML table in the QTextBrowser widget
            query_output_view.setHtml(html_table)
        except Exception as e:
            query_output_view.setPlainText(str(e))

    def open_file_dialog(self):
        """Opens a file dialog to select a CSV file and loads it into a new tab."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if file_path:
            self.load_csv_tab(file_path)

    def load_csv_tab(self, file_path):
        """Loads a CSV file into a new tab.

        Args:
            file_path (str): The path to the CSV file.
        """
        file_name = os.path.basename(file_path)  # Extract the file name from the file path
        new_query_tab = self.create_query_tab(file_name)
        self.tab_widget.addTab(new_query_tab, file_name)

        try:
            # Read the CSV file into a pandas DataFrame
            data = pd.read_csv(file_path)

            # Create an in-memory SQLite database and load the data into it
            conn = sqlite3.connect(':memory:')
            data.to_sql('data', conn, index=False, if_exists='replace')

            # Store the connection for this tab using tab index as the key
            tab_index = self.tab_widget.indexOf(new_query_tab)
            self.connections[tab_index] = conn
        except Exception as e:
            new_query_tab.query_output_view.setPlainText(str(e))

    def close_tab(self, index):
        """Closes the tab at the specified index.

        Args:
            index (int): The index of the tab to close.
        """
        widget = self.tab_widget.widget(index)
        self.tab_widget.removeTab(index)
        widget.deleteLater()

        # Close the database connection for the tab and remove it from the dictionary
        conn = self.connections.pop(index, None)
        if conn:
            conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())
