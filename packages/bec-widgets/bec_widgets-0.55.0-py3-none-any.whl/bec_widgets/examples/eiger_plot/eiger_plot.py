import json
import os
import threading

import h5py
import numpy as np
import pyqtgraph as pg
import zmq
from pyqtgraph.Qt import uic
from qtpy.QtCore import Signal as pyqtSignal
from qtpy.QtCore import Slot as pyqtSlot
from qtpy.QtGui import QKeySequence
from qtpy.QtWidgets import QDialog, QFileDialog, QFrame, QLabel, QShortcut, QVBoxLayout, QWidget

# from scipy.stats import multivariate_normal


class EigerPlot(QWidget):
    update_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # pg.setConfigOptions(background="w", foreground="k", antialias=True)

        current_path = os.path.dirname(__file__)
        uic.loadUi(os.path.join(current_path, "eiger_plot.ui"), self)

        # Set widow name
        self.setWindowTitle("Eiger Plot")

        self.hist_lims = None
        self.mask = None
        self.image = None

        # UI
        self.init_ui()
        self.hook_signals()
        self.key_bindings()

        # ZMQ Consumer
        self._zmq_consumer_exit_event = threading.Event()
        self._zmq_consumer_thread = self.start_zmq_consumer()

    def close(self):
        super().close()
        self._zmq_consumer_exit_event.set()
        self._zmq_consumer_thread.join()

    def init_ui(self):
        # Create Plot and add ImageItem
        self.plot_item = pg.PlotItem()
        self.plot_item.setAspectLocked(True)
        self.imageItem = pg.ImageItem()
        self.plot_item.addItem(self.imageItem)

        # Setting up histogram
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.imageItem)
        self.hist.gradient.loadPreset("magma")
        self.update_hist()

        # Adding Items to Graphical Layout
        self.glw.addItem(self.plot_item)
        self.glw.addItem(self.hist)

    def hook_signals(self):
        # Buttons
        # self.pushButton_test.clicked.connect(self.start_sim_stream)
        self.pushButton_mask.clicked.connect(self.load_mask_dialog)
        self.pushButton_delete_mask.clicked.connect(self.delete_mask)
        self.pushButton_help.clicked.connect(self.show_help_dialog)

        # SpinBoxes
        self.doubleSpinBox_hist_min.valueChanged.connect(self.update_hist)
        self.doubleSpinBox_hist_max.valueChanged.connect(self.update_hist)

        # Signal/Slots
        self.update_signal.connect(self.on_image_update)

    def key_bindings(self):
        # Key bindings for rotation
        rotate_plus = QShortcut(QKeySequence("Ctrl+A"), self)
        rotate_minus = QShortcut(QKeySequence("Ctrl+Z"), self)
        self.comboBox_rotation.setToolTip("Increase rotation: Ctrl+A\nDecrease rotation: Ctrl+Z")
        self.checkBox_transpose.setToolTip("Toggle transpose: Ctrl+T")

        max_index = self.comboBox_rotation.count() - 1  # Maximum valid index

        rotate_plus.activated.connect(
            lambda: self.comboBox_rotation.setCurrentIndex(
                min(self.comboBox_rotation.currentIndex() + 1, max_index)
            )
        )

        rotate_minus.activated.connect(
            lambda: self.comboBox_rotation.setCurrentIndex(
                max(self.comboBox_rotation.currentIndex() - 1, 0)
            )
        )

        # Key bindings for transpose
        transpose = QShortcut(QKeySequence("Ctrl+T"), self)
        transpose.activated.connect(self.checkBox_transpose.toggle)

        FFT = QShortcut(QKeySequence("Ctrl+F"), self)
        FFT.activated.connect(self.checkBox_FFT.toggle)
        self.checkBox_FFT.setToolTip("Toggle FFT: Ctrl+F")

        log = QShortcut(QKeySequence("Ctrl+L"), self)
        log.activated.connect(self.checkBox_log.toggle)
        self.checkBox_log.setToolTip("Toggle log: Ctrl+L")

        mask = QShortcut(QKeySequence("Ctrl+M"), self)
        mask.activated.connect(self.pushButton_mask.click)
        self.pushButton_mask.setToolTip("Load mask: Ctrl+M")

        delete_mask = QShortcut(QKeySequence("Ctrl+D"), self)
        delete_mask.activated.connect(self.pushButton_delete_mask.click)
        self.pushButton_delete_mask.setToolTip("Delete mask: Ctrl+D")

    def update_hist(self):
        self.hist_levels = [
            self.doubleSpinBox_hist_min.value(),
            self.doubleSpinBox_hist_max.value(),
        ]
        self.hist.setLevels(min=self.hist_levels[0], max=self.hist_levels[1])
        self.hist.setHistogramRange(
            self.hist_levels[0] - 0.1 * self.hist_levels[0],
            self.hist_levels[1] + 0.1 * self.hist_levels[1],
        )

    def load_mask_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Mask File", "", "H5 Files (*.h5);;All Files (*)", options=options
        )
        if file_name:
            self.load_mask(file_name)

    def load_mask(self, path):
        try:
            with h5py.File(path, "r") as f:
                self.mask = f["data"][...]
            if self.mask is not None:
                # Set label to mask name without path
                self.label_mask.setText(os.path.basename(path))
        except KeyError as e:
            # Update GUI with the error message
            print(f"Error: {str(e)}")

    def delete_mask(self):
        self.mask = None
        self.label_mask.setText("No Mask")

    @pyqtSlot()
    def on_image_update(self):
        # TODO first rotate then transpose
        if self.mask is not None:
            # self.image = np.ma.masked_array(self.image, mask=self.mask) #TODO test if np works
            self.image = self.image * (1 - self.mask) + 1

        if self.checkBox_FFT.isChecked():
            self.image = np.abs(np.fft.fftshift(np.fft.fft2(self.image)))

        if self.comboBox_rotation.currentIndex() > 0:  # rotate
            self.image = np.rot90(self.image, k=self.comboBox_rotation.currentIndex(), axes=(0, 1))

        if self.checkBox_transpose.isChecked():  # transpose
            self.image = np.transpose(self.image)

        if self.checkBox_log.isChecked():
            self.image = np.log10(self.image)

        self.imageItem.setImage(self.image, autoLevels=False)

    ###############################
    # ZMQ Consumer
    ###############################

    def start_zmq_consumer(self):
        consumer_thread = threading.Thread(
            target=self.zmq_consumer, args=(self._zmq_consumer_exit_event,), daemon=True
        )
        consumer_thread.start()
        return consumer_thread

    def zmq_consumer(self, exit_event):
        print("starting consumer")
        live_stream_url = "tcp://129.129.95.38:20000"
        receiver = zmq.Context().socket(zmq.SUB)
        receiver.connect(live_stream_url)
        receiver.setsockopt_string(zmq.SUBSCRIBE, "")

        poller = zmq.Poller()
        poller.register(receiver, zmq.POLLIN)

        # code could be a bit simpler here, testing exit_event in
        # 'while' condition, but like this it is easier for the
        # 'test_zmq_consumer' test
        while True:
            if poller.poll(1000):  # 1s timeout
                raw_meta, raw_data = receiver.recv_multipart(zmq.NOBLOCK)

                meta = json.loads(raw_meta.decode("utf-8"))
                self.image = np.frombuffer(raw_data, dtype=meta["type"]).reshape(meta["shape"])
                self.update_signal.emit()
            if exit_event.is_set():
                break

        receiver.disconnect(live_stream_url)

    ###############################
    # just simulations from here
    ###############################

    def show_help_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Help")

        layout = QVBoxLayout()

        # Key bindings section
        layout.addWidget(QLabel("Keyboard Shortcuts:"))

        key_bindings = [
            ("Ctrl+A", "Increase rotation"),
            ("Ctrl+Z", "Decrease rotation"),
            ("Ctrl+T", "Toggle transpose"),
            ("Ctrl+F", "Toggle FFT"),
            ("Ctrl+L", "Toggle log scale"),
            ("Ctrl+M", "Load mask"),
            ("Ctrl+D", "Delete mask"),
        ]

        for keys, action in key_bindings:
            layout.addWidget(QLabel(f"{keys} - {action}"))

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Histogram section
        layout.addWidget(QLabel("Histogram:"))
        layout.addWidget(
            QLabel(
                "Use the Double Spin Boxes to adjust the minimum and maximum values of the histogram."
            )
        )

        # Another Separator
        another_separator = QFrame()
        another_separator.setFrameShape(QFrame.HLine)
        another_separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(another_separator)

        # Mask section
        layout.addWidget(QLabel("Mask:"))
        layout.addWidget(
            QLabel(
                "Use 'Load Mask' to load a mask from an H5 file. 'Delete Mask' removes the current mask."
            )
        )

        dialog.setLayout(layout)
        dialog.exec()

    ###############################
    # just simulations from here
    ###############################
    # def start_sim_stream(self):
    #     sim_stream_thread = threading.Thread(target=self.sim_stream, daemon=True)
    #     sim_stream_thread.start()
    #
    # def sim_stream(self):
    #     for i in range(100):
    #         # Generate 100x100 image of random noise
    #         self.image = np.random.rand(100, 100) * 0.2
    #
    #         # Define Gaussian parameters
    #         x, y = np.mgrid[0:50, 0:50]
    #         pos = np.dstack((x, y))
    #
    #         # Center at (25, 25) longer along y-axis
    #         rv = multivariate_normal(mean=[25, 25], cov=[[25, 0], [0, 80]])
    #
    #         # Generate Gaussian in the first quadrant
    #         gaussian_quadrant = rv.pdf(pos) * 40
    #
    #         # Place Gaussian in the first quadrant
    #         self.image[0:50, 0:50] += gaussian_quadrant * 10
    #
    #         self.update_signal.emit()
    #         time.sleep(0.1)


if __name__ == "__main__":
    import sys

    from qtpy.QtWidgets import QApplication

    app = QApplication(sys.argv)
    plot = EigerPlot()
    plot.show()
    sys.exit(app.exec())
