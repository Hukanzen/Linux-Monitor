/* ユーザ作成 */
CREATE USER 'user1'@'10.0.1.%' IDENTIFIED BY 'password';

CREATE DATABASE IF NOT EXISTS `Machine` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

GRANT  INSERT,SELECT,UPDATE ON `Machine`.* TO 'user1'@'10.0.1.%';

CREATE TABLE `Machine`.`ReportData`(
	count   INTEGER UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
	ipaddr    INTEGER UNSIGNED NOT NULL,
	la1min    FLOAT            NOT NULL,
	la5min    FLOAT            NOT NULL,
	la15min   FLOAT            NOT NULL,
	delay     INTEGER          NOT NULL,
	cpuUsage  INTEGER          NOT NULL,
	memUsage  INTEGER          NOT NULL,
	diskUsage INTEGER          NOT NULL,
	hostname  VARCHAR(30)      NOT NULL,
	gettime   DATETIME         NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8;