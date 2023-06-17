INSERT INTO MEMBER
(Name, Phone, Pwd, Gender, Birthday, MLevel, MPoints , MAccumSpend)
VALUES 
('Penny', '0988088088', '36f583dd16f4e1e201eb1e6f6d8e35a2ccb3bbe2658de46b4ffae7b0e9ed872e','Female','2000-01-01', '1', '0', '0'),
('Apple', '0987654321', 'ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae','Female','2023-05-01', '1', '0', '0'),
('Alice', '0989898808', 'ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae',null, '1987-06-15','1', '0', '0'),
('John', '0938674532', 'ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae','Male', '1970-10-10','1', '0', '0');

INSERT INTO RESTAURANT
(RName, RPhone, RAddress, RAccount, RPwd, URL)
VALUES
('Yummy','0223222322','台北市文山區','yummy','4359dbe2796b11d2c9c214a5d3a9b505db2ad679254d3f4fad30baf44e6e2944','https://'),
('Good','0212345678','新北市永和區','good','42a99bd1f0f175a03f3f45af820cdfdcbaca8dcd457ed5401d1d5ac1319be374','https://');


INSERT INTO SEATS
(RID, TNo, Seats)
VALUES
('1','A1','2'),
('1','A2','2'),
('1','B1','4'),
('1','B2','4'),
('1','C1','6'),
('1','C2','6'),
('2','A1','2'),
('2','A2','2'),
('2','B1','4'),
('2','B2','4'),
('2','C1','6'),
('2','C2','6');


INSERT INTO RESERVATION
(ReRID, ReMID, Reason, CreateTime, ReTime, ReTNo, RePerson)
VALUES
('2','4','約會','2023-06-06 23:48:00','2023-06-06 12:00:00','A1','2'),
('1','4','聚餐','2023-06-06 23:48:00','2023-06-15 18:00:00','B1','4');
