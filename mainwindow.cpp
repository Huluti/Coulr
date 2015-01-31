#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Move window at center
    QRect screenGeometry = QApplication::desktop()->screenGeometry();
    int x = (screenGeometry.width()-this->width()) / 2;
    int y = (screenGeometry.height()-this->height()) / 2;
    move(x, y);

    // Setup color at lauch (#000)
    changeColor();

    // Signals
    connect(ui->red, SIGNAL(valueChanged(int)), this, SLOT(changeColor()));
    connect(ui->green, SIGNAL(valueChanged(int)), this, SLOT(changeColor()));
    connect(ui->blue, SIGNAL(valueChanged(int)), this, SLOT(changeColor()));
    connect(ui->actionAbout, SIGNAL(triggered()), this, SLOT(about()));
}

//  Get HTML color
QString MainWindow::generateColor(int r, int g, int b)
{
    QColor color = QColor(r, g, b);

    return color.name();
}

// Change widget background
void MainWindow::changeColor()
{
    QString color = generateColor(ui->red->value(), ui->green->value(), ui->blue->value());
    ui->color_widget->setStyleSheet("background: " + color + ";");
    ui->html_color->setText(color);
}

// About Coulr
void MainWindow::about()
{
    QMessageBox::information(this, tr("About"), tr("Coulr is a free color box software designed by <a href=\"https://github.com/Huluti\">Hugo Posnic</a> using Qt 5. Software under <a href=\"https://github.com/Huluti/Coulr/blob/master/LICENSE\">MIT Licence</a>."));
}

MainWindow::~MainWindow()
{
    delete ui;
}
