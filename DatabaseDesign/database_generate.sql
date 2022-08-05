CREATE TABLE `Image`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `source_url` VARCHAR(255) NOT NULL COMMENT 'URL pointing to embeddable image',
    `attribution_url` VARCHAR(255) NOT NULL COMMENT 'URL pointing to the website where the image is used from',
    `attribution_text` VARCHAR(255) NULL COMMENT 'Attribution text to be shown instead of \"Image Source\"'
);
CREATE TABLE `Post`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(255) NOT NULL,
    `publish_date` DATETIME NOT NULL,
    `content` TEXT NOT NULL COMMENT 'HTML rich text content to be rendered.',
    `author_id` INT UNSIGNED NOT NULL COMMENT 'One or more author(s)',
    `cover_image_id` INT UNSIGNED NOT NULL,
    `category_id` INT UNSIGNED NOT NULL
);
CREATE TABLE `Author`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
CREATE TABLE `Post_Author`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `author_id` INT UNSIGNED NOT NULL
);
CREATE TABLE `Category`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Post` ADD CONSTRAINT `post_cover_image_id_foreign` FOREIGN KEY(`cover_image_id`) REFERENCES `Image`(`id`);
ALTER TABLE
    `Post` ADD CONSTRAINT `post_author_id_foreign` FOREIGN KEY(`author_id`) REFERENCES `Post_Author`(`id`);
ALTER TABLE
    `Post_Author` ADD CONSTRAINT `post_author_author_id_foreign` FOREIGN KEY(`author_id`) REFERENCES `Author`(`id`);
ALTER TABLE
    `Post` ADD CONSTRAINT `post_category_id_foreign` FOREIGN KEY(`category_id`) REFERENCES `Category`(`id`);