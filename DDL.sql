DROP TABLE IF EXISTS `douban_proxy`;
CREATE TABLE `douban_proxy` (
  `id`  BIGINT NOT NULL AUTO_INCREMENT COMMENT '',
  `ip` VARCHAR(32) NOT NULL COMMENT 'ip',
  `speed`  DECIMAL(10,2) NOT NULL comment '速度(秒)',
  PRIMARY KEY (`id`),
  INDEX `idx_ip_port` (`ip`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COMMENT='代理表';



DROP TABLE IF EXISTS `douban_group`;
CREATE TABLE `douban_group` (
  `id`  BIGINT NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(32) NOT NULL COMMENT '小组名',
  `url`  VARCHAR(128) NOT NULL comment '小组地址',
  `matchCount` INT NOT NULL DEFAULT '0' comment '匹配数量',
  PRIMARY KEY (`id`),
  UNIQUE `idx_url` (`url`)
) ENGINE=INNODB DEFAULT CHARSET=utf8 COMMENT='豆瓣组';

