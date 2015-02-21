/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QSlider>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionQuitter;
    QAction *actionPick_color;
    QAction *actionAbout;
    QWidget *centralWidget;
    QGridLayout *gridLayout_2;
    QTabWidget *tabWidget1;
    QWidget *tabWidgetPage1;
    QVBoxLayout *verticalLayout;
    QWidget *color_widget;
    QLineEdit *html_color;
    QWidget *tab_4;
    QGridLayout *gridLayout_5;
    QWidget *color3;
    QWidget *color4;
    QWidget *color1;
    QWidget *color2;
    QLineEdit *color2_html;
    QLineEdit *color1_html;
    QLineEdit *color3_html;
    QLineEdit *color4_html;
    QTabWidget *tabWidget;
    QWidget *tab;
    QGridLayout *gridLayout;
    QLabel *label_3;
    QSlider *horizontalSlider_2;
    QLabel *label_2;
    QSlider *horizontalSlider_3;
    QSpinBox *red;
    QLabel *label;
    QSpinBox *green;
    QSpinBox *blue;
    QSlider *horizontalSlider;
    QWidget *tab_2;
    QGridLayout *gridLayout_3;
    QLabel *label_4;
    QSpinBox *lightness;
    QSpinBox *saturation;
    QLabel *label_5;
    QLabel *label_6;
    QSpinBox *hue;
    QSlider *horizontalSlider_4;
    QSlider *horizontalSlider_5;
    QSlider *horizontalSlider_6;
    QWidget *tab_3;
    QGridLayout *gridLayout_4;
    QSpinBox *hue2;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QSpinBox *saturation2;
    QSpinBox *value;
    QSlider *horizontalSlider_7;
    QSlider *horizontalSlider_8;
    QSlider *horizontalSlider_9;
    QMenuBar *menuBar;
    QToolBar *toolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(725, 317);
        QIcon icon;
        QString iconThemeName = QStringLiteral("coulr");
        if (QIcon::hasThemeIcon(iconThemeName)) {
            icon = QIcon::fromTheme(iconThemeName);
        } else {
            icon.addFile(QStringLiteral(""), QSize(), QIcon::Normal, QIcon::Off);
        }
        MainWindow->setWindowIcon(icon);
        actionQuitter = new QAction(MainWindow);
        actionQuitter->setObjectName(QStringLiteral("actionQuitter"));
        actionPick_color = new QAction(MainWindow);
        actionPick_color->setObjectName(QStringLiteral("actionPick_color"));
        actionPick_color->setCheckable(false);
        QIcon icon1;
        icon1.addFile(QStringLiteral("icons/picker.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionPick_color->setIcon(icon1);
        actionAbout = new QAction(MainWindow);
        actionAbout->setObjectName(QStringLiteral("actionAbout"));
        QIcon icon2;
        iconThemeName = QStringLiteral("help-about");
        if (QIcon::hasThemeIcon(iconThemeName)) {
            icon2 = QIcon::fromTheme(iconThemeName);
        } else {
            icon2.addFile(QStringLiteral(""), QSize(), QIcon::Normal, QIcon::Off);
        }
        actionAbout->setIcon(icon2);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout_2 = new QGridLayout(centralWidget);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        tabWidget1 = new QTabWidget(centralWidget);
        tabWidget1->setObjectName(QStringLiteral("tabWidget1"));
        tabWidget1->setMinimumSize(QSize(172, 0));
        tabWidgetPage1 = new QWidget();
        tabWidgetPage1->setObjectName(QStringLiteral("tabWidgetPage1"));
        verticalLayout = new QVBoxLayout(tabWidgetPage1);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
        color_widget = new QWidget(tabWidgetPage1);
        color_widget->setObjectName(QStringLiteral("color_widget"));

        verticalLayout->addWidget(color_widget);

        html_color = new QLineEdit(tabWidgetPage1);
        html_color->setObjectName(QStringLiteral("html_color"));

        verticalLayout->addWidget(html_color);

        tabWidget1->addTab(tabWidgetPage1, QString());
        tab_4 = new QWidget();
        tab_4->setObjectName(QStringLiteral("tab_4"));
        gridLayout_5 = new QGridLayout(tab_4);
        gridLayout_5->setSpacing(6);
        gridLayout_5->setContentsMargins(11, 11, 11, 11);
        gridLayout_5->setObjectName(QStringLiteral("gridLayout_5"));
        color3 = new QWidget(tab_4);
        color3->setObjectName(QStringLiteral("color3"));

        gridLayout_5->addWidget(color3, 2, 0, 1, 1);

        color4 = new QWidget(tab_4);
        color4->setObjectName(QStringLiteral("color4"));

        gridLayout_5->addWidget(color4, 2, 1, 1, 1);

        color1 = new QWidget(tab_4);
        color1->setObjectName(QStringLiteral("color1"));

        gridLayout_5->addWidget(color1, 0, 0, 1, 1);

        color2 = new QWidget(tab_4);
        color2->setObjectName(QStringLiteral("color2"));

        gridLayout_5->addWidget(color2, 0, 1, 1, 1);

        color2_html = new QLineEdit(tab_4);
        color2_html->setObjectName(QStringLiteral("color2_html"));

        gridLayout_5->addWidget(color2_html, 1, 1, 1, 1);

        color1_html = new QLineEdit(tab_4);
        color1_html->setObjectName(QStringLiteral("color1_html"));

        gridLayout_5->addWidget(color1_html, 1, 0, 1, 1);

        color3_html = new QLineEdit(tab_4);
        color3_html->setObjectName(QStringLiteral("color3_html"));

        gridLayout_5->addWidget(color3_html, 3, 0, 1, 1);

        color4_html = new QLineEdit(tab_4);
        color4_html->setObjectName(QStringLiteral("color4_html"));

        gridLayout_5->addWidget(color4_html, 3, 1, 1, 1);

        tabWidget1->addTab(tab_4, QString());

        gridLayout_2->addWidget(tabWidget1, 0, 1, 1, 1);

        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tab = new QWidget();
        tab->setObjectName(QStringLiteral("tab"));
        gridLayout = new QGridLayout(tab);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        label_3 = new QLabel(tab);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout->addWidget(label_3, 0, 0, 1, 1);

        horizontalSlider_2 = new QSlider(tab);
        horizontalSlider_2->setObjectName(QStringLiteral("horizontalSlider_2"));
        horizontalSlider_2->setMaximum(255);
        horizontalSlider_2->setOrientation(Qt::Horizontal);

        gridLayout->addWidget(horizontalSlider_2, 1, 2, 1, 1);

        label_2 = new QLabel(tab);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        horizontalSlider_3 = new QSlider(tab);
        horizontalSlider_3->setObjectName(QStringLiteral("horizontalSlider_3"));
        horizontalSlider_3->setMaximum(255);
        horizontalSlider_3->setOrientation(Qt::Horizontal);

        gridLayout->addWidget(horizontalSlider_3, 2, 2, 1, 1);

        red = new QSpinBox(tab);
        red->setObjectName(QStringLiteral("red"));
        red->setMaximum(255);

        gridLayout->addWidget(red, 0, 1, 1, 1);

        label = new QLabel(tab);
        label->setObjectName(QStringLiteral("label"));

        gridLayout->addWidget(label, 2, 0, 1, 1);

        green = new QSpinBox(tab);
        green->setObjectName(QStringLiteral("green"));
        green->setMaximum(255);

        gridLayout->addWidget(green, 1, 1, 1, 1);

        blue = new QSpinBox(tab);
        blue->setObjectName(QStringLiteral("blue"));
        blue->setMaximum(255);

        gridLayout->addWidget(blue, 2, 1, 1, 1);

        horizontalSlider = new QSlider(tab);
        horizontalSlider->setObjectName(QStringLiteral("horizontalSlider"));
        horizontalSlider->setMaximum(255);
        horizontalSlider->setOrientation(Qt::Horizontal);

        gridLayout->addWidget(horizontalSlider, 0, 2, 1, 1);

        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QStringLiteral("tab_2"));
        gridLayout_3 = new QGridLayout(tab_2);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        label_4 = new QLabel(tab_2);
        label_4->setObjectName(QStringLiteral("label_4"));

        gridLayout_3->addWidget(label_4, 0, 0, 1, 1);

        lightness = new QSpinBox(tab_2);
        lightness->setObjectName(QStringLiteral("lightness"));
        lightness->setMaximum(255);

        gridLayout_3->addWidget(lightness, 3, 1, 1, 1);

        saturation = new QSpinBox(tab_2);
        saturation->setObjectName(QStringLiteral("saturation"));
        saturation->setMaximum(255);

        gridLayout_3->addWidget(saturation, 2, 1, 1, 1);

        label_5 = new QLabel(tab_2);
        label_5->setObjectName(QStringLiteral("label_5"));

        gridLayout_3->addWidget(label_5, 2, 0, 1, 1);

        label_6 = new QLabel(tab_2);
        label_6->setObjectName(QStringLiteral("label_6"));

        gridLayout_3->addWidget(label_6, 3, 0, 1, 1);

        hue = new QSpinBox(tab_2);
        hue->setObjectName(QStringLiteral("hue"));
        hue->setMaximum(359);

        gridLayout_3->addWidget(hue, 0, 1, 1, 1);

        horizontalSlider_4 = new QSlider(tab_2);
        horizontalSlider_4->setObjectName(QStringLiteral("horizontalSlider_4"));
        horizontalSlider_4->setMaximum(360);
        horizontalSlider_4->setOrientation(Qt::Horizontal);

        gridLayout_3->addWidget(horizontalSlider_4, 0, 2, 1, 1);

        horizontalSlider_5 = new QSlider(tab_2);
        horizontalSlider_5->setObjectName(QStringLiteral("horizontalSlider_5"));
        horizontalSlider_5->setMaximum(255);
        horizontalSlider_5->setOrientation(Qt::Horizontal);

        gridLayout_3->addWidget(horizontalSlider_5, 2, 2, 1, 1);

        horizontalSlider_6 = new QSlider(tab_2);
        horizontalSlider_6->setObjectName(QStringLiteral("horizontalSlider_6"));
        horizontalSlider_6->setMaximum(255);
        horizontalSlider_6->setOrientation(Qt::Horizontal);

        gridLayout_3->addWidget(horizontalSlider_6, 3, 2, 1, 1);

        tabWidget->addTab(tab_2, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QStringLiteral("tab_3"));
        gridLayout_4 = new QGridLayout(tab_3);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        hue2 = new QSpinBox(tab_3);
        hue2->setObjectName(QStringLiteral("hue2"));
        hue2->setMaximum(359);

        gridLayout_4->addWidget(hue2, 0, 1, 1, 1);

        label_7 = new QLabel(tab_3);
        label_7->setObjectName(QStringLiteral("label_7"));

        gridLayout_4->addWidget(label_7, 0, 0, 1, 1);

        label_8 = new QLabel(tab_3);
        label_8->setObjectName(QStringLiteral("label_8"));

        gridLayout_4->addWidget(label_8, 1, 0, 1, 1);

        label_9 = new QLabel(tab_3);
        label_9->setObjectName(QStringLiteral("label_9"));

        gridLayout_4->addWidget(label_9, 2, 0, 1, 1);

        saturation2 = new QSpinBox(tab_3);
        saturation2->setObjectName(QStringLiteral("saturation2"));
        saturation2->setMaximum(255);

        gridLayout_4->addWidget(saturation2, 1, 1, 1, 1);

        value = new QSpinBox(tab_3);
        value->setObjectName(QStringLiteral("value"));
        value->setMaximum(255);

        gridLayout_4->addWidget(value, 2, 1, 1, 1);

        horizontalSlider_7 = new QSlider(tab_3);
        horizontalSlider_7->setObjectName(QStringLiteral("horizontalSlider_7"));
        horizontalSlider_7->setMaximum(359);
        horizontalSlider_7->setOrientation(Qt::Horizontal);

        gridLayout_4->addWidget(horizontalSlider_7, 0, 2, 1, 1);

        horizontalSlider_8 = new QSlider(tab_3);
        horizontalSlider_8->setObjectName(QStringLiteral("horizontalSlider_8"));
        horizontalSlider_8->setMaximum(255);
        horizontalSlider_8->setOrientation(Qt::Horizontal);

        gridLayout_4->addWidget(horizontalSlider_8, 1, 2, 1, 1);

        horizontalSlider_9 = new QSlider(tab_3);
        horizontalSlider_9->setObjectName(QStringLiteral("horizontalSlider_9"));
        horizontalSlider_9->setMaximum(255);
        horizontalSlider_9->setOrientation(Qt::Horizontal);

        gridLayout_4->addWidget(horizontalSlider_9, 2, 2, 1, 1);

        tabWidget->addTab(tab_3, QString());

        gridLayout_2->addWidget(tabWidget, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 725, 25));
        MainWindow->setMenuBar(menuBar);
        toolBar = new QToolBar(MainWindow);
        toolBar->setObjectName(QStringLiteral("toolBar"));
        toolBar->setAllowedAreas(Qt::AllToolBarAreas);
        MainWindow->addToolBar(Qt::LeftToolBarArea, toolBar);
        QWidget::setTabOrder(tabWidget1, red);
        QWidget::setTabOrder(red, horizontalSlider);
        QWidget::setTabOrder(horizontalSlider, green);
        QWidget::setTabOrder(green, horizontalSlider_2);
        QWidget::setTabOrder(horizontalSlider_2, blue);
        QWidget::setTabOrder(blue, horizontalSlider_3);
        QWidget::setTabOrder(horizontalSlider_3, html_color);

        toolBar->addAction(actionAbout);

        retranslateUi(MainWindow);
        QObject::connect(red, SIGNAL(valueChanged(int)), horizontalSlider, SLOT(setValue(int)));
        QObject::connect(horizontalSlider, SIGNAL(valueChanged(int)), red, SLOT(setValue(int)));
        QObject::connect(green, SIGNAL(valueChanged(int)), horizontalSlider_2, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_2, SIGNAL(valueChanged(int)), green, SLOT(setValue(int)));
        QObject::connect(blue, SIGNAL(valueChanged(int)), horizontalSlider_3, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_3, SIGNAL(valueChanged(int)), blue, SLOT(setValue(int)));
        QObject::connect(hue, SIGNAL(valueChanged(int)), horizontalSlider_4, SLOT(setValue(int)));
        QObject::connect(saturation, SIGNAL(valueChanged(int)), horizontalSlider_5, SLOT(setValue(int)));
        QObject::connect(lightness, SIGNAL(valueChanged(int)), horizontalSlider_6, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_6, SIGNAL(valueChanged(int)), lightness, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_4, SIGNAL(valueChanged(int)), hue, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_5, SIGNAL(valueChanged(int)), saturation, SLOT(setValue(int)));
        QObject::connect(hue2, SIGNAL(valueChanged(int)), horizontalSlider_7, SLOT(setValue(int)));
        QObject::connect(saturation2, SIGNAL(valueChanged(int)), horizontalSlider_8, SLOT(setValue(int)));
        QObject::connect(value, SIGNAL(valueChanged(int)), horizontalSlider_9, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_7, SIGNAL(valueChanged(int)), hue2, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_8, SIGNAL(valueChanged(int)), saturation2, SLOT(setValue(int)));
        QObject::connect(horizontalSlider_9, SIGNAL(valueChanged(int)), value, SLOT(setValue(int)));

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Coulr", 0));
        actionQuitter->setText(QApplication::translate("MainWindow", "Quit", 0));
        actionPick_color->setText(QApplication::translate("MainWindow", "Pick color", 0));
        actionAbout->setText(QApplication::translate("MainWindow", "About", 0));
        html_color->setPlaceholderText(QString());
        tabWidget1->setTabText(tabWidget1->indexOf(tabWidgetPage1), QApplication::translate("MainWindow", "Render", 0));
        tabWidget1->setTabText(tabWidget1->indexOf(tab_4), QApplication::translate("MainWindow", "Palette", 0));
        label_3->setText(QApplication::translate("MainWindow", "R", 0));
        label_2->setText(QApplication::translate("MainWindow", "G", 0));
        label->setText(QApplication::translate("MainWindow", "B", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("MainWindow", "RGB", 0));
        label_4->setText(QApplication::translate("MainWindow", "H", 0));
        label_5->setText(QApplication::translate("MainWindow", "S", 0));
        label_6->setText(QApplication::translate("MainWindow", "L", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("MainWindow", "HSL", 0));
        label_7->setText(QApplication::translate("MainWindow", "H", 0));
        label_8->setText(QApplication::translate("MainWindow", "S", 0));
        label_9->setText(QApplication::translate("MainWindow", "V", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QApplication::translate("MainWindow", "HSV", 0));
        toolBar->setWindowTitle(QApplication::translate("MainWindow", "toolBar", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
