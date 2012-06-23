use woocode;
drop table  if exists `repo`;
create table repo(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `path` varchar(100) NOT NULL UNIQUE,
  `status` varchar(1) NOT NULL DEFAULT '',
  `desc` text,
  PRIMARY KEY (`id`),
  KEY `idx_status` (`owner_id`, `name`, `status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='movie report';


drop table  if exists `user`;
create table user(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(100) NOT NULL UNIQUE,
  `email` varchar(100) NOT NULL UNIQUE,
  `password` varchar(100) NOT NULL,
  `status` varchar(1) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `idx_status` (`name`, `status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='movie report';
