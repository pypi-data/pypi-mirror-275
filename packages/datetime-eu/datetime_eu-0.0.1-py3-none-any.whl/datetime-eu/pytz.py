database.py:

import pymysql
from pymysql import MySQLError

class Database:
    def __init__(self,host,user,password,database):
        try:
            self.connection = pymysql.connect(host=host, user=user, password=password, database=database)
            self.cursor = self.connection.cursor()
            print("Успешное подключение!")

        except MySQLError as e:
            print(f"Ошибка {e}")

db = Database(host='localhost', user='root', password='', database='book_club')


----------------------------------------------------------------------------------------------------------

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 28 2024 г., 03:57
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `2233`
--

-- --------------------------------------------------------

--
-- Структура таблицы `category`
--

CREATE TABLE `category` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'Художественная литература'),
(2, 'Научная фантастика'),
(3, 'Фэнтези'),
(4, 'Нон-фикшн'),
(5, 'Психология и саморазвитие');

-- --------------------------------------------------------

--
-- Структура таблицы `orderdetails`
--

CREATE TABLE `orderdetails` (
  `id` int NOT NULL,
  `product_id` int NOT NULL,
  `user_id` int NOT NULL,
  `price` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `orderdetails`
--

INSERT INTO `orderdetails` (`id`, `product_id`, `user_id`, `price`) VALUES
(8, 11, 3, 200);

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `id` int NOT NULL,
  `orderdate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ordernumber` int NOT NULL,
  `totalamount` decimal(10,0) NOT NULL,
  `discountamount` int DEFAULT NULL,
  `orderstatus` varchar(50) NOT NULL DEFAULT 'новый',
  `pickup_id` int NOT NULL,
  `pickup_code` varchar(50) NOT NULL,
  `id_order_details` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`id`, `orderdate`, `ordernumber`, `totalamount`, `discountamount`, `orderstatus`, `pickup_id`, `pickup_code`, `id_order_details`) VALUES
(1, '2024-05-28 03:57:12', 1, '200', NULL, 'новый', 1, 'random_code', 8);

-- --------------------------------------------------------

--
-- Структура таблицы `pickuppoint`
--

CREATE TABLE `pickuppoint` (
  `id` int NOT NULL,
  `adress` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `pickuppoint`
--

INSERT INTO `pickuppoint` (`id`, `adress`) VALUES
(1, 'Улица Тверская, дом 15, Москва'),
(2, 'Проспект Мира, дом 101, Москва'),
(3, 'Ленинский проспект, дом 45, Москва'),
(4, 'Улица Новый Арбат, дом 10, Москва'),
(5, 'Кутузовский проспект, дом 30, Москва'),
(6, 'Улица Профсоюзная, дом 56, Москва');

-- --------------------------------------------------------

--
-- Структура таблицы `product`
--

CREATE TABLE `product` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(250) NOT NULL,
  `manufactur` varchar(250) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `count` int NOT NULL,
  `discount` int DEFAULT NULL,
  `image` longblob,
  `category_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `product`
--

INSERT INTO `product` (`id`, `name`, `description`, `manufactur`, `price`, `count`, `discount`, `image`, `category_id`) VALUES
(1, '\"Война и мир\" - Лев Толстой', 'Эпическая хроника о жизни русских аристократов в начале 19 века, охватывающая события войны с Наполеоном.', 'Издательство \"Азбука\"', '750', 12, NULL, 0x30, 1),
(2, '\"Преступление и наказание\" - Федор Достоевский', 'Психологический роман о молодом студенте, который совершает убийство и затем переживает угрызения совести.', 'Издательство \"Эксмо\"', '330', 8, NULL, 0x30, 1),
(3, '\"1984\" - Джордж Оруэлл', 'Антиутопия о тоталитарном обществе, где правительство контролирует все аспекты жизни граждан.', 'Издательство \"АСТ\"', '570', 17, NULL, 0x30, 2),
(4, '\"Дюна\" - Фрэнк Герберт', 'Эпическая сага о политических интригах и борьбе за контроль над пустынной планетой Арракис.', 'Издательство \"Альфа-книга\"', '110', 4, NULL, 0x30, 2),
(5, '\"Властелин колец\" - Дж. Р. Р. Толкин', 'История о борьбе за уничтожение могущественного кольца, которое может принести зло в мир Средиземья.', 'Издательство \"Росмэн\"', '770', 23, NULL, 0x30, 3),
(8, '\"Игра престолов\" - Джордж Р. Р. Мартин', 'Политическая интрига и борьба за трон в вымышленном мире Вестерос.', 'Издательство \"АСТ\"', '3210', 13, NULL, 0x30, 3),
(11, '\"Краткая история времени\" - Стивен Хокинг', 'Научно-популярная книга, объясняющая сложные концепции космологии и физики доступным языком.', 'Издательство \"АСТ\"', '200', 11, NULL, 0x30, 4),
(12, '\"Sapiens\" - Юваль Ной Харари', 'Исследование истории человечества от древнейших времен до наших дней.', 'Издательство \"Синдбад\"', '400', 4, NULL, 0x30, 4),
(13, '\"Думай и богатей\" - Наполеон Хилл', 'Книга о том, как достичь успеха и богатства, основанная на изучении историй успешных людей.', 'Издательство \"Попурри\"', '780', 32, NULL, 0x30, 5),
(14, '\"Сила привычки\" - Чарльз Дахигг', 'Исследование природы привычек и методов их изменения для улучшения жизни.', 'Издательство \"Манн, Иванов и Фербер\"', '550', 350, NULL, 0x30, 5),
(15, 'авпвап', 'вапап', 'вапвап', '24', 24, NULL, 0x30, 5),
(16, 'ваыаа', 'ываыва', 'ыва', '234', 42, NULL, 0x30, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `role`
--

CREATE TABLE `role` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `role`
--

INSERT INTO `role` (`id`, `name`) VALUES
(1, 'Администратор'),
(2, 'Менеджер'),
(3, 'Клиент');

-- --------------------------------------------------------

--
-- Структура таблицы `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `username` varchar(50) NOT NULL DEFAULT 'ghost',
  `password` varchar(50) NOT NULL DEFAULT 'ghost',
  `id_role` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `id_role`) VALUES
(1, 'root', 'root', 1),
(2, 'manager', 'manager', 2),
(3, 'ghost', 'ghost', 3);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`product_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pickup_id` (`pickup_id`),
  ADD KEY `id_order_details` (`id_order_details`);

--
-- Индексы таблицы `pickuppoint`
--
ALTER TABLE `pickuppoint`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- Индексы таблицы `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_role` (`id_role`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `category`
--
ALTER TABLE `category`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `orderdetails`
--
ALTER TABLE `orderdetails`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `pickuppoint`
--
ALTER TABLE `pickuppoint`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `product`
--
ALTER TABLE `product`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT для таблицы `role`
--
ALTER TABLE `role`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD CONSTRAINT `orderdetails_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  ADD CONSTRAINT `orderdetails_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`pickup_id`) REFERENCES `pickuppoint` (`id`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`id_order_details`) REFERENCES `orderdetails` (`id`);

--
-- Ограничения внешнего ключа таблицы `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);

--
-- Ограничения внешнего ключа таблицы `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
