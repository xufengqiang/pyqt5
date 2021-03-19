import sys
import formlayout
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建主窗口
    main_window = QMainWindow()
    ui = formlayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
    pass

