use woocode;
drop table  if exists `repo`;
create table repo(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `path` varchar(100) NOT NULL UNIQUE,
  `status` varchar(1) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `idx_status` (`user_id`, `name`, `status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='movie report';
