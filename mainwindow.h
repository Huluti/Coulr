#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QSettings>
#include <QDesktopWidget>
#include <QSignalMapper>
#include <QMessageBox>
#include <QClipboard>
#include <QCloseEvent>

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
    void changeColor(QString method);
    void colorToClipboard();
    void about();

private:
    Ui::MainWindow *ui;
    QSignalMapper *signalMapper;
    QClipboard *cb;
    QString version;
    QString html_color;

protected:
    void closeEvent(QCloseEvent *event);

};

#endif // MAINWINDOW_H
