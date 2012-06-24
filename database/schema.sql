use woocode;
drop table  if exists `repo`;
create table repo(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_repo_id` int(11) NOT NULL DEFAULT '0',
  `owner_id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(1) NOT NULL DEFAULT '',
  `desc` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index3` (`owner_id`,`name`)
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


drop table  if exists `pull_request`;
create table pull_request(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_repo_id` int(11) NOT NULL,
  `to_repo_id` int(11) NOT NULL,
  `from_branch` varchar(100) NOT NULL,
  `to_branch` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(1) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `idx_status` (`from_repo_id`, `to_repo_id`, `user_id`, `status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='movie report';
