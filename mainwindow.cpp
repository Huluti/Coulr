#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Setup color at lauch (#000)
    changeColor();

    // Signals
    connect(ui->red, SIGNAL(valueChanged(int)), this, SLOT(changeColor()));
    connect(ui->green, SIGNAL(valueChanged(int)), this, SLOT(changeColor()));
    connect(ui->blue, SIGNAL(valueChanged(int)), this, SLOT(changeColor()));
}

//  Get HTML color
QString MainWindow::generateColor(int r, int g, int b)
{
    QColor color = QColor(r, g, b);
    QString html_color = color.name();

    return html_color;
}

// Change widget background
void MainWindow::changeColor()
{
    QString color = generateColor(ui->red->value(), ui->green->value(), ui->blue->value());
    ui->color_widget->setStyleSheet("background: " + color + ";");
    ui->html_color->setText(color);
}

MainWindow::~MainWindow()
{
    delete ui;
}
