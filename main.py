from insurancePP.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from insurancePP.pipeline.stage2_data_validation import DataValidationPipeline
from insurancePP.pipeline.stage3_data_transformation import DataTransformationPipeline
from insurancePP.pipeline.stage4_model_trainer import ModelTrainingPipeline
# from textSummerizer.pipeline.stage5_model_evaluation import ModelEvaluationPipeline
from insurancePP.logging import logger

STAGE_NAME = 'data_ingestion_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e

STAGE_NAME = 'data_validation_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e


STAGE_NAME = 'data_transformation'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e


STAGE_NAME = 'model_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e
