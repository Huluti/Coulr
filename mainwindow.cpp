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
    changeColorByRGB();

    // Signals

    connect(ui->red, SIGNAL(valueChanged(int)), this, SLOT(changeColorByRGB()));
    connect(ui->green, SIGNAL(valueChanged(int)), this, SLOT(changeColorByRGB()));
    connect(ui->blue, SIGNAL(valueChanged(int)), this, SLOT(changeColorByRGB()));

    connect(ui->hue, SIGNAL(valueChanged(int)), this, SLOT(changeColorByHSL()));
    connect(ui->saturation, SIGNAL(valueChanged(int)), this, SLOT(changeColorByHSL()));
    connect(ui->lightness, SIGNAL(valueChanged(int)), this, SLOT(changeColorByHSL()));

    connect(ui->actionAbout, SIGNAL(triggered()), this, SLOT(about()));
}

void MainWindow::changeColorByRGB()
{
    if(ui->tabWidget->currentIndex() == 0)
    {
        applyColor(ui->red->value(), ui->green->value(), ui->blue->value(), 0);
    }
}

void MainWindow::changeColorByHSL()
{
    if(ui->tabWidget->currentIndex() == 1)
    {
        applyColor(ui->hue->value(), ui->saturation->value(), ui->lightness->value(), 1);
    }
}

//  Get HTML color and change widget background
void MainWindow::applyColor(int param1, int param2, int param3, int t)
{
    /* t:
    * 0: RGB
    * 1: HSL
    */

    QColor color;
    QColor rgb;
    QColor hsl;

    switch (t) {
        case 0:
            color = QColor(param1, param2, param3);
            hsl = color.convertTo(QColor::Hsl);
            ui->hue->setValue(hsl.hslHue());
            ui->saturation->setValue(hsl.saturation());
            ui->lightness->setValue(hsl.lightness());
            break;
        case 1:
            color = QColor::fromHsl(param1, param2, param3);
            rgb = color.convertTo(QColor::Rgb);
            ui->red->setValue(rgb.red());
            ui->green->setValue(rgb.green());
            ui->blue->setValue(rgb.blue());
            break;
    }

    QString html_color = color.name();

    ui->color_widget->setStyleSheet("background: " + html_color + ";");
    ui->html_color->setText(html_color);
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
