import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QGroupBox, QLabel, QFileDialog,
                             QScrollArea, QMainWindow, QSizePolicy, QSplitter,
                             QRadioButton, QVBoxLayout, QLineEdit, QCheckBox, QDoubleSpinBox, QTabWidget,
                             QTableWidget, QTableWidgetItem, QSpinBox, QStyleFactory)
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QFont, QPalette, QColor
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class ScatterCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(ScatterCanvas, self).__init__(fig)

class SDAnalysisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SD Event Analysis App')
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Setup for the left panel (event categories and classifications)
        self.setup_left_panel()

        # Setup for the right panel (histograms, event plots, and event information)
        self.setup_right_panel()

        # Final layout setup
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.addWidget(self.main_splitter)

        self.data = None
        self.events_data = {}
        self.classification_to_event_ids = {} 
        self.selected_event_ids = set() 


    def setup_left_panel(self):
        self.top_group = QGroupBox()
        self.top_group_layout = QVBoxLayout(self.top_group)
        
        # Setup components of top_group
        self.configure_top_group()

        # Setup scroll areas for Event Categories and Classifications
        self.event_categories_group_box, self.event_categories_layout = self.setup_scroll_area("Event Categories")
        self.event_classification_group_box, self.event_classification_layout = self.setup_scroll_area("Event Classifications")

        # Adjustments to place the Select All button at the bottom
        self.select_all_button = QPushButton("Select All")
        self.select_all_button.clicked.connect(self.select_all_classifications)

        # Left Splitter Configuration
        self.left_splitter = QSplitter(Qt.Orientation.Vertical)
        self.left_splitter.addWidget(self.top_group)
        self.left_splitter.addWidget(self.event_categories_group_box)
        self.left_splitter.addWidget(self.event_classification_group_box)
        self.left_splitter.addWidget(self.select_all_button)  # Add the Select All button here
        self.left_splitter.setSizes([10, 300, 300, 50])  # Adjust sizes accordingly
        self.main_splitter.addWidget(self.left_splitter)

    def configure_top_group(self):
        self.title_label = QLabel('SD Event Analysis App')
        self.title_label.setFont(QFont('Arial', 23, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label = QLabel('shankar.dutt@anu.edu.au')
        self.subtitle_label.setFont(QFont('Arial', 15, QFont.Weight.Bold))
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top_group_layout.addWidget(self.title_label)
        self.top_group_layout.addWidget(self.subtitle_label)

        self.file_button = QPushButton('Select File')
        self.file_button.clicked.connect(self.load_file)
        self.top_group_layout.addWidget(self.file_button)

        # Container for Similarity Threshold Label and SpinBox
        self.threshold_container = QWidget()
        self.threshold_container_layout = QHBoxLayout(self.threshold_container)

        self.threshold_label = QLabel("Similarity Threshold: ")
        self.threshold_container_layout.addWidget(self.threshold_label)
        
        self.threshold_input = QDoubleSpinBox()
        self.threshold_input.setSuffix(" %")
        self.threshold_input.setRange(0, 100)
        self.threshold_input.setValue(85)
        self.threshold_input.setSingleStep(1)
        
        # Setup QTimer
        self.threshold_timer = QTimer(self)  # Create a QTimer instance
        self.threshold_timer.setSingleShot(True)  # Set the timer to single-shot mode
        self.threshold_timer.timeout.connect(self.on_threshold_changed)  # Connect the timer's timeout signal to on_threshold_changed
        self.threshold_input.valueChanged.connect(self.start_threshold_timer)  # Connect valueChanged signal to a method that starts the timer
        
        self.threshold_container_layout.addWidget(self.threshold_input)

        self.reclassify_checkbox = QCheckBox("Reclassify the event categories based on threshold")
        self.reclassify_checkbox.stateChanged.connect(self.on_threshold_changed)
        self.top_group_layout.addWidget(self.threshold_container)
        self.top_group_layout.addWidget(self.reclassify_checkbox)

    def start_threshold_timer(self):
        self.threshold_timer.start(500)  # Start/restart the timer with a 500ms delay

    def setup_right_panel(self):
        self.right_panel = QWidget()
        self.right_splitter = QSplitter(Qt.Orientation.Vertical)

        # Create tabs for histograms and scatter plots
        self.tabs = QTabWidget()
        self.histograms_tab = QWidget()
        self.scatter_plots_tab = QWidget()
        self.tabs.addTab(self.histograms_tab, "Histograms")
        self.tabs.addTab(self.scatter_plots_tab, "Scatter Plots")

        # Setup histograms tab
        self.setup_histograms_tab()

        # Setup scatter plots tab
        self.setup_scatter_plots_tab()

        self.right_splitter.addWidget(self.tabs)

        # Histograms group setup
        self.histograms_group = QGroupBox("Histograms")
        self.histograms_horizontal_layout = QHBoxLayout(self.histograms_group)
        
        # Create and setup the first histogram canvas and toolbar for all events
        # self.all_events_layout = QVBoxLayout()
        # self.all_events_histogram_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        # self.all_events_layout.addWidget(self.all_events_histogram_canvas)
        # self.all_events_histogram_toolbar = NavigationToolbar2QT(self.all_events_histogram_canvas, self.histograms_group)
        # self.all_events_histogram_toolbar.setIconSize(QSize(16, 16))
        # self.all_events_layout.addWidget(self.all_events_histogram_toolbar)
        # self.histograms_horizontal_layout.addLayout(self.all_events_layout)
        
        # # Create and setup the second histogram canvas and toolbar for selected classifications
        # self.selected_classifications_layout = QVBoxLayout()
        # self.selected_classifications_histogram_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        # self.selected_classifications_layout.addWidget(self.selected_classifications_histogram_canvas)
        # self.selected_classifications_histogram_toolbar = NavigationToolbar2QT(self.selected_classifications_histogram_canvas, self.histograms_group)
        # self.selected_classifications_histogram_toolbar.setIconSize(QSize(16, 16))
        # self.selected_classifications_layout.addWidget(self.selected_classifications_histogram_toolbar)
        # self.histograms_horizontal_layout.addLayout(self.selected_classifications_layout)
        
        # self.right_splitter.addWidget(self.histograms_group)

        # Adjusted setup for event plots and event information to be side by side
        self.bottom_right_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Event plots group setup
        self.event_plots_group = QGroupBox("Event Plots")
        self.event_plots_layout = QVBoxLayout(self.event_plots_group)
        self.event_plot_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.event_plots_layout.addWidget(self.event_plot_canvas)
        self.event_plot_toolbar = NavigationToolbar2QT(self.event_plot_canvas, self.event_plots_group)
        self.event_plot_toolbar.setIconSize(QSize(16, 16))
        self.event_plots_layout.addWidget(self.event_plot_toolbar)

        # Navigation controls under the event plots
        self.event_navigation_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.event_navigation_layout.addWidget(self.prev_button)
        # self.jump_to_label = QLabel("Jump to:")
        # self.event_navigation_layout.addWidget(self.jump_to_label)
        # self.jump_spinbox = QSpinBox()
        # self.jump_spinbox.setMinimum(1)  # Adjust as needed
        # self.jump_spinbox.setMaximum(100)  # Adjust based on your events count
        # self.event_navigation_layout.addWidget(self.jump_spinbox)
        # self.jump_button = QPushButton("Jump")
        # self.event_navigation_layout.addWidget(self.jump_button)
        self.next_button = QPushButton("Next")
        self.event_navigation_layout.addWidget(self.next_button)
        self.event_plots_layout.addLayout(self.event_navigation_layout)
        self.next_button.clicked.connect(self.next_event)  # Connect to the method handling the next event action
        self.prev_button.clicked.connect(self.previous_event)  # Connect to the method handling the previous event action


        self.bottom_right_splitter.addWidget(self.event_plots_group)

        # Event information group setup
        self.table_group = QGroupBox("Event Information")
        self.table_layout = QVBoxLayout(self.table_group)
        self.event_info_table = QTableWidget(10, 3)  # Adjust row, column count as needed
        self.event_info_table.setHorizontalHeaderLabels(['Type', 'Value', 'Description'])
        self.table_layout.addWidget(self.event_info_table)
        self.bottom_right_splitter.addWidget(self.table_group)

        self.right_splitter.addWidget(self.bottom_right_splitter)
        self.main_splitter.addWidget(self.right_splitter)

        # Setting initial sizes for splitters
        self.main_splitter.setSizes([300, 800])  # Adjust as needed
        self.right_splitter.setSizes([400, 350])  # Adjust as needed
        self.bottom_right_splitter.setSizes([400, 400])  # Adjust as needed

    def setup_histograms_tab(self):
        self.histograms_layout = QVBoxLayout(self.histograms_tab)
        self.histograms_group = QGroupBox("Histograms")
        self.histograms_horizontal_layout = QHBoxLayout(self.histograms_group)
        
        # Create and setup the first histogram canvas and toolbar for all events
        self.all_events_layout = QVBoxLayout()
        self.all_events_histogram_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.all_events_layout.addWidget(self.all_events_histogram_canvas)
        self.all_events_histogram_toolbar = NavigationToolbar2QT(self.all_events_histogram_canvas, self.histograms_group)
        self.all_events_histogram_toolbar.setIconSize(QSize(16, 16))
        self.all_events_layout.addWidget(self.all_events_histogram_toolbar)
        self.histograms_horizontal_layout.addLayout(self.all_events_layout)
        
        # Create and setup the second histogram canvas and toolbar for selected classifications
        self.selected_classifications_layout = QVBoxLayout()
        self.selected_classifications_histogram_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.selected_classifications_layout.addWidget(self.selected_classifications_histogram_canvas)
        self.selected_classifications_histogram_toolbar = NavigationToolbar2QT(self.selected_classifications_histogram_canvas, self.histograms_group)
        self.selected_classifications_histogram_toolbar.setIconSize(QSize(16, 16))
        self.selected_classifications_layout.addWidget(self.selected_classifications_histogram_toolbar)
        self.histograms_horizontal_layout.addLayout(self.selected_classifications_layout)
        
        self.histograms_layout.addWidget(self.histograms_group)

    def setup_scatter_plots_tab(self):
        self.scatter_plots_layout = QVBoxLayout(self.scatter_plots_tab)
        self.scatter_plots_group = QGroupBox("Scatter Plots")
        self.scatter_plots_horizontal_layout = QHBoxLayout(self.scatter_plots_group)

        # Create and setup the first scatter plot canvas and toolbar for all events
        self.all_events_scatter_layout = QVBoxLayout()
        self.all_events_scatter_canvas = ScatterCanvas(self, width=5, height=3)
        self.all_events_scatter_layout.addWidget(self.all_events_scatter_canvas)
        self.all_events_scatter_toolbar = NavigationToolbar2QT(self.all_events_scatter_canvas, self.scatter_plots_group)
        self.all_events_scatter_toolbar.setIconSize(QSize(16, 16))
        self.all_events_scatter_layout.addWidget(self.all_events_scatter_toolbar)
        self.scatter_plots_horizontal_layout.addLayout(self.all_events_scatter_layout)

        # Create and setup the second scatter plot canvas and toolbar for selected classifications
        self.selected_classifications_scatter_layout = QVBoxLayout()
        self.selected_classifications_scatter_canvas = ScatterCanvas(self, width=5, height=3)
        self.selected_classifications_scatter_layout.addWidget(self.selected_classifications_scatter_canvas)
        self.selected_classifications_scatter_toolbar = NavigationToolbar2QT(self.selected_classifications_scatter_canvas, self.scatter_plots_group)
        self.selected_classifications_scatter_toolbar.setIconSize(QSize(16, 16))
        self.selected_classifications_scatter_layout.addWidget(self.selected_classifications_scatter_toolbar)
        self.scatter_plots_horizontal_layout.addLayout(self.selected_classifications_scatter_layout)

        self.scatter_plots_layout.addWidget(self.scatter_plots_group)


    def setup_scroll_area(self, title):
        scroll_area = QScrollArea()  # Create the scroll area
        scroll_area.setWidgetResizable(True)
        
        container_widget = QWidget()  
        layout = QVBoxLayout(container_widget) 
        
        scroll_area.setWidget(container_widget) 

        group_box = QGroupBox(title)
        group_layout = QVBoxLayout(group_box)  
        group_layout.addWidget(scroll_area) 

        return group_box, layout 

    def on_threshold_changed(self):
        #current_value = self.threshold_input.value()
        self.prepare_and_display_event_data()  

    
    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open NPZ File', '', 'NPZ Files (*event_fitting.npz)')
        if file_name:
            self.data = np.load(file_name, allow_pickle=True)  # Directly load and store data
            self.prepare_and_display_event_data()

    def prepare_and_display_event_data(self):
        if self.data is not None:
            self.events_data.clear()  # Ensure we're starting fresh
            self.clear_layout(self.event_categories_layout)
            self.clear_layout(self.event_classification_layout)
            self.plot_all_events_histogram()

            # Process and categorize events
            for key in self.data.files:
                if 'SEGMENT_INFO' in key and 'number_of_segments' in key:
                    event_id = int(key.split('_')[2])
                    # Extract mean_diffs to determine if reclassification changes segment count
                    mean_diffs_key = f'SEGMENT_INFO_{event_id}_segment_mean_diffs'
                    segment_widths_key = f'SEGMENT_INFO_{event_id}_segment_widths_time'
                    if mean_diffs_key in self.data and segment_widths_key in self.data:
                        mean_diffs = self.data[mean_diffs_key]
                        segment_widths = self.data[segment_widths_key]
                        _, new_segment_count = self.classify_event(mean_diffs)  # Use new segment count
                        self.events_data.setdefault(new_segment_count, []).append((event_id, mean_diffs, segment_widths))
                    else:
                        new_segment_count = int(self.data[key][0])
                        self.events_data.setdefault(new_segment_count, []).append((event_id, [], []))
            
            for num_segments in sorted(self.events_data):
                events_data = self.events_data[num_segments]
                event_ids = [event_data[0] for event_data in events_data]
                radio_button = QRadioButton(f"{num_segments} segments ({len(event_ids)} events)")
                radio_button.segment_number = num_segments
                radio_button.toggled.connect(self.on_radio_button_toggled)
                self.event_categories_layout.addWidget(radio_button)
            
            

    def on_radio_button_toggled(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.update_classification_group(radio_button.segment_number)

    def update_classification_group(self, segment_number):
        self.clear_layout(self.event_classification_layout)
        classification_counts = {}
        self.classification_checkboxes = []
        self.classification_to_event_ids.clear()  # Reset the mapping

        for event_data in self.events_data.get(segment_number, []):
            event_id = event_data[0]
            mean_diffs_key = f'SEGMENT_INFO_{event_id}_segment_mean_diffs'
            if mean_diffs_key in self.data:
                mean_diffs = self.data[mean_diffs_key]
                classification, _ = self.classify_event(mean_diffs)
                classification_counts[classification] = classification_counts.get(classification, 0) + 1
                # Store event IDs under each classification
                if classification not in self.classification_to_event_ids:
                    self.classification_to_event_ids[classification] = []
                self.classification_to_event_ids[classification].append(event_id)

        for classification, count in sorted(classification_counts.items(), key=lambda x: x[0]):
            checkbox = QCheckBox(f"Category {classification} ({count} events)")
            # Now each checkbox represents a whole category/classification of events
            checkbox.classification = classification  # Use classification to identify the group
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)
            self.event_classification_layout.addWidget(checkbox)
            self.classification_checkboxes.append(checkbox)

        # Ensure the "Select All" button works with the newly added checkboxes
        self.select_all_button.clicked.disconnect()  # First, disconnect any existing connection
        self.select_all_button.clicked.connect(self.select_all_classifications)  # Reconnect with the updated list of checkboxes



    def classify_event(self, mean_diffs):
        threshold_ratio = self.threshold_input.value() / 100.0

        # Initial classification
        if len(mean_diffs) <= 1:
            return "1", 1  # Single segment events are automatically classified as "1"

        # Initial classifications: each segment starts as unique
        classifications = ["1"]
        
        for i in range(1, len(mean_diffs)):
            found_similar = False
            for j in range(i):
                # Calculate the ratio to compare the mean differences
                ratio = mean_diffs[i] / mean_diffs[j] if mean_diffs[i] > mean_diffs[j] else mean_diffs[j] / mean_diffs[i]
                
                # If the ratio is within the similarity threshold
                if ratio <= (1 / threshold_ratio):
                    classifications.append(classifications[j])  # Assign the same classification as the similar segment
                    found_similar = True
                    break
            
            if not found_similar:
                # Assign a new unique classification
                max_classification = max([int(c) for c in classifications])
                classifications.append(str(max_classification + 1))

        # Check if reclassification based on threshold is checked
        if self.reclassify_checkbox.isChecked() and len(classifications) > 1:
            # Perform reclassification
            new_classifications = [classifications[0]]
            for i in range(1, len(classifications)):
                # Merge adjacent similar classifications
                if classifications[i] == classifications[i - 1]:
                    continue  # Skip adding it to new classifications
                new_classifications.append(classifications[i])
            classifications = new_classifications

        # Calculate new segment count based on reclassification
        new_segment_count = len(classifications)

        # Return both the classification string and the new segment count
        return ''.join(classifications), new_segment_count


    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def select_all_classifications(self):
        try:
            if any(not checkbox.isChecked() for checkbox in self.classification_checkboxes):
                for checkbox in self.classification_checkboxes:
                    checkbox.setChecked(True)
            else:
                for checkbox in self.classification_checkboxes:
                    checkbox.setChecked(False)

            # Update the button text based on the new state
            self.select_all_button.setText("Unselect All" if any(checkbox.isChecked() for checkbox in self.classification_checkboxes) else "Select All")
        except:
            pass


    def plot_all_events_histogram(self):
        max_mean_diffs = []
        for key in self.data.files:
            if 'segment_mean_diffs' in key:
                mean_diffs = self.data[key]
                max_mean_diffs.append(np.max(mean_diffs))
        
        # Clear the figure/canvas before plotting
        self.all_events_histogram_canvas.figure.clear()

        ax = self.all_events_histogram_canvas.figure.subplots()
        
        # Calculate bin edges with 'auto' and then double the number of bins
        _, bins_auto = np.histogram(max_mean_diffs, bins='auto')
        num_bins_auto = len(bins_auto) - 1  # Number of bins is one less than the number of edges
        doubled_num_bins = num_bins_auto * 2  # Double the number of bins
        
        # Use linspace to create new bin edges with doubled number of bins
        new_bins = np.linspace(bins_auto[0], bins_auto[-1], doubled_num_bins + 1)
        
        ax.hist(max_mean_diffs, bins=new_bins)
        ax.set_title('Max Segment Mean Diffs for All Events')
        ax.set_xlabel('Max Mean Diff')
        ax.set_ylabel('Frequency')
        self.all_events_histogram_canvas.figure.tight_layout()
        self.all_events_histogram_canvas.draw()
        # Plot the corresponding scatter plot
        self.plot_all_events_scatter()

    def on_checkbox_state_changed(self):
        self.selected_event_ids.clear()  # Clear and repopulate based on current selections

        for checkbox in self.classification_checkboxes:
            if checkbox.isChecked():
                # Add all event IDs from this classification to the selected set
                event_ids = self.classification_to_event_ids.get(checkbox.classification, [])
                self.selected_event_ids.update(event_ids)
        
        # Plot and display segment info for the first selected event, if any
        self.current_event_index = 0
        if self.selected_event_ids:
            first_event_id = next(iter(sorted(self.selected_event_ids)))
            self.plot_event_data(first_event_id)
            self.display_segment_info(first_event_id)

        # Optionally update plots/information here
        self.plot_selected_events_histogram()
    
    def setup_navigation_buttons(self):
        self.current_event_index = 0  # Initialize the current index
        self.previous_button.clicked.connect(self.previous_event)
        self.next_button.clicked.connect(self.next_event)

    def previous_event(self):
        if self.selected_event_ids and self.current_event_index > 0:
            self.current_event_index -= 1
            event_id = sorted(self.selected_event_ids)[self.current_event_index]
            self.plot_event_data(event_id)
            self.display_segment_info(event_id)

    def next_event(self):
        if self.selected_event_ids and self.current_event_index < len(self.selected_event_ids) - 1:
            self.current_event_index += 1
            event_id = sorted(self.selected_event_ids)[self.current_event_index]
            self.plot_event_data(event_id)
            self.display_segment_info(event_id)

    def plot_selected_events_histogram(self):
        all_mean_diffs = []
        for event_id in self.selected_event_ids:
            key = f'SEGMENT_INFO_{event_id}_segment_mean_diffs'
            if key in self.data:
                mean_diffs = self.data[key]
                all_mean_diffs.extend(mean_diffs)              
        
        if len(all_mean_diffs)>1:
            # Clear the figure/canvas before plotting
            self.selected_classifications_histogram_canvas.figure.clear()

            ax = self.selected_classifications_histogram_canvas.figure.subplots()
            
            # Decide on the number of bins
            num_bins = 'auto'  # Default
            
            # Plot the histogram with bar boundaries
            ax.hist(all_mean_diffs, bins=num_bins, edgecolor='black')

            ax.set_title('Segment Mean Diffs for Selected Events')
            ax.set_xlabel('Mean Diff')
            ax.set_ylabel('Frequency')
            self.selected_classifications_histogram_canvas.figure.tight_layout()
            self.selected_classifications_histogram_canvas.draw()
        
        # Plot the corresponding scatter plot
        self.plot_selected_events_scatter()

    def plot_all_events_scatter(self):
        max_mean_diffs = []
        event_widths = []
        for key in self.data.files:
            if 'segment_mean_diffs' in key:
                mean_diffs = self.data[key]
                max_mean_diffs.append(np.max(mean_diffs))

            if 'event_width' in key:
                event_widths.append(self.data[key])

        if len(max_mean_diffs) > 0 and len(event_widths) > 0:
            # Clear the figure/canvas before plotting
            self.all_events_scatter_canvas.figure.clear()

            ax = self.all_events_scatter_canvas.figure.subplots()
            ax.scatter(np.log(np.array(event_widths)*1e3), max_mean_diffs)
            ax.set_title('Max Segment Mean Diffs vs log(Event Width) for All Events')
            ax.set_xlabel('log(Δt (ms))')
            ax.set_ylabel('ΔI')
            self.all_events_scatter_canvas.figure.tight_layout()
            self.all_events_scatter_canvas.draw()


    def plot_selected_events_scatter(self):
        all_mean_diffs = []
        all_segment_widths = []
        for event_id in self.selected_event_ids:
            for segment_count, events in self.events_data.items():
                for event_data in events:
                    if event_data[0] == event_id:
                        _, mean_diffs, segment_widths = event_data
                        all_mean_diffs.extend(mean_diffs)
                        all_segment_widths.extend(segment_widths)
                        break

        if len(all_mean_diffs) > 0 and len(all_segment_widths) > 0:
            # Clear the figure/canvas before plotting
            self.selected_classifications_scatter_canvas.figure.clear()

            ax = self.selected_classifications_scatter_canvas.figure.subplots()
            ax.scatter(np.log(np.array(all_segment_widths)*1e3), all_mean_diffs)
            ax.set_title('Segment Mean Diffs vs log(dt (ms)) for Selected Events')
            ax.set_xlabel('log(Δt (ms))')
            ax.set_ylabel('Mean Diff')
            self.selected_classifications_scatter_canvas.figure.tight_layout()
            self.selected_classifications_scatter_canvas.draw()

    def plot_event_data(self, event_id):
        # Retrieve event data
        x_values = self.data[f'EVENT_DATA_{event_id}_part_0']
        y_values_event = self.data[f'EVENT_DATA_{event_id}_part_1']
        y_values_fit = self.data[f'EVENT_DATA_{event_id}_part_3']
        
        # Clear the plot
        self.event_plot_canvas.figure.clear()
        
        # Create a new plot
        ax = self.event_plot_canvas.figure.subplots()
        ax.plot(x_values, y_values_event, label='Event Data')
        ax.plot(x_values, y_values_fit, label='Fit Data', linestyle='--')
        
        # Adding legends, title, and labels
        ax.legend()
        ax.set_title(f'Event {event_id} Data')
        ax.set_xlabel('Time')
        ax.set_ylabel('Data')
        
        self.event_plot_canvas.figure.tight_layout()
        # Refresh the canvas
        self.event_plot_canvas.draw()

    

    def display_segment_info(self, event_id):
        segment_info_keys = [
            f'SEGMENT_INFO_{event_id}_number_of_segments',
            f'SEGMENT_INFO_{event_id}_segment_mean_diffs',
            f'SEGMENT_INFO_{event_id}_segment_widths_time'
        ]
        
        # Extract segment info
        number_of_segments = self.data[segment_info_keys[0]][0]
        segment_mean_diffs = self.data[segment_info_keys[1]]
        segment_widths_time = self.data[segment_info_keys[2]]
        
        # Configure table for display
        self.event_info_table.setRowCount(int(number_of_segments))
        self.event_info_table.setColumnCount(3)
        self.event_info_table.setHorizontalHeaderLabels(['Segment', 'Mean Diff', 'Width Time'])
        
        # Populate the table and round the data
        for i in range(int(number_of_segments)):
            self.event_info_table.setItem(i, 0, QTableWidgetItem(f"{i + 1}"))
            self.event_info_table.setItem(i, 1, QTableWidgetItem(f"{segment_mean_diffs[i]:.3g}"))  # Rounded to 3 significant figures
            self.event_info_table.setItem(i, 2, QTableWidgetItem(f"{segment_widths_time[i]:.3g}"))  # Rounded to 3 significant figures

        # Adjust column widths to fit the content
        self.event_info_table.resizeColumnsToContents()

        # Optionally, you can also adjust the row heights if needed
        self.event_info_table.resizeRowsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))  #
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(palette)
    mainWin = SDAnalysisApp()
    mainWin.showMaximized()
    sys.exit(app.exec())
