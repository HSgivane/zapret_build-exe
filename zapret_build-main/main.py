from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QSpacerItem, QSizePolicy, QSystemTrayIcon, QMenu
)
from PyQt6.QtGui import QIcon, QAction  
from PyQt6.QtCore import Qt
import sys
import os
import subprocess
import psutil
import time
from config import exe_path, args_gen, args_dis, args_service

#заменить перед сборкой
import ctypes

#заменить перед сборкой
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#заменить перед сборкой
if not is_admin():
    # Перезапуск от имени администратора
    script = os.path.abspath(sys.argv[0])
    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, f'"{script}" {params}', None, 1)
    sys.exit()


def get_winws_pid():
                try:
                    output = subprocess.check_output(
                        'tasklist | findstr winws.exe', shell=True, text=True
                    )

                    for line in output.strip().split('\n'):
                        if "winws.exe" in line.lower():
                            parts = line.split()
                            pid = int(parts[1])
                            print(f"[+] Найден winws.exe с PID: {pid}")
                            return pid

                except:
                    return '1'

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

def kill_by_pid():
            try:
                pid = get_winws_pid()
                proc = psutil.Process(pid)
                proc.kill()
                print(f"[+] Убил процесс")
            except:
                print(f"[!] Не удалось убить процесс")


class CustomWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("zapret-build givane.apk")
        self.setFixedSize(300, 340)
        self.setWindowIcon(QIcon(resource_path("icon.ico")))
        self.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #666;
            }
            QLabel {
                font-size: 14px;
            }
        """)

        layout = QVBoxLayout()

        # Кнопки
        self.general_btn = QPushButton("General")
        self.discord_btn = QPushButton("Discord")
        self.stop_btn = QPushButton("Остановить процесс")

        # Статус
        self.status_label = QLabel("Служба остановлена")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("color: red; font-weight: bold;")

        # Нижняя часть
        self.create_btn = QPushButton("Создать службу")
        self.note_label = QLabel("При первом запуске")
        self.note_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.note_label.setStyleSheet("color: red;")

        # Привязка
        self.general_btn.clicked.connect(self.on_general)
        self.discord_btn.clicked.connect(self.on_discord)
        self.stop_btn.clicked.connect(self.on_stop)
        self.create_btn.clicked.connect(self.on_create_service)

        layout.addWidget(self.general_btn)
        layout.addWidget(self.discord_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.status_label)
        layout.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addWidget(self.create_btn)
        layout.addWidget(self.note_label)
        self.setLayout(layout)

        # === ТРЕЙ ===
        self.tray_icon = QSystemTrayIcon(QIcon(resource_path("icon.ico")), self)

        tray_menu = QMenu()
        action_show = QAction("Открыть", self)
        action_quit = QAction("Выход", self)

        action_show.triggered.connect(self.show)
        action_quit.triggered.connect(self.on_quit)

        tray_menu.addAction(action_show)
        tray_menu.addAction(action_quit)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_activated)
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "Zapret", "Приложение свернуто в трей", QSystemTrayIcon.MessageIcon.Information, 3000
        )

    def on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show()

    def on_general(self):
        kill_by_pid()
        time.sleep(1)
        proc = subprocess.Popen(
            [exe_path] + args_gen,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        self.status_label.setText("Служба запущена")
        self.status_label.setStyleSheet("color: green; font-weight: bold;")

    def on_discord(self):
        kill_by_pid()
        time.sleep(1)
        proc = subprocess.Popen(
            [exe_path] + args_dis,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        self.status_label.setText("Только дискорд")
        self.status_label.setStyleSheet("color: green; font-weight: bold;")

    def on_stop(self):
        kill_by_pid()
        self.status_label.setText("Служба остановлена")
        self.status_label.setStyleSheet("color: red; font-weight: bold;")

    def on_create_service(self):
        proc = subprocess.Popen(
            [exe_path] + args_service,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        self.tray_icon.showMessage("Запрет", "Служба успешно создана ✅", QSystemTrayIcon.MessageIcon.Information, 2000)

    def on_quit(self):
        kill_by_pid()
        time.sleep(0.5)
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWindow()
    window.show()
    sys.exit(app.exec())
