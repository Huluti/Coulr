#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QDesktopWidget>
#include <QMessageBox>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    QString generateColor(int r, int g, int b);
    ~MainWindow();

public slots:
    void changeColor();
    void about();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
