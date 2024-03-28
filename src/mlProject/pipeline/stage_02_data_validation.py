from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidaton
from mlProject import logger

STAGE_NAME = "Data Validation Stage"

class DatavalidationTrainingPipeline :
    def __init__(self) :
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_validation_config()
        data_validation = DataValidaton(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=='__main__':
    try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = DatavalidationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x=========x')
    except Exception as e:
        logger.exception(e)
        raise e