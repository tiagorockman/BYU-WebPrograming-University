-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`artist`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`artist` ;

CREATE TABLE IF NOT EXISTS `mydb`.`artist` (
  `artist_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `middle_name` VARCHAR(45) NULL,
  `artist_last_name` VARCHAR(45) NULL,
  `year_of_birth` INT NULL,
  `year_of_death` INT NULL,
  `country` VARCHAR(45) NULL,
  `local` ENUM('y', 'n') NULL,
  PRIMARY KEY (`artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`artwork`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`artwork` ;

CREATE TABLE IF NOT EXISTS `mydb`.`artwork` (
  `artwork_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  `year` VARCHAR(4) NULL,
  `period` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  `file` VARCHAR(100) NULL,
  `artist_id` INT NOT NULL,
  PRIMARY KEY (`artwork_id`),
  INDEX `fk_artwork_artist_idx` (`artist_id` ASC) VISIBLE,
  CONSTRAINT `fk_artwork_artist`
    FOREIGN KEY (`artist_id`)
    REFERENCES `mydb`.`artist` (`artist_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = '		';


-- -----------------------------------------------------
-- Table `mydb`.`keyword`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`keyword` ;

CREATE TABLE IF NOT EXISTS `mydb`.`keyword` (
  `keyword_id` INT NOT NULL AUTO_INCREMENT,
  `keyword` VARCHAR(50) NULL,
  PRIMARY KEY (`keyword_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`keyword_has_artwork`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`keyword_has_artwork` ;

CREATE TABLE IF NOT EXISTS `mydb`.`keyword_has_artwork` (
  `keyword_id` INT NOT NULL,
  `artwork_id` INT NOT NULL,
  PRIMARY KEY (`keyword_id`, `artwork_id`),
  INDEX `fk_keyword_has_artwork_artwork1_idx` (`artwork_id` ASC) VISIBLE,
  INDEX `fk_keyword_has_artwork_keyword1_idx` (`keyword_id` ASC) VISIBLE,
  CONSTRAINT `fk_keyword_has_artwork_keyword1`
    FOREIGN KEY (`keyword_id`)
    REFERENCES `mydb`.`keyword` (`keyword_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_keyword_has_artwork_artwork1`
    FOREIGN KEY (`artwork_id`)
    REFERENCES `mydb`.`artwork` (`artwork_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
