admin.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Admin</class>
 <widget class="QMainWindow" name="Admin">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>852</width>
    <height>614</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Admin</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QPushButton" name="pushButton_add_product">
      <property name="text">
       <string>Добавить товар</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_edit_product">
      <property name="text">
       <string>Редактировать товар</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_delete_product">
      <property name="text">
       <string>Удалить товар</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_edit_order">
      <property name="text">
       <string>Редактировать заказ</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_view_orders">
      <property name="text">
       <string>Просмотреть заказы</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="text">
       <string>Просмотр товаров</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QTableWidget" name="tableWidget"/>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>852</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
----------------------------------------------------------------------

admin_auth:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>450</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Авторизация</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>380</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>ВОЙТИ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>401</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Авторизация администратора</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>140</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(141, 141, 141);</string>
    </property>
    <property name="text">
     <string>Имя пользователя</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>170</y>
      <width>391</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(107, 107, 107);</string>
    </property>
    <property name="inputMask">
     <string/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="placeholderText">
     <string>Введите своё имя пользователя</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>270</y>
      <width>391</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(107, 107, 107);</string>
    </property>
    <property name="inputMask">
     <string/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="maxLength">
     <number>32767</number>
    </property>
    <property name="echoMode">
     <enum>QLineEdit::Password</enum>
    </property>
    <property name="dragEnabled">
     <bool>false</bool>
    </property>
    <property name="placeholderText">
     <string>Введите свой пароль</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>240</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(141, 141, 141);</string>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>450</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
-------------------------------------------------------------------------------

basket_view.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>900</width>
    <height>900</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Корзина</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>780</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>ЗАКАЗАТЬ </string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>80</y>
      <width>841</width>
      <height>451</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout"/>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>710</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>УДАЛИТЬ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>490</x>
      <y>760</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>ИТОГО:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>30</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>КОРЗИНА</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_3">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>10</y>
      <width>101</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>НАЗАД</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>630</x>
      <y>760</y>
      <width>221</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>580</y>
      <width>91</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Место выдачи</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>610</y>
      <width>821</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>900</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
------------------------------------------------------------------------------------------

client_auth.ui:


<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>450</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Авторизация</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>190</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>ТОВАРЫ</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>450</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
----------------------------------------------------------------------------------

manager.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1200</width>
    <height>1000</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1200</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1200</width>
    <height>1000</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Корзина</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QPushButton" name="pushButton_3">
      <property name="styleSheet">
       <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:10px;</string>
      </property>
      <property name="text">
       <string>НАЗАД</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_2">
      <property name="font">
       <font>
        <pointsize>16</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="text">
       <string>МЕНЕДЖЕР</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QTableWidget" name="tableWidget"/>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="styleSheet">
       <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:10px;</string>
      </property>
      <property name="text">
       <string>Показать товары</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_4">
      <property name="styleSheet">
       <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:10px;</string>
      </property>
      <property name="text">
       <string>Показать заказы</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_2">
      <property name="styleSheet">
       <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:10px;</string>
      </property>
      <property name="text">
       <string>Создать заказ</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_5">
      <property name="styleSheet">
       <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:10px;</string>
      </property>
      <property name="text">
       <string>Редактировать заказ</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1200</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
------------------------------------------------------------------------------------

manager_auth.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>450</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>450</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Авторизация</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>380</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>ВОЙТИ</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>401</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Авторизация менеджера</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>140</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(141, 141, 141);</string>
    </property>
    <property name="text">
     <string>Имя пользователя</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>170</y>
      <width>391</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(107, 107, 107);</string>
    </property>
    <property name="inputMask">
     <string/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="placeholderText">
     <string>Введите своё имя пользователя</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>270</y>
      <width>391</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(107, 107, 107);</string>
    </property>
    <property name="inputMask">
     <string/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="maxLength">
     <number>32767</number>
    </property>
    <property name="echoMode">
     <enum>QLineEdit::Password</enum>
    </property>
    <property name="dragEnabled">
     <bool>false</bool>
    </property>
    <property name="placeholderText">
     <string>Введите свой пароль</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>240</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>9</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(141, 141, 141);</string>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>450</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
---------------------------------------------------------------------------------------

products_view.ui:

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>900</width>
    <height>900</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>900</width>
    <height>900</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Продукты</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>790</y>
      <width>301</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 75 10pt &quot;Microsoft YaHei UI&quot;;
font-weight: bold;
color: rgb(255, 255, 255);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
border-style: solid;
border-radius:21px;</string>
    </property>
    <property name="text">
     <string>КОРЗИНА</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>40</y>
      <width>751</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
   </widget>
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>150</y>
      <width>841</width>
      <height>591</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout"/>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>800</y>
      <width>341</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>20</y>
      <width>131</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Выберите категорию</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>100</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Товары</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>900</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Сотрудник?</string>
    </property>
    <addaction name="action"/>
    <addaction name="action_2"/>
    <addaction name="action_3"/>
   </widget>
   <addaction name="menu"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action">
   <property name="text">
    <string>Администратор</string>
   </property>
  </action>
  <action name="action_2">
   <property name="text">
    <string>Менеджнр</string>
   </property>
  </action>
  <action name="action_3">
   <property name="text">
    <string>Клиент</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
