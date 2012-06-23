use woocode;
drop table  if exists `user`;
create table user(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(100) NOT NULL UNIQUE,
  `password` varchar(100) NOT NULL,
  `status` varchar(1) NOT NULL DEFAULT '',
   
  PRIMARY KEY (`id`),
  KEY `idx_status` (`name`, `status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='movie report';
