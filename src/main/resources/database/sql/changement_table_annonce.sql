ALTER TABLE `immobilier`.`modifiee` 
ADD COLUMN `id` INT NULL FIRST;

UPDATE modifiee
SET id = (@rownum := 1 + @rownum)
WHERE 0 = (@rownum:=0)
ORDER BY id
LIMIT 20000;

ALTER TABLE `immobilier`.`modifiee` 
CHANGE COLUMN `id` `id` INT UNSIGNED NOT NULL ,
ADD PRIMARY KEY (`id`),
ADD UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE;

ALTER TABLE modifiee MODIFY COLUMN id BIGINT auto_increment;

ALTER TABLE `immobilier`.`modifiee` 
RENAME TO  `immobilier`.`annonce`;