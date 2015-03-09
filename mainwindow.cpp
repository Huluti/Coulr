#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow) {
    ui->setupUi(this);

    // Define version number
    version = "0.6";

    // Move window at center
    QRect screenGeometry = QApplication::desktop()->screenGeometry();
    int x = (screenGeometry.width()-this->width()) / 2;
    int y = (screenGeometry.height()-this->height()) / 2;
    move(x, y);

    // Setup color at lauch
    QSettings settings("Coulr", "Coulr");
    if(!settings.value("last_color").toString().isEmpty()) {
        QColor launch_color = QColor();
        launch_color.setNamedColor(settings.value("last_color").toString());
        applyColor(launch_color.red(), launch_color.green(), launch_color.blue(), 0);
    }
    else {
        changeColor("RGB"); // #000
    }

    // Signals
    signalMapper = new QSignalMapper (this) ;

    // HEXA
    connect(ui->html_color, SIGNAL(returnPressed()), signalMapper, SLOT(map()));
    signalMapper->setMapping (ui->html_color, "HEXA");
    // RGB
    connect(ui->red, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    connect(ui->green, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    connect(ui->blue, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    signalMapper->setMapping (ui->red, "RGB");
    signalMapper->setMapping (ui->green, "RGB");
    signalMapper->setMapping (ui->blue, "RGB");
    // HSL
    connect(ui->hue, SIGNAL(valueChanged(int)), signalMapper, SLOT(map())) ;
    connect(ui->saturation, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    connect(ui->lightness, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    signalMapper->setMapping (ui->hue, "HSL");
    signalMapper->setMapping (ui->saturation, "HSL");
    signalMapper->setMapping (ui->lightness, "HSL");
    // HSV
    connect(ui->hue2, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    connect(ui->saturation2, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    connect(ui->value, SIGNAL(valueChanged(int)), signalMapper, SLOT(map()));
    signalMapper->setMapping (ui->hue2, "HSV");
    signalMapper->setMapping (ui->saturation2, "HSV");
    signalMapper->setMapping (ui->value, "HSV");

    connect(signalMapper, SIGNAL(mapped(QString)), this, SLOT(changeColor(QString)));
    connect(ui->copyColor, SIGNAL(clicked()), this, SLOT(colorToClipboard()));
    connect(ui->actionAbout, SIGNAL(triggered()), this, SLOT(about()));

    // Clipboard
    cb = QApplication::clipboard();
}

// Get values then call applyColor
void MainWindow::changeColor(QString method) {
    if(method == "HEXA") {
        QString color_code = ui->html_color->text();

        if(color_code.at(0) != '#') {
            color_code = "#" + color_code;
        }

        if(QColor::isValidColor(color_code) && color_code != html_color) {
            QColor color = QColor();
            color.setNamedColor(color_code);
            applyColor(color.red(), color.green(), color.blue(), 0);
        }
    }
    else if(method == "RGB" && ui->tabWidget->currentIndex() == 0) {
        applyColor(ui->red->value(), ui->green->value(), ui->blue->value(), 1);
    }
    else if(method == "HSL" && ui->tabWidget->currentIndex() == 1) {
        applyColor(ui->hue->value(), ui->saturation->value(), ui->lightness->value(), 2);
    }
    else if(method == "HSV" && ui->tabWidget->currentIndex() == 2) {
        applyColor(ui->hue2->value(), ui->saturation2->value(), ui->value->value(), 3);
    }
}

//  Create HTML color then change background color and create palette
void MainWindow::applyColor(int param1, int param2, int param3, int t) {
    /* t:
    * 0: HEXA
    * 1: RGB
    * 2: HSL
    * 3: HSV
    */

    QColor color;

    switch (t) {
        case 0:
            color = QColor(param1, param2, param3);
            fillValues(true, true, true, color);
            break;
        case 1:
            color = QColor(param1, param2, param3);
            fillValues(false, true, true, color);
            break;
        case 2:
            color = QColor::fromHsl(param1, param2, param3);
            fillValues(true, false, true, color);
            break;
        case 3:
            color = QColor::fromHsv(param1, param2, param3);
            fillValues(true, true, false, color);
    }

    html_color = color.name();
    ui->color_widget->setStyleSheet("background: " + html_color + ";");
    ui->html_color->setText(html_color);

    palette();
}

// Fill values of QLineEdits
void MainWindow::fillValues(bool rgb, bool hsl, bool hsv, QColor color) {
    QColor rgb_color, hsl_color, hsv_color;

    if(rgb) {
        rgb_color = color.convertTo(QColor::Rgb);
        ui->red->setValue(rgb_color.red());
        ui->green->setValue(rgb_color.green());
        ui->blue->setValue(rgb_color.blue());
    }
    if(hsl) {
        hsl_color = color.convertTo(QColor::Hsl);
        ui->hue->setValue(hsl_color.hslHue());
        ui->saturation->setValue(hsl_color.saturation());
        ui->lightness->setValue(hsl_color.lightness());
    }
    if(hsv) {
        hsv_color = color.convertTo(QColor::Hsv);
        ui->hue2->setValue(hsv_color.hue());
        ui->saturation2->setValue(hsv_color.saturation());
        ui->value->setValue(hsv_color.value());
    }
}

// Create palette
void MainWindow::palette() {
    QColor color = QColor(html_color);

    // Original color
    ui->color1->setStyleSheet("background: " + html_color + ";");
    ui->color1_html->setText(html_color);

    QString color2 = color.lighter(150).name();
    ui->color2->setStyleSheet("background: " + color2 + ";");
    ui->color2_html->setText(color2);

    QString color3 = color.darker(150).name();
    ui->color3->setStyleSheet("background: " + color3 + ";");
    ui->color3_html->setText(color3);

    QString color4 = color.darker(300).name();
    ui->color4->setStyleSheet("background: " + color4 + ";");
    ui->color4_html->setText(color4);
}

// Copy a color into clipboard by pressing "copy" button
void MainWindow::colorToClipboard() {
    cb->setText(html_color);
}

// About window
void MainWindow::about() {
    QMessageBox::information(this, tr("About"), tr("Coulr is a free color box software develop by <a href=\"https://github.com/Huluti\">Hugo Posnic</a> using <a href=\"http://qt-project.org/\">Qt 5</a>. Software under <a href=\"https://github.com/Huluti/Coulr/blob/master/LICENSE\">MIT Licence</a>.<br><br> Version : ") + version);
}

// Save last color at close
void MainWindow::closeEvent(QCloseEvent *event) {
    QSettings settings("Coulr", "Coulr");
    settings.setValue("last_color", html_color);

    event->accept();
}

MainWindow::~MainWindow() {
    delete ui;
}
