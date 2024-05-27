import os
import sys

from loguru import logger


async def load_extensions(bot, folder: str):
    try:
        logger.info("Load modules...")
        src_directory = os.path.join(folder)
        sys.path.append(src_directory)
        
        for directory in os.listdir(src_directory):
            directory_path = os.path.join(src_directory, directory)

            if os.path.isdir(directory_path) and directory != "utils":
                for filename in os.listdir(directory_path):
                    bot.load_extension(f"{directory}.{filename[:-3]}")
                    logger.info("Starting bot...")

    except Exception as e:
        logger.error(f"Произошла ошибка при загрузке модулей\n╰─> Ошибка: {e}")
