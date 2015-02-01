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
    void applyColor(int param1, int param2, int param3, int t);
    void fillValues(bool rgb, bool hsl, bool hsv, QColor color);
    void palette();
    ~MainWindow();

public slots:
    void changeColorByRGB();
    void changeColorByHSL();
    void changeColorByHSV();
    void about();

private:
    Ui::MainWindow *ui;
    QString html_color;
};

#endif // MAINWINDOW_H
